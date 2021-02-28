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
from fgi.base import make_wrapper
from fgi.renderer import Renderer
from fgi.seo import keywords

class RendererAuthor(Renderer):
    def __init__(self, *args, **kwargs):
        self.basectx = {
            "rr": "../..",
        }

        super().__init__(*args, **kwargs)

        self.authors = self.lctx["authors"]

    def new_author_context(self):
        return self.context.copy()

    def render_author(self, author):
        print("  => %s" % author.name)

        context = self.new_context()
        context["author"] = author

        return self.env.get_template("author.html").render(context)

    def render(self):
        os.mkdir(self.getpath("authors"))

        for _, author in self.authors.items():
            with self.sm_openw("authors", author.id + ".html", priority="0.7") as f:
                f.write(self.render_author(author))

impl = RendererAuthor
