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

tagdep = {}

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

def patch(game):
    for ns, v in game["tags"].items():
        if ns in tagdep:
            tmp = set(v)
            for i in v:
                if i in tagdep[ns]:
                    tmp = tmp.union(tagdep[ns][i])
            game["tags"][ns] = list(sorted(tmp))
