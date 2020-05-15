
# -*- coding: utf-8 -*-

import os
from utils.i18n import get

context = {
    "lang": "en",
    "active_languages": "actived",
    "get": get
}

def render(games, env, language, language_ui, output):
    context["ui"] = language_ui
    with open(os.path.join(output, "languages.html"), "w") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("languages.html").render(context))
        f.write(env.get_template("footer.html").render(context))
