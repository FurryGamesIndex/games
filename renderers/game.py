# -*- coding: utf-8 -*-

import os
import re
from utils import image
from utils.i18n import get
from utils.i18n import get_desc
from utils.link import link_info

def checktag(game, namespace, value):
    return value in game["tags"].get(namespace, {})

context = {
    "rr": "../..",
    "image": image,
    "get": get,
    "get_desc": get_desc,
    "link_info": link_info,
    "checktag": checktag,
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

        with open(os.path.join(output, "games", name + ".html"), "w") as f:
            f.write(env.get_template("header.html").render(context))
            f.write(env.get_template("game.html").render(context))
            f.write(env.get_template("footer.html").render(context))
