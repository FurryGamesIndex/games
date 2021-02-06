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

from fgi.link import uri_to_src

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

def cook_game_add_auto_medias(game, mfac):
    # FIXME: link search should be done in link.py after classfied it
    if "links" in game and game.get("auto-steam-widget", True):
        for i in game["links"]:
            if i["name"] == ".steam":
                if i["uri"].startswith("steam:"):
                    swid = i["uri"].split(':', 1)[1]
                    game["media"].append(mfac.create_media({
                        "type": "steam-widget",
                        "id": swid,
                    }, game["id"]))
                else:
                    print("[warning] steam widget can not be added while not using the steam: URI.")

def cook_game(game, tagmgr, mfac):
    gameid = game["id"]

    if "authors" in game:
        if "author" in game["tags"]:
            raise ValueError("authors property conflict #/tags/author namespace")

        tmp = { "author": list() }
        tmp.update(game["tags"])
        game["tags"] = tmp
        for i in game["authors"]:
            if "standalone" not in i:
                i["standalone"] = False
            if i["standalone"]:
                if "avatar" in i:
                    i["hi_avatar"] = mfac.uri_to_html_image(i["avatar"], gameid)
                if "link-uri" in i:
                    i["link_href"] = uri_to_src(i["link-uri"])
            else:
                game["tags"]["author"].append(i["name"])

    else:
        # For games using legecy format or without author infomation,
        # create a STUB authors property
        game["authors"] = list()
        for i in game["tags"].get("author", {}):
            tmp = dict()
            tmp["name"] = i
            tmp["@stub"] = True
            tmp["standalone"] = False
            game["authors"].append(tmp)

    tagmgr.check_and_patch(game)

    if "description-format" not in game:
        game["description-format"] = "plain"

    parse_description(game, game["description-format"], gameid, mfac)

    for ln, game_l10n in game["tr"].items():
        parse_description(game_l10n, game["description-format"], gameid, mfac)

    if "thumbnail" in game:
        game["hi_thumbnail"] = mfac.uri_to_html_image(game["thumbnail"], gameid)

    if "sensitive_media" in game:
        print(f"[warning] game '{gameid}' is using deprecated property 'sensitive_media'. This property will be ignored.")
        game["sensitive_media"] = False

    game["media"] = list()

    cook_game_add_auto_medias(game, mfac)

    for i in game["screenshots"]:
        game["media"].append(mfac.create_media(i, gameid))
        if type(i) is not str and \
                "sensitive" in i and \
                i["sensitive"] == True:
            game["sensitive_media"] = True

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
            if not i["standalone"]:
                name = i["name"]
                if name not in authors:
                    authors[name] = dict()
                    authors[name]["@stub"] = True
                    authors[name]["games"] = list()

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
