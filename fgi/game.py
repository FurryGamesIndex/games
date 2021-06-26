# -*- coding: utf-8 -*-

# 
# Copyright (C) 2021 Utopic Panther
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# 

from html import escape
from bs4 import BeautifulSoup
from markdown2 import Markdown

from fgi.link import Link, uri_to_ua_uri

class Tag:
    def __init__(self, ns, value):
        self.ns = ns
        self.value = value

    @staticmethod
    def from_string(string):
        tmp = string.split(":", 1)
        return Tag(tmp[0], tmp[1])

class GameDescription:
    def __init__(self, game, data):
        self.fmt = "plain"
        self.brief = None

        if "description-format" in data:
            self.fmt = data["description-format"]

        if "brief-description" in data:
            self.brief = data["brief-description"]

        self.game = game
        self.text = data["description"]
        self.html = None

    def realize(self, mfac):
        if self.fmt == "plain":
            self.html = escape(self.text).replace("\n", "<br>")
        elif self.fmt == "markdown":
            # FIXME: hardcode `../..` is not good
            #        we should embed a HTMLImage object into markdown
            # FIXME: should not use the src property, webp condation will be dropped.
            markdowner = Markdown(extras={
                        "strike": None,
                        "target-blank-links": None,
                        "x-FGI-min-header-level": 2
                    },
                    inline_image_uri_filter = lambda uri: mfac.uri_to_html_image(uri, self.game.id).with_rr("../..").src)
            self.html = markdowner.convert(self.text)
            self.text = BeautifulSoup(self.html, features="html.parser").get_text()
        else:
            raise ValueError(f"description format invaild: {fmt}")

        if not self.brief:
            # FIXME: split by words, not characters.
            self.brief = self.text[:480] + (self.text[480:] and "...")
            self.brief = self.brief.replace("\n", " ")

        self.brief = self.brief.rstrip(" \n")

        self.brief_sl = self.brief.replace("\n", " ")
        self.brief_html = escape(self.brief).replace("\n", "<br />")

class GameL10n:
    def __init__(self, game, data, mtime):
        super().__init__()

        self.mtime = mtime
        self.name = None
        self.description = None
        self.links_tr = dict()

        if "name" in data:
            self.name = data["name"]

        if "description" in data:
            self.description = GameDescription(game, data)

        if "links-tr" in data:
            self.links_tr = data["links-tr"]

class GameAuthor:
    def __init__(self, stub = False, data = None):
        self.name = None
        self.standalone = False
        self.roles = list()

        self.stub = stub
        self.avatar = None
        self.avatar_uri = None
        self.link_href = None

        self.author = None

        if data:
            self.name = data["name"]

            if "standalone" in data and data["standalone"]:
                self.standalone = True
                if "avatar" in data:
                    self.avatar_uri = data["avatar"]
                if "link-uri" in data:
                    self.link_href = uri_to_ua_uri(data["link-uri"])

            if "role" in data:
                self.roles = data["role"]

    @staticmethod
    def make_stub_gameauthor(name):
        ga = GameAuthor(stub = True)
        ga.name = name
        return ga

    def realize(self, game, authors, mfac):
        if self.stub:
            return

        if self.avatar_uri:
            self.avatar = mfac.uri_to_html_image(self.avatar_uri, game.id)
        del self.avatar_uri

        if not self.standalone:
            if self.name not in authors:
                print(f"[warning] non-stub author '{self.name}' referenced without defined.")
            else:
                self.author = authors[self.name]

    def get_avatar(self):
        if self.avatar:
            return self.avatar

        if self.author and self.author.avatar:
            return self.author.avatar

        return None

class Game:
    def __init__(self, data, gid, mtime):
        super().__init__()
        self.tr = dict()
        self.id = gid
        self.mtime = mtime

        self.tags = data["tags"]

        self.authors = list()

        self.name = data["name"]
        self.description = GameDescription(self, data)

        self.expunge = False
        if "expunge" in data and data["expunge"]:
            self.expunge = True

        self.replaced_by = None
        self._replaced_by_gid = None
        if "replaced-by" in data:
            self._replaced_by_gid = data["replaced-by"]

        self.old_ids = None
        if "old-ids" in data:
            self.old_ids = data["old-ids"]

        if "authors" in data:
            if "author" in self.tags:
                raise ValueError("authors property conflict #/tags/author namespace")

            tmp = { "author": list() }
            tmp.update(self.tags)
            self.tags = tmp

            for i in data["authors"]:
                author = GameAuthor(data = i)
                self.authors.append(author)

                if not author.standalone:
                    self.tags["author"].append(author.name)
        else:
            # For games using legecy format or without author infomation,
            # create STUB author properties
            for i in self.tags.get("author", {}):
                self.authors.append(GameAuthor.make_stub_gameauthor(i))

        self.links_prepare = list()
        self.links = list()
        self.screenshots = list()
        self.media = list()

        if "links" in data:
            self.links_prepare = data["links"]

        if "screenshots" in data:
            self.screenshots = data["screenshots"]

        if "thumbnail" in data:
            self.thumbnail_uri = data["thumbnail"]

        if "sensitive_media" in data:
            print(f"[warning] game '{self.id}' is using deprecated property 'sensitive_media'. This property will be ignored.")

        self.sensitive_media = False
        self.auto_steam_widget = data.get("auto-steam-widget", True)

    def add_l10n_data(self, ln, data, mtime):
        self.tr[ln] = GameL10n(self, data, mtime)

    def link(self, games):
        if self._replaced_by_gid:
            self.replaced_by = games[self._replaced_by_gid]

        if self.old_ids:
            for i in self.old_ids:
                if i in games:
                    raise ValueError(f"Old id '{i}' of game {self.id} conflict exist game")

    def realize(self, tagmgr, mfac, ifac, authors):
        tagmgr.check_and_patch(self)

        self.description.realize(mfac)
        for ln, gl10n in self.tr.items():
            if gl10n.description:
                gl10n.description.realize(mfac)

        if self.thumbnail_uri:
            self.thumbnail = mfac.uri_to_html_image(self.thumbnail_uri, self.id)

        for i in self.authors:
            i.realize(self, authors, mfac)

        for i in self.links_prepare:
            l = Link(i, ifac)
            for ln, ldata in self.tr.items():
                l.add_l10n_name_from_trdata(ln, ldata.links_tr)

            self.links.append(l)

        self.links_prepare = None

        if self.auto_steam_widget:
            for i in self.links:
                if i.stock and i.name == "steam":
                    if i.uri.startswith("steam:"):
                        swid = i.uri.split(':', 1)[1]
                        self.media.append(mfac.create_media({
                            "type": "steam-widget",
                            "id": swid,
                        }, self.id))
                    else:
                        print("[warning] steam widget can not be added while not using the steam: URI.")

        for i in self.screenshots:
            media = mfac.create_media(i, self.id)
            self.media.append(media)
            if media.sensitive:
                self.sensitive_media = True

    def _get(self, ln: str, key: str):
        if ln in self.tr:
            l10n_value = getattr(self.tr[ln], key)
            if l10n_value:
                return l10n_value

        return getattr(self, key)

    def get_name(self, ln: str) -> str:
        return self._get(ln, "name")

    def get_description(self, ln: str) -> GameDescription:
        return self._get(ln, "description")

    def get_mtime(self, ln: str) -> int:
        if ln in self.tr:
            return max(self.tr[ln].mtime, self.mtime)
        else:
            return self.mtime

    def check_tag(self, ns: str, value: str) -> bool:
        return ns in self.tags and \
                value in self.tags[ns]

    def has_tag(self, tag: Tag) -> bool:
        return self.check_tag(tag.ns, tag.value)
