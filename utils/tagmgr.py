# -*- coding: utf-8 -*-

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
