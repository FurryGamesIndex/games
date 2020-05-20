# -*- coding: utf-8 -*-

import os
from datetime import datetime
from markdown2 import Markdown

context= {
    "rr": "..",
}

def render(games, env, language, language_ui, output):
    context["lang"] = language
    context["ui"] = language_ui
    context["datetime"] = datetime

    markdowner = Markdown()
    with open("README." + language + ".md") as f:
        context["index_content"] = markdowner.convert(f.read())
    with open("doc/faq." + language + ".md") as f:
        context["faq_content"] = markdowner.convert(f.read())

    context["active_search"] = "actived"
    with open(os.path.join(output, "search.html"), "w") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("search.html").render(context))
        f.write(env.get_template("footer.html").render(context))
    del context["active_search"]

    context["active_index"] = "actived"
    with open(os.path.join(output, "index.html"), "w") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("index.html").render(context))
        f.write(env.get_template("footer.html").render(context))
    del context["active_index"]

    context["active_faq"] = "actived"
    with open(os.path.join(output, "faq.html"), "w") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("faq.html").render(context))
        f.write(env.get_template("footer.html").render(context))
    del context["active_faq"]
