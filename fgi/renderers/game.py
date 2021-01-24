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
from fgi.base import make_wrapper
from fgi.renderer import Renderer
from fgi.i18n import get, get_mtime
from fgi.link import link_info
from fgi.seo import keywords

def checktag(game, namespace, value):
    return value in game["tags"].get(namespace, {})

platform_icons = {
    "web": '<i title="Web" class="fab fa-safari fa-fw"></i>',
    "windows": '<i title="Microsoft Windows" class="fab fa-windows fa-fw"></i>',
    "macos": '<i title="Apple macOS" class="fab fa-apple fa-fw"></i>',
    "linux": '<i title="GNU/Linux" class="fab fa-linux fa-fw"></i>',
    "android": '<i title="Android" class="fab fa-android fa-fw"></i>',
    "ios": '<i title="Apple iOS" class="fab fa-app-store-ios fa-fw"></i>',
    "playstation": '<i title="Playstation" class="fab fa-playstation fa-fw"></i>',
    "playstation2": '<i title="Playstation 2" class="fab fa-playstation fa-fw"></i>',
    "playstation3": '<i title="Playstation 3" class="fab fa-playstation fa-fw"></i>',
    "playstation4": '<i title="Playstation 4" class="fab fa-playstation fa-fw"></i>',
    "psv": '<i title="Playstation Vita" class="fab fa-playstation fa-fw"></i>',
    "psp": '<i title="Playstation Portable" class="fab fa-playstation fa-fw"></i>',
    "xbox": '<i title="Xbox" class="fab fa-xbox fa-fw"></i>',
    "xbox-one": '<i title="Xbox One" class="fab fa-xbox fa-fw"></i>',
    "xbox-360": '<i title="Xbox 360" class="fab fa-xbox fa-fw"></i>',
}

class RendererGame(Renderer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.basectx = {
            "rr": "../..",
            "get": get,
            "link_info": make_wrapper(link_info, self.fctx),
            "checktag": checktag,
            "platform_icons": platform_icons
        }

        self.games = self.lctx["games"]
        self.authors = self.lctx["authors"]
        self.context = self.new_context()

        lang_without_region = self.language
        if '-' in lang_without_region:
            lang_without_region = lang_without_region.split('-')[0]

        self.context["lang_without_region"] = lang_without_region

    def new_game_context(self):
        return self.context.copy()

    def author_widget(self, game):
        name = game["id"]
        data = {}
        ga = {}

        for author in game["authors"]:
            aname = author["name"]
            if aname in self.authors:
                tmp = self.authors[aname]["games"]

                for g in tmp:
                    i = g["id"]
                    if i != name:
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

        if 'expunge' in game:
            context["noindex"] = True

        meta = dict()
        meta["title"] = get(game, self.language, 'name')
        desc = get(game, self.language, 'description')[:200].replace('\n', '') + "..."
        meta["description"] = re.sub(r'<[^<]*>', '', desc)
        meta["image"] = game["hi_thumbnail"].with_rr(context["rr"]).src
        meta["extra_keywords"] = keywords.game_page_extra_keywords(game, context["ui"])
        context["meta"] = meta

        if 'replaced-by' in game:
            rbgame = self.games[game['replaced-by']]
            context["rbgame"] = rbgame

        return self.env.get_template("game.html").render(context)

    def render(self):
        for gid, game in self.games.items():
            nosm = 'expunge' in game

            with self.sm_openw("games", gid + ".html", sm = not nosm,
                    priority="0.7", lastmod_ts=get_mtime(game, self.language)) as f:
                f.write(self.render_game(gid, game))

impl = RendererGame
