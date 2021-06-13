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
import re
from html import escape

from fgi.base import make_wrapper
from fgi.renderer import Renderer
from fgi.seo import keywords

class RendererGame(Renderer):
    def __init__(self, *args, **kwargs):
        self.basectx = {
            "rr": "../..",
        }

        super().__init__(*args, **kwargs)

        self.games = self.lctx["games"]
        self.authors = self.lctx["authors"]
        self.author_game_map = self.lctx["author_game_map"]
        self.context = self.new_context()

    def new_game_context(self):
        return self.context.copy()

    def author_widget(self, game):
        gid = game.id
        data = {}
        ga = {}

        for author in game.authors:
            aname = author.name
            if aname in self.author_game_map:
                for g in self.author_game_map[aname]:
                    i = g.id
                    if i != gid:
                        if i not in ga:
                            ga[i] = set()
                        ga[i].add(aname)

        for gid, au in ga.items():
            authornames = ", ".join(sorted(au))
            if authornames not in data:
                data[authornames] = []
            data[authornames].append(self.games[gid])

        return data

    def render_game(self, gid, game):
        print("  => %s" % gid)
        context = self.new_game_context()

        context["game"] = game
        context["name"] = gid
        context["author_widget"] = self.author_widget(game)

        if game.expunge:
            context["noindex"] = True

        meta = dict()
        meta["title"] = game.get_name(self.language)
        meta["description"] = escape(game.get_description(self.language).brief_sl)
        meta["image"] = game.thumbnail.with_rr(context["rr"]).src
        meta["extra_keywords"] = keywords.game_page_extra_keywords(game, context["ui"])
        context["meta"] = meta

        return self.env.get_template("game.html").render(context)

    def render(self):
        for gid, game in self.games.items():
            with self.sm_openw("games", gid + ".html", sm = not game.expunge,
                    priority="0.7", lastmod_ts=game.get_mtime(self.language)) as f:
                f.write(self.render_game(gid, game))

impl = RendererGame
