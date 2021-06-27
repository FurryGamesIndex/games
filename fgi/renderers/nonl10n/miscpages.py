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
from markdown2 import Markdown

class RendererMiscPages(Renderer):
    def __init__(self, *args, **kwargs):
        self.basectx = {
            "rr": "..",
        }

        super().__init__(*args, **kwargs, nonl10n=True)

        self.markdowner = Markdown(extras=["tables"])

    def render(self):
        env = self.env

        os.mkdir(self.getpath("misc"))

        context = self.new_context()
        context["noindex"] = True

        for dirpath, dirnames, filenames in \
                os.walk(os.path.join(self.fctx.args.data_dir_prefix, "misc-pages")):
            for ofn in filenames:
                fn = os.path.splitext(ofn)[0]

                print(f"  => {dirpath} {fn}")

                with open(os.path.join(dirpath, ofn)) as of:
                    with open(self.getpath("misc", fn + ".html"), "w") as tf:
                        context["content"] = self.markdowner.convert(of.read())
                        tf.write(self.env.get_template("simple_md.html").render(context))

impl = RendererMiscPages
