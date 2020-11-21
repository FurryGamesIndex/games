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
from fgi.i18n import conv_doc_markdown

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

    context["content"] = conv_doc_markdown("faq", language)
    context["active_faq"] = "actived"
    with openw_with_sm(output, os.path.join(language, "faq.html"), priority="0.4") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("simple_md.html").render(context))
        f.write(env.get_template("footer.html").render(context))
    del context["active_faq"]
    del context["content"]

    context["content"] = conv_doc_markdown("search_help", language)
    context["extra_styles"] = context["content"].metadata["styles"]
    with openw_with_sm(output, os.path.join(language, "search_help.html"), priority="0.5") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("simple_md.html").render(context))
        f.write(env.get_template("footer.html").render(context))
    del context["extra_styles"]
    del context["content"]

    with openw_with_sm(output, os.path.join(language, "sensitive.html"), priority="0.2",
            lastmod_file="templates/sensitive.html") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("sensitive.html").render(context))
        f.write(env.get_template("footer.html").render(context))
