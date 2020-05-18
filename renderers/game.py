# -*- coding: utf-8 -*-

import os
from utils.image_uri import image_uri
from utils.i18n import get
from utils.i18n import get_desc
from utils.link import link_info

def checktag(game, namespace, value):
    return value in game["tags"].get(namespace, {})

context = {
    "rr": "../..",
    "image_uri": image_uri,
    "get": get,
    "get_desc": get_desc,
    "link_info": link_info,
    "checktag": checktag,
}

def render(games, env, language, language_ui, output):
    context["lang"] = language
    context["ui"] = language_ui
    for name, game in games.items():
        context["game"] = game
        context["name"] = name
        print("  => %s" % name)
        with open(os.path.join(output, "games", name + ".html"), "w") as f:
            f.write(env.get_template("header.html").render(context))
            f.write(env.get_template("game.html").render(context))
            f.write(env.get_template("footer.html").render(context))
