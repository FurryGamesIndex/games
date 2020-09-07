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
from utils import image
from utils.i18n import get
from utils.i18n import get_desc
from utils.link import link_info
from utils.seo.sitemap import openw_with_sm

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

context = {
    "rr": "../..",
    "image": image,
    "get": get,
    "get_desc": get_desc,
    "link_info": link_info,
    "checktag": checktag,
    "platform_icons": platform_icons
}

def render(games, env, language, language_ui, output):
    context["lang"] = language
    context["ui"] = language_ui
    meta = {}
    context["meta"] = meta

    lang_without_region = language
    if '-' in lang_without_region:
        lang_without_region = lang_without_region.split('-')[0]

    context["lang_without_region"] = lang_without_region

    for name, game in games.items():
        context["game"] = game
        context["name"] = name
        print("  => %s" % name)

        if 'expunge' in game:
            context["noindex"] = True

        meta["title"] = get(game, language, 'name')
        desc = get(game, language, 'description')[:200].replace('\n', '') + "..."
        meta["description"] = re.sub(r'<[^<]*>', '', desc)
        meta["image"] = image.uri(context["rr"], game["thumbnail"], name)

        # TODO: Refactor this code
        if 'expunge' in game:
            with open(os.path.join(output, language, "games", name + ".html"), "w") as f:
                f.write(env.get_template("header.html").render(context))
                f.write(env.get_template("game.html").render(context))
                f.write(env.get_template("footer.html").render(context))
        else:
            with openw_with_sm(output, os.path.join(language, "games", name + ".html"),
                    priority="0.7", lastmod_file=os.path.join("games", name + ".yaml")) as f:
                f.write(env.get_template("header.html").render(context))
                f.write(env.get_template("game.html").render(context))
                f.write(env.get_template("footer.html").render(context))

        if "noindex" in context:
            del context["noindex"]
