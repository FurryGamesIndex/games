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
import re
from datetime import datetime
from fgi.renderer import Renderer
from fgi.i18n import conv_doc_markdown

class RendererMisc(Renderer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.basectx = {
            "rr": "..",
            "datetime": datetime,
        }

    def render(self):
        env = self.env

        # search.html

        context = self.new_context()
        context["active_search"] = "actived"
        context["noindex"] = True
        with open(self.getpath("search.html"), "w") as f:
            f.write(env.get_template("search.html").render(context))

        # index.html

        context = self.new_context()
        context["active_index"] = "actived"
        with self.sm_openw("index.html", priority="0.6") as f:
            f.write(env.get_template("index.html").render(context))

        # faq.html

        context = self.new_context()
        context["content"] = conv_doc_markdown("faq", self.language)
        context["active_faq"] = "actived"
        with self.sm_openw("faq.html", priority="0.4") as f:
            f.write(env.get_template("simple_md.html").render(context))

        # search_help.html

        def _add_search_icon_link(m):
            c = m.group(1)
            if not c.endswith(":"):
                return f"`{c}` <a target='_blank' href='search.html?tagx?{c}'><i class='fas fa-search fa-fw'></i></a>"
            else:
                return f"`{c[:-1]}`"

        context = self.new_context()
        context["content"] = conv_doc_markdown("search_help", self.language,
            callback=lambda c: re.sub(r'`(.*?)`', _add_search_icon_link, c))
        context["extra_styles"] = context["content"].metadata["styles"]

        with self.sm_openw("search_help.html", priority="0.5") as f:
            f.write(env.get_template("simple_md.html").render(context))

        # sensitive.html

        context = self.new_context()
        with self.sm_openw("sensitive.html", priority="0.2",
                lastmod_file="templates/sensitive.html") as f:
            f.write(env.get_template("sensitive.html").render(context))

impl = RendererMisc
