# -*- coding: utf-8 -*-

import os
from markdown2 import Markdown

context = {
    "active_index": "actived"
}

def render(games, env, language, language_ui, output):
    context["lang"] = language
    context["ui"] = language_ui

    markdowner = Markdown()
    with open("README." + language + ".md") as f:
        context["index_content"] = markdowner.convert(f.read())

    with open(os.path.join(output, "index.html"), "w") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("index.html").render(context))
        f.write(env.get_template("footer.html").render(context))
