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
from fgi.renderer import Renderer
from fgi.i18n import conv_doc_markdown

class RendererSingles(Renderer):
    def __init__(self, *args, **kwargs):
        self.basectx = {
            "rr": ".",
        }

        super().__init__(*args, **kwargs, nonl10n=True)

    def render(self):
        context = self.new_context()
        context["active_languages"] = "activated"
        with open(self.getpath("languages.html"), "w") as f:
            f.write(self.env.get_template("languages.html").render(context))

        context = self.new_context()
        context["content"] = conv_doc_markdown(self.fctx, "privacy-policy", None)
        with open(self.getpath("privacy-policy.html"), "w") as f:
            f.write(self.env.get_template("simple_md.html").render(context))

        context = self.new_context()
        context["content"] = conv_doc_markdown(self.fctx, "credits", None)
        with self.sm_openw("credits.html") as f:
            f.write(self.env.get_template("simple_md.html").render(context))

        context = self.new_context()
        context["rr"] = ""
        with self.sm_openw("404.html") as f:
            f.write(self.env.get_template("404.html").render(context))

impl = RendererSingles
