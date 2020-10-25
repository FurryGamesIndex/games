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
import json
from fgi import image
from fgi.i18n import get
from fgi.seo.sitemap import openw_with_sm

context = {
    "rr": "..",
    "active_list": "actived",
    "uri_to_html_image": image.uri_to_html_image,
    "get": get
}

def render(games, env, lctx, output):
    context.update(lctx)
    language = lctx["lang"]

    context["games"] = games
    with openw_with_sm(output, os.path.join(language, "list.html"), priority="0.6") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("list.html").render(context))
        f.write(env.get_template("footer.html").render(context))
