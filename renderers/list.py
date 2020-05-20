# -*- coding: utf-8 -*-

import os
import json
from utils.image_uri import image_uri
from utils.i18n import get

context = {
    "rr": "..",
    "active_list": "actived",
    "image_uri": image_uri,
    "get": get
}

def render(games, env, language, language_ui, output):
    context["lang"] = language
    context["ui"] = language_ui
    context["games"] = games
    with open(os.path.join(output, "list.html"), "w") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("list.html").render(context))
        f.write(env.get_template("footer.html").render(context))

    glist = {}
    for id, data in games.items():
        desc = get(data, language, "description")
        desc = (desc[:480] + (desc[480:] and '...'))
        glist[id] = {}
        glist[id]["name"] = get(data, language, "name")
        glist[id]["description"] = desc
        glist[id]["thumbnail"] = image_uri("..", data["thumbnail"], id)
    with open(os.path.join(output, "gamelist.json"), "w") as f:
        f.write(json.dumps(glist))
