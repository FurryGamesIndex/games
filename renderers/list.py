# -*- coding: utf-8 -*-

import os
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
