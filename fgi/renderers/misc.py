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
from datetime import datetime
from markdown2 import Markdown
from fgi.seo.sitemap import openw_with_sm

context= {
    "rr": "..",
}

def render(games, env, lctx, output):
    context.update(lctx)
    language = lctx["lang"]

    context["datetime"] = datetime

    markdowner = Markdown()

    context["active_search"] = "actived"
    context["noindex"] = True
    with open(os.path.join(output, language, "search.html"), "w") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("search.html").render(context))
        f.write(env.get_template("footer.html").render(context))
    del context["active_search"]
    del context["noindex"]

    context["active_index"] = "actived"
    with openw_with_sm(output, os.path.join(language, "index.html"), priority="0.6") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("index.html").render(context))
        f.write(env.get_template("footer.html").render(context))
    del context["active_index"]

    faq_source = "doc/faq." + language + ".md"
    if not os.path.exists(faq_source):
        faq_source = "doc/faq.en.md"
    with open(faq_source) as f:
        context["content"] = markdowner.convert(f.read())
    context["active_faq"] = "actived"
    with openw_with_sm(output, os.path.join(language, "faq.html"), priority="0.4",
            lastmod_file="doc/faq." + language + ".md") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("simple_md.html").render(context))
        f.write(env.get_template("footer.html").render(context))
    del context["active_faq"]
    del context["content"]

    with openw_with_sm(output, os.path.join(language, "sensitive.html"), priority="0.2",
            lastmod_file="templates/sensitive.html") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("sensitive.html").render(context))
        f.write(env.get_template("footer.html").render(context))
