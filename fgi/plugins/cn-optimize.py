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
import shutil
from fgi.plugin import Plugin

def remove_image_path_rr_parents(path):
    return re.sub(r'^[./]*', '', path)

class ChinaOptimizePlugin(Plugin):
    def __init__(self, options):
        print("""
ChinaOptimizePlugin loaded.

This plugin is aim to build a "china-optimized" verrsion FGI.

To make a best build. Please use the steam-cdn-unite plugin
and set cdn option to "china".

"china-optimized" version will use jsdelivr to serve images, and
webp format will be converted by standard FGI builds on Github.
So, we can STUB the webp converting but still add webp candition
to HTML picture as a source. Use webp-converter-stub plugin to
get faster building and lose nothing. :-)

Recommend build arguments:
    ./generate.py \\
        --no-sitemap \\
        --images-candidate-webp \\
        --plugin steam-cdn-unite,cdn=china \\
        --plugin cn-optimize \\
        --plugin webp-converter-stub
""")

        super().__init__(options)

    def post_build(self, _, *args, **kwargs):
        output = kwargs["output_path"]
        shutil.rmtree(os.path.join(output, "assets"))
        shutil.rmtree(os.path.join(output, "styles"))
        shutil.rmtree(os.path.join(output, "scripts"))
        shutil.rmtree(os.path.join(output, "webfonts"))
        shutil.rmtree(os.path.join(output, "en"))
        shutil.rmtree(os.path.join(output, "zh-tw"))
        with open(os.path.join(output, "CNAME"), "w") as f:
            f.write("cn.furrygames.top\n")
        with open(os.path.join(output, "robots.txt"), "w") as f:
            f.write("User-agent: *\n")
            f.write("Disallow: /\n")

    def html_local_res_href(self, mod, rr = None, path = None, hc_uquery = None, *args, **kwargs):
        if not mod:
            return "https://cdn.jsdelivr.net/gh/FurryGamesIndex/FurryGamesIndex.github.io" + path + "?"
        else:
            return mod

    def image_post_html_image_done(self, hi, *args, **kwargs):
        for i in hi.sources:
            img = i.srcset
            if not img.is_remote:
                suffix = remove_image_path_rr_parents(img.uri)
                if suffix.startswith("assets/"):
                    suffix += "?hc=always"
                img.uri = "https://cdn.jsdelivr.net/gh/FurryGamesIndex/FurryGamesIndex.github.io/" + suffix
                img.is_remote = True

impl = ChinaOptimizePlugin
