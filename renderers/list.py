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
from utils import image
from utils.i18n import get
from utils.seo.sitemap import openw_with_sm

from __main__ import args

context = {
    "rr": "..",
    "active_list": "actived",
    "uri_to_html_image": image.uri_to_html_image,
    "get": get
}

def render(games, env, language, language_ui, output):
    context["lang"] = language
    context["ui"] = language_ui
    context["games"] = dict(sorted(games.items(), key=lambda t: t[0].replace("_", "").upper()))
    with openw_with_sm(output, os.path.join(language, "list.html"), priority="0.6") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("list.html").render(context))
        f.write(env.get_template("footer.html").render(context))

    '''if not args.no_searchdb:
        glist = {}
        for id, data in games.items():
            desc = get(data, language, "description")
            desc = (desc[:480] + (desc[480:] and '...'))
            glist[id] = {}
            glist[id]["name"] = get(data, language, "name")
            glist[id]["description"] = desc
            glist[id]["thumbnail"] = image.uri("..", data["thumbnail"], id)
        with open(os.path.join(output, language, "gamelist.json"), "w") as f:
            f.write(json.dumps(glist))'''
