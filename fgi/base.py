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
import yaml

from fgi.utils.uriutils import append_query


def sorted_games_name(games):
    return sorted(games, key=lambda t: t.replace("_", "").upper())

def sorted_games(games):
    return dict(sorted(games.items(), key=lambda t: t[0].replace("_", "").upper()))

def sorted_games_by_mtime(games):
    return dict(sorted(games.items(), key=lambda t: t[1].mtime, reverse=True))

def sorted_games_by_bmtime_g(games, use_btime, ln):
    if use_btime:
        yield from sorted(games, key=lambda t: t[1].btime, reverse=True)
    else:
        yield from sorted(games, key=lambda t: t[1].get_mtime(ln), reverse=True)

def strip_games_expunge_g(games):
    for k, v in games:
        if not v.expunge:
            yield k, v

def strip_games_expunge(games):
    return { k: v for k, v in games.items() if not v.expunge }

def list_pymod(dirname):
    package_path = os.path.dirname(__file__)
    return [os.path.splitext(f)[0] \
        for f in os.listdir(os.path.join(package_path, dirname)) \
            if os.path.isfile(os.path.join(package_path, dirname, f)) \
                and f[0] != '.' and f != "__init__.py"]

def find_local_file(dirlist, path):
    for i in dirlist:
        fn = os.path.join(i, *path)
        if os.path.exists(fn):
            return fn

    raise ValueError(f"Can not find file '{'/'.join(path)}' in {dirlist}")

def local_res_src(gctx, rr, path,
        force_hc_uquery = None,
        force_ignore_file_check = False):
    t = path[0]

    src = rr + "/" + "/".join(path)
    query = dict()
    hc_uquery = None

    if force_hc_uquery:
        hc_uquery = force_hc_uquery
    elif force_ignore_file_check:
        pass
    elif t == "styles":
        fn = "/".join(path[1:])
        ss = gctx.stylesheets.get(fn, None)
        if not ss:
            raise ValueError(f"Can not find stylesheet {fn}")
        hc_uquery = ss.mtime
    elif t == "icons":
        fn = find_local_file([gctx.icon_path], path[1:])
        hc_uquery = os.path.getmtime(fn)
    elif t == "scripts":
        fn = find_local_file(gctx.webroot_path, path)
        hc_uquery = os.path.getmtime(fn)

    if hc_uquery:
        query["hc"] = "uquery"
        query["t"] = str(int(hc_uquery))

    mod = gctx.pmgr.invoke_plugins("html_local_res_src", None, rr=rr, src=src, path=path, query=query)

    if mod:
        src = mod["src"]
        if "query_mode" in mod:
            if mod["query_mode"] == "unmanaged":
                pass
            elif mod["query_mode"] == "origin-first":
                if query == "":
                    query = mod["query"]
            elif mod["query_mode"] == "managed":
                query = mod["query"]
            else:
                raise ValueError(f"unkown query_mode: {mode['query_mode']}")

    src = append_query(src, query)
    return src

def make_wrapper(func, arg):
    def new_func(*args, **kwargs):
        return func(arg, *args, **kwargs)
    return new_func
