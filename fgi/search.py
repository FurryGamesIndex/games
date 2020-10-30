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

from fgi import image
from fgi.i18n import get, get_desc

class searchdb:
    def __init__(self, no_data=False):
        self.db = {}
        self.db["rtag"] = {}
        self.db["data"] = {}
        self.no_data = no_data

    def add_extra_data(self, k, v):
        self.db[k] = v

    def update(self, game):
        if 'expunge' in game:
            return

        for ns, tags in game["tags"].items():
            for v in tags:
                tag = ns + ":" + v
                if tag not in self.db["rtag"]:
                    self.db["rtag"][tag] = []
                self.db["rtag"][tag].append(game["id"])

        if not self.no_data:
            data = {}
            data["tr"] = {}
            data["name"] = game["name"]
            data["description"] = game["description"]
            data["thumbnail"] = image.uri("..", game["thumbnail"], game["id"])

            for lang in game["tr"]:
                data["tr"][lang] = {}
                if "name" in game["tr"][lang]:
                    data["tr"][lang]["name"] = game["tr"][lang]["name"]
                if "description" in game["tr"][lang]:
                    desc = game["tr"][lang]["description"]
                    desc = desc[:480] + (desc[480:] and '...')
                    data["tr"][lang]["description"] = desc

            self.db["data"][game["id"]] = data
