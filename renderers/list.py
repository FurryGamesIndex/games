# -*- coding: utf-8 -*-

import os
import json
from utils import image
from utils.i18n import get
from utils.sitemap import openw_with_sm

context = {
    "rr": "..",
    "active_list": "actived",
    "image_uri": image.uri,
    "get": get
}

def render(games, env, language, language_ui, output):
    context["lang"] = language
    context["ui"] = language_ui
    context["games"] = games
    with openw_with_sm(output, os.path.join(language, "list.html"), priority="0.6") as f:
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
        glist[id]["thumbnail"] = image.uri("..", data["thumbnail"], id)
    with open(os.path.join(output, language, "gamelist.json"), "w") as f:
        f.write(json.dumps(glist))
