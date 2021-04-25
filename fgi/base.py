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

from fgi.game import Game
from fgi.author import Author
from fgi.utils.uriutils import append_query

def load_game(dbdir, f, languages):
    game = None
    fn = os.path.join(dbdir, f)

    if (not os.path.isfile(fn)) or (f[0] == '.'):
        return None

    game_id = os.path.splitext(f)[0]

    print("Loading %s" % fn)
    with open(fn) as stream:
        game = Game(yaml.safe_load(stream), game_id, os.path.getmtime(fn))

    for language in languages:
        l10n_file = os.path.join(dbdir, "l10n", language, f)
        if os.path.isfile(l10n_file):
            print("Loading %s" % l10n_file)
            with open(l10n_file) as stream:
                game.add_l10n_data(language, yaml.safe_load(stream), os.path.getmtime(l10n_file))

    return game

def sorted_games_name(games):
    return sorted(games, key=lambda t: t.replace("_", "").upper())

def sorted_games(games):
    return dict(sorted(games.items(), key=lambda t: t[0].replace("_", "").upper()))

def sorted_games_by_mtime(games):
    return dict(sorted(games.items(), key=lambda t: t[1].mtime, reverse=True))

def strip_games_expunge(games):
    return { k: v for k, v in games.items() if not v.expunge }

def load_game_all(dbdir, sdb, tagmgr, languages, mfac, ifac, authors, author_game_map):
    games = {}

    for f in sorted_games_name(os.listdir(dbdir)):
        game = load_game(dbdir, f, languages)

        if game:
            game.realize(tagmgr, mfac, ifac, authors)
            games[game.id] = game

            for i in game.authors:
                if not i.standalone:
                    if i.name not in author_game_map:
                        author_game_map[i.name] = list()
                    author_game_map[i.name].append(game)

            sdb.update(game)

    for _, game in games.items():
        game.link(games)

    return games

def load_author(dbdir, f):
    fn = os.path.join(dbdir, f)

    if (not os.path.isfile(fn)) or (f[0] == '.'):
        return None

    author_id = os.path.splitext(f)[0]

    print("Loading %s" % fn)
    with open(fn) as stream:
        author = Author(yaml.safe_load(stream), author_id)

    return author

def load_author_all(dbdir, mfac, ifac, author_game_map):
    authors = dict()

    for f in os.listdir(dbdir):
        author = load_author(dbdir, f)

        if author:
            author.realize(mfac, ifac, author_game_map)
            authors[author.name] = author

    return authors

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
