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

from fgi.i18n import get_languages_list
from fgi.plugin import invoke_plugins


def parse_description(game, fmt, game_id, mfac):
    if "description" not in game:
        return

    desc = game["description"]

    if fmt == "plain":
        game["@desc_html"] = escape(desc).replace("\n", "<br>")
    elif fmt == "markdown":
        markdowner = Markdown(extras=["strike", "target-blank-links"],
                inline_image_uri_filter = lambda uri: mfac.uri_to_html_image("../..", uri, game_id).src)
        game["@desc_html"] = markdowner.convert(desc)
        game["description"] = BeautifulSoup(game["@desc_html"], features="html.parser").get_text()
    else:
        raise ValueError(f"description format invaild: {fmt}")

def load_game(dbdir, f, languages, mfac):
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

        if "description-format" not in game:
            game["description-format"] = "plain"

        parse_description(game, game["description-format"], game_id, mfac)

    for language in languages:
        l10n_file = os.path.join(dbdir, "l10n", language, f)
        if os.path.isfile(l10n_file):
            print("Loading %s" % l10n_file)
            with open(l10n_file) as stream:
                game["tr"][language] = yaml.safe_load(stream)
                game["tr"][language]["mtime"] = os.path.getmtime(l10n_file)
                parse_description(game["tr"][language], game["description-format"], game_id, mfac)

    return (game, game_id)

def sorted_games(games):
    return dict(sorted(games.items(), key=lambda t: t[0].replace("_", "").upper()))

def sorted_games_by_mtime(games):
    return dict(sorted(games.items(), key=lambda t: t[1]["mtime"], reverse=True))

def strip_games_expunge(games):
    return { k: v for k, v in games.items() if "expunge" not in v }

def load_game_all(dbdir, sdb, tagmgr, languages, mfac):
    games = {}

    for f in os.listdir(dbdir):
        game, game_id = load_game(dbdir, f, languages, mfac)

        if game is None:
            continue

        games[game_id] = game

        tagmgr.check_and_patch(game)
        sdb.update(game)

    games = sorted_games(games)
    return games

def list_pymod(dirname):
    package_path = os.path.dirname(__file__)
    return [os.path.splitext(f)[0] \
        for f in os.listdir(os.path.join(package_path, dirname)) \
            if os.path.isfile(os.path.join(package_path, dirname, f)) \
                and f[0] != '.' and f != "__init__.py"]

def local_res_href(rr, path, hc_uquery = None):
    query = ""
    if hc_uquery:
        query = f"?hc=uquery&t={hc_uquery}"

    mod = invoke_plugins("html_local_res_href", None, rr=rr, path=path, hc_uquery=hc_uquery)

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


