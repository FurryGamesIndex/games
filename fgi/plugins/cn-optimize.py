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
from urllib.parse import quote
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

        self.rev = "master"

        super().__init__(options)

    def i18n_post_ll_done(self, ll, *args, **kwargs):
        return ["zh-cn"]

    def post_build(self, _, *args, **kwargs):
        output = kwargs["output_path"]
        shutil.rmtree(os.path.join(output, "assets"))
        shutil.rmtree(os.path.join(output, "styles"))
        shutil.rmtree(os.path.join(output, "scripts"))
        shutil.rmtree(os.path.join(output, "webfonts"))
        with open(os.path.join(output, "CNAME"), "w") as f:
            f.write("cn.furrygames.top\n")
        with open(os.path.join(output, "robots.txt"), "w") as f:
            f.write("User-agent: *\n")
            f.write("Disallow: /\n")
            f.write("User-agent: Baiduspider\n")
            f.write("Allow: /\n")
        with open(os.path.join(output, "_redirects"), "w") as f:
            f.write("/en/*    https://furrygames.top/en/:splat    301\n")
            f.write("/zh-tw/*    https://furrygames.top/zh-tw/:splat    301\n")
        with open(os.path.join(output, "netlify.toml"), "w") as f:
            f.write("[build.processing]\n")
            f.write("  skip_processing = true\n")

    def html_local_res_href(self, mod, rr = None, path = None, hc_uquery = None, *args, **kwargs):
        if not mod:
            mod = dict()
            mod["new_uri"] = "https://cdn.jsdelivr.net/gh/FurryGamesIndex/FurryGamesIndex.github.io@" + self.rev + path
            mod["query_mode"] = "managed"

            query = ""
            if hc_uquery is not None:
                query = f"?hc=uquery&t={hc_uquery}&cors=1&uid=v1/" + quote(path, safe='')
            else:
                if path.startswith("styles/"):
                    query = "?hc=always&cors=1"
            mod["new_uri"] += query

        return mod

    def image_post_html_image_done(self, hi, *args, **kwargs):
        modified = False

        for i in hi.sources:
            img = i.srcset
            if not img.is_remote:
                suffix = remove_image_path_rr_parents(img.uri)
                img.uri = f"https://cdn.jsdelivr.net/gh/FurryGamesIndex/FurryGamesIndex.github.io@{self.rev}/{suffix}?uid=v1/{quote(suffix, safe='')}"
                img.is_remote = True
                modified = True

        if modified:
            hi.query["cors"] = "1"

impl = ChinaOptimizePlugin
