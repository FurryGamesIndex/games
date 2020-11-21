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

from fgi.i18n import get_languages_list
from fgi import tagmgr

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

def sorted_games(games):
    return dict(sorted(games.items(), key=lambda t: t[0].replace("_", "").upper()))

def sorted_games_by_mtime(games):
    return dict(sorted(games.items(), key=lambda t: t[1]["mtime"], reverse=True))

def strip_games_expunge(games):
    return { k: v for k, v in games.items() if "expunge" not in v }

def load_game_all(dbdir, sdb):
    games = {}
    languages = get_languages_list(dbdir)

    for f in os.listdir(dbdir):
        game, game_id = load_game(dbdir, f, languages)

        if game is None:
            continue

        games[game_id] = game

    games = sorted_games(games)

    for game_id, game in games.items():
        tagmgr.check_and_patch(game)
        sdb.update(game)

    return games
