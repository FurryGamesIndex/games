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

from fgi.link import Link
from fgi.media import MediaFactory
from fgi.icon import IconFactory

class Author:
    def __init__(self, data, aid):
        self.id = aid
        self.games = None

        self.name = data["name"]
        self.type = data["type"]
        self.aliases = list()
        self.l10n_names = dict()
        self.avatar_uri = None
        self.avatar = None
        self.links_prepare = list()
        self.links = list()

        if "aliases" in data:
            for i in data["aliases"]:
                if type(i) == str:
                    self.aliases.append(i)
                else:
                    self.aliases.append(i["name"])
                    if "as-l10n-name-in" in i:
                        for ln in i["as-l10n-name-in"]:
                            self.l10n_names[ln] = i["name"]

        if "avatar" in data:
            self.avatar_uri = data["avatar"]

        if "links" in data:
            self.links_prepare = data["links"]

    def realize(self, mfac: MediaFactory, ifac: IconFactory, author_game_map):
        self.games = list()
        author_game_map[self.name] = self.games

        if self.avatar_uri:
            self.avatar = mfac.uri_to_html_image(self.avatar_uri, "_avatar")

        for i in self.links_prepare:
            self.links.append(Link(i, ifac))

        self.links_prepare = None
