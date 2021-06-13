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

import os
import json
import base64

class SearchDatabase:
    def __init__(self, fctx, no_data=False):
        self.fctx = fctx

        self.db = {}
        self.db["rtag"] = {}
        self.db["data"] = {}
        self.no_data = no_data

    def add_extra_data(self, k, v):
        self.db[k] = v

    def update(self, game):
        if game.expunge or \
                self.no_data:
            return

        for ns, tags in game.tags.items():
            for v in tags:
                tag = ns + ":" + v
                if tag not in self.db["rtag"]:
                    self.db["rtag"][tag] = []
                self.db["rtag"][tag].append(game.id)

        data = {}
        data["tr"] = {}
        data["name"] = game.name
        data["brief"] = game.description.brief_html
        data["thumbnail"] = game.thumbnail.dict()
        data["mtime"] = game.mtime

        for lang in game.tr:
            data["tr"][lang] = {}
            if game.tr[lang].name:
                data["tr"][lang]["name"] = game.tr[lang].name
            if game.tr[lang].description:
                data["tr"][lang]["brief"] = game.tr[lang].description.brief_html

        self.db["data"][game.id] = data

    def write_to_file(self, output):
        if not self.no_data:
            data = json.dumps(self.db, separators=(',', ':'))

            with open(os.path.join(output, "scripts", "searchdb.json"), "w") as f:
                f.write(data)

            if self.fctx.args.file_uri_workaround:
                with open(os.path.join(output, "scripts", "searchdb_offline.js"), "w") as f:
                    f.write("var _searchdb=JSON.parse(atob('")
                    f.write(base64.b64encode(data.encode('utf-8')).decode('ascii'))
                    f.write("'))")
