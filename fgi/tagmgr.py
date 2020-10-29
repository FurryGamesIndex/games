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

import sys

tagdep = {}
tags = {}
tagalias = {}

def closure(ns, s):
    r = s.copy()

    for i in s:
        if i in tagdep[ns]:
            r = r.union(closure(ns, tagdep[ns][i]))

    return r

def loaddep(data):
    global tagdep

    tagdep = { k: { kk: set(vv) for kk, vv in v.items() } for k, v in data.items() if k[0] != '_' }

    for ns, v in tagdep.items():
        for value, s in v.items():
            tagdep[ns][value] = closure(ns, s)

def load(data):
    global tags
    global tagalias

    tmp = { k: v for k, v in data.items() if k[0] != '@' }

    for k, v in tmp.items():
        for ns in v["namespaces"]:
            if ns not in tags:
                tags[ns] = {}
                tags[ns]["@cur_index"] = 1
            tags[ns][k] = tags[ns]["@cur_index"] + 6000
            tags[ns]["@cur_index"] += 1

        if "alias" in v:
            for i in v["alias"]:
                tagalias[i] = k

    for ns in tags:
        del tags[ns]["@cur_index"]

needed_ns = ["type", "author", "lang", "platform"]

def check_and_patch(game):
    for i in needed_ns:
        if i not in game["tags"]:
            print("[warning] missing %s namespace for game '%s'" % (i, game["id"]))

    for ns, v in game["tags"].items():
        if ns != "author":
            for i in v:
                if i not in tags[ns]:
                    print("""Error: The tag '%s:%s' is not standardized.
Is it a spelling mistake? If you wish to add tags, please edit the tags.yaml file.""" % (ns, i))
                    sys.exit(1)

        if ns in tagdep:
            tmp = set(v)
            for i in v:
                if i in tagdep[ns]:
                    tmp = tmp.union(tagdep[ns][i])
            game["tags"][ns] = list(tmp)

        if ns != "author":
            game["tags"][ns] = sorted(game["tags"][ns], key=lambda i: tags[ns][i])

