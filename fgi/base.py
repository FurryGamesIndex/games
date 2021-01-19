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
from html import escape
from bs4 import BeautifulSoup
from markdown2 import Markdown

def parse_description(game, fmt, game_id, mfac):
    if "description" not in game:
        return

    desc = game["description"]

    if fmt == "plain":
        game["@desc_html"] = escape(desc).replace("\n", "<br>")
    elif fmt == "markdown":
        markdowner = Markdown(extras=["strike", "target-blank-links"],
                inline_image_uri_filter = lambda uri: mfac.uri_to_html_image(uri, game_id).with_rr("../..").src)
        game["@desc_html"] = markdowner.convert(desc)
        game["description"] = BeautifulSoup(game["@desc_html"], features="html.parser").get_text()
    else:
        raise ValueError(f"description format invaild: {fmt}")

def cook_game(game, tagmgr, mfac):
    if "authors" in game:
        # If Using new generation format authors property,
        # the #/tags/author will be overrided unconditionally
        tmp = { "author": list() }
        tmp.update(game["tags"])
        game["tags"] = tmp
        for i in game["authors"]:
            game["tags"]["author"].append(i["name"])
    else:
        # For games using legecy format or without author infomation,
        # create a STUB authors property
        game["authors"] = list()
        for i in game["tags"].get("author", {}):
            tmp = dict()
            tmp["name"] = i
            tmp["@stub"] = True
            game["authors"].append(tmp)

    tagmgr.check_and_patch(game)

    if "description-format" not in game:
        game["description-format"] = "plain"

    parse_description(game, game["description-format"], game["id"], mfac)

    for ln, game_l10n in game["tr"].items():
        parse_description(game_l10n, game["description-format"], game["id"], mfac)

    if "thumbnail" in game:
        game["hi_thumbnail"] = mfac.uri_to_html_image(game["thumbnail"], game["id"])

    game["media"] = list()
    for i in game["screenshots"]:
        game["media"].append(mfac.create_media(i, game["id"]))

def load_game(dbdir, f, languages):
    game = None
    fn = os.path.join(dbdir, f)

    if (not os.path.isfile(fn)) or (f[0] == '.'):
        return (None, None)

    game_id = os.path.splitext(f)[0]

    print("Loading %s" % fn)
    with open(fn) as stream:
        game = yaml.safe_load(stream)
        game["id"] = game_id
        game["tr"] = {}
        game["mtime"] = os.path.getmtime(fn)

    for language in languages:
        l10n_file = os.path.join(dbdir, "l10n", language, f)
        if os.path.isfile(l10n_file):
            print("Loading %s" % l10n_file)
            with open(l10n_file) as stream:
                game["tr"][language] = yaml.safe_load(stream)
                game["tr"][language]["mtime"] = os.path.getmtime(l10n_file)

    return (game, game_id)

def sorted_games_name(games):
    return sorted(games, key=lambda t: t.replace("_", "").upper())

def sorted_games(games):
    return dict(sorted(games.items(), key=lambda t: t[0].replace("_", "").upper()))

def sorted_games_by_mtime(games):
    return dict(sorted(games.items(), key=lambda t: t[1]["mtime"], reverse=True))

def strip_games_expunge(games):
    return { k: v for k, v in games.items() if "expunge" not in v }

def load_game_all(dbdir, sdb, tagmgr, languages, mfac, authors):
    games = {}

    for f in sorted_games_name(os.listdir(dbdir)):
        game, game_id = load_game(dbdir, f, languages)

        if game is None:
            continue

        cook_game(game, tagmgr, mfac)

        games[game_id] = game

        for i in game["authors"]:
            name = i["name"]
            if name in authors:
                authors[name]["games"].append(game)

        sdb.update(game)

    return games

def load_author(dbdir, f, mfac):
    fn = os.path.join(dbdir, f)

    if (not os.path.isfile(fn)) or (f[0] == '.'):
        return None

    author_id = os.path.splitext(f)[0]

    print("Loading %s" % fn)
    with open(fn) as stream:
        author = yaml.safe_load(stream)
        author["id"] = author_id
        author["games"] = list()

    if "avatar" in author:
        author["hi_avatar"] = mfac.uri_to_html_image(author["avatar"], "_avatar")

    return author

def load_author_all(dbdir, mfac):
    authors = dict()

    for f in os.listdir(dbdir):
        author = load_author(dbdir, f, mfac)

        if author is None:
            continue

        authors[author["name"]] = author

    return authors

def list_pymod(dirname):
    package_path = os.path.dirname(__file__)
    return [os.path.splitext(f)[0] \
        for f in os.listdir(os.path.join(package_path, dirname)) \
            if os.path.isfile(os.path.join(package_path, dirname, f)) \
                and f[0] != '.' and f != "__init__.py"]

def local_res_href(pmgr, rr, path, hc_uquery = None):
    query = ""
    if hc_uquery:
        query = f"?hc=uquery&t={hc_uquery}"

    mod = pmgr.invoke_plugins("html_local_res_href", None, rr=rr, path=path, hc_uquery=hc_uquery)

    if mod:
        mod_value = mod["new_uri"]
        if "query_mode" in mod:
            if mod["query_mode"] == "unmanaged":
                mod_value = mod_value + query
            elif mod["query_mode"] == "origin-first":
                if query != "":
                    mod_value = mod_value + query
                else:
                    mod_value = mod_value + mod["query_fb"]
            elif mod["query_mode"] == "managed":
                pass
            else:
                raise ValueError(f"unkown query_mode: {mode['query_mode']}")
        return mod_value
    else:
        return rr + path + query

def make_wrapper(func, arg):
    def new_func(*args, **kwargs):
        return func(arg, *args, **kwargs)
    return new_func
