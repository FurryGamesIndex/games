# -*- coding: utf-8 -*-

import os
import re
from utils import image
from utils.i18n import get
from utils.i18n import get_desc
from utils.link import link_info
from utils.sitemap import openw_with_sm

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
    "psv": '<i title="psv" class="fab fa-playstation fa-fw"></i>',
    "psp": '<i title="psp" class="fab fa-playstation fa-fw"></i>',
    "xbox": '<i title="xbox" class="fab fa-xbox fa-fw"></i>',
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

    for name, game in games.items():
        context["game"] = game
        context["name"] = name
        print("  => %s" % name)

        meta["title"] = get(game, language, 'name')
        desc = get(game, language, 'description')[:200].replace('\n', '') + "..."
        meta["description"] = re.sub(r'<[^<]*>', '', desc)
        meta["image"] = image.uri(context["rr"], game["thumbnail"], name)

        with openw_with_sm(output, os.path.join(language, "games", name + ".html"),
                priority="0.7", lastmod_file=os.path.join("games", name + ".yaml")) as f:
            f.write(env.get_template("header.html").render(context))
            f.write(env.get_template("game.html").render(context))
            f.write(env.get_template("footer.html").render(context))
