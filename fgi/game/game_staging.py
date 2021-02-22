# -*- coding: utf-8 -*-

# 
# Copyright (C) 2020 Utopic Panther
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

from .tag import Tag
from fgi.link import uri_to_src

class GameDescription:
    def __init__(self, game, data):
        self.fmt = "plain"

        if "description-format" in data:
            self.fmt = data["description-format"]

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

class GameL10n(dict):
    def __init__(self, game, data, mtime):
        super().__init__()
        self.update(data)

        self.mtime = mtime
        self.description = None
        self.thumbnail_uri = None

        self["mtime"] = self.mtime

        if "description" in data:
            self.description = GameDescription(game, data)

class Game(dict):
    def __init__(self, data, gid, mtime):
        super().__init__()
        self.update(data)

        self.tr = dict()
        self.id = gid
        self.mtime = mtime

        # TODO: compat code should be removed in future.
        self["tr"] = self.tr
        self["id"] = self.id
        self["mtime"] = self.mtime

        self.tags = data["tags"]

        self.authors = None
        if "authors" in data:
            self.authors = data["authors"]

        self.description = GameDescription(self, data)

        self.links = list()
        self.screenshots = list()
        self.media = list()

        if "links" in data:
            self.links = data["links"]
        if "screenshots" in data:
            self.screenshots = data["screenshots"]

        if "thumbnail" in data:
            self.thumbnail_uri = data["thumbnail"]

        if "sensitive_media" in data:
            print(f"[warning] game '{self.id}' is using deprecated property 'sensitive_media'. This property will be ignored.")
            # TODO: compat code should be removed in future.
            self["sensitive_media"] = False

        # TODO: compat code should be removed in future.
        self["media"] = self.media

        self.sensitive_media = False
        self.auto_steam_widget = data.get("auto-steam-widget", True)

    def add_l10n_data(self, ln, data, mtime):
        self.tr[ln] = GameL10n(self, data, mtime)

    def realize(self, tagmgr, mfac):
        if self.authors:
            if "author" in self.tags:
                raise ValueError("authors property conflict #/tags/author namespace")

            tmp = { "author": list() }
            tmp.update(self.tags)
            self.tags = tmp
            self["tags"] = tmp
            # FIXME: create a GameAuthor class
            for i in self.authors:
                if "standalone" not in i:
                    i["standalone"] = False
                if i["standalone"]:
                    if "avatar" in i:
                        i["hi_avatar"] = mfac.uri_to_html_image(i["avatar"], self.id)
                    if "link-uri" in i:
                        i["link_href"] = uri_to_src(i["link-uri"])
                else:
                    self.tags["author"].append(i["name"])

        else:
            # For games using legecy format or without author infomation,
            # create a STUB authors property
            self.authors = list()
            # TODO: compat code should be removed in future.
            self["authors"] = self.authors
            for i in self.tags.get("author", {}):
                tmp = dict()
                tmp["name"] = i
                tmp["@stub"] = True
                tmp["standalone"] = False
                self.authors.append(tmp)

        tagmgr.check_and_patch(self)

        self.description.realize(mfac)
        for ln, gl10n in self.tr.items():
            if gl10n.description:
                gl10n.description.realize(mfac)

                # TODO: compat code should be removed in future.
                gl10n["@desc_html"] = gl10n.description.html
                gl10n["description"] = gl10n.description.text
        self["@desc_html"] = self.description.html
        self["description"] = self.description.text

        if self.thumbnail_uri:
            self.thumbnail = mfac.uri_to_html_image(self.thumbnail_uri, self.id)

            # TODO: compat code should be removed in future.
            self["hi_thumbnail"] = self.thumbnail

        if self.auto_steam_widget:
            for i in self.links:
                if i["name"] == ".steam":
                    if i["uri"].startswith("steam:"):
                        swid = i["uri"].split(':', 1)[1]
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

        # TODO: compat code should be removed in future.
        self["sensitive_media"] = self.sensitive_media

    def has_tag(self, tag: Tag) -> bool:
        return tag.ns in self["tags"] and \
                tag.value in self["tags"][tag.ns]
