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
from itertools import islice

tagdep = {}
tags = {}
tagalias = {}
tagns = {}

def closure(_ns, s):
    r = s.copy()

    for i in s:
        ns = _ns
        prefix = ""
        if ":" in i:
            ns, i = i.split(":")
            prefix = ns + ":"
        if ns in tagdep and i in tagdep[ns]:
            tmp = tagdep[ns][i]
            tmp = set([i if ":" in i else prefix + i for i in tmp])
            r = r.union(closure(ns, tmp))

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
    global tagns

    tmp = { k: v for k, v in data.items() if k[0] != '@' }

    for k, v in tmp.items():
        for ns in v["namespaces"]:
            if ns not in tags:
                tags[ns] = {}
                tags[ns]["@cur_index"] = 1

            if "order" in v:
                tags[ns][k] = v["order"]
            else:
                tags[ns][k] = tags[ns]["@cur_index"] + 6000
                tags[ns]["@cur_index"] += 1

        if "alias" in v:
            for i in v["alias"]:
                tagalias[i] = k

        tagns[k] = v["namespaces"]

    for ns in tags:
        del tags[ns]["@cur_index"]

needed_ns = ["type", "author", "lang", "platform"]

def check_and_patch(game):
    for ns, v in game["tags"].items():
        if ns in tagdep:
            for i in islice(v, 0, len(v)):
                if i in tagdep[ns]:
                    for j in tagdep[ns][i]:
                        if ":" in j:
                            nns, j = j.split(":")
                            if nns not in game["tags"]:
                                game["tags"] = {}
                            game["tags"][nns].append(j)
                        else:
                            v.append(j)

    for i in needed_ns:
        if i not in game["tags"]:
            print("[warning] missing %s namespace for game '%s'" % (i, game["id"]))

    for ns in game["tags"]:
        if ns != "author":
            v = list(set(game["tags"][ns]))
            v = sorted(v, key=lambda i: tags[ns][i])
            game["tags"][ns] = v

            for i in v:
                if i not in tags[ns]:
                    print("""Error: The tag '%s:%s' is not standardized.
Is it a spelling mistake? If you wish to add tags, please edit the tags.yaml file.""" % (ns, i))
                    sys.exit(1)

