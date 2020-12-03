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
from itertools import islice
from datetime import datetime, timezone
import email.utils

from fgi import image, args
from fgi.i18n import get
from fgi.seo.sitemap import openw_with_sm
from fgi.base import sorted_games_by_mtime, strip_games_expunge

def ts_to_rfc5322(ts):
    dt = datetime.fromtimestamp(ts, tz=timezone.utc)
    return email.utils.format_datetime(dt)

def list_games(games):
    for name, game in games.items():
        if "replaced-by" in game \
                or "expuge" in game:
            continue
        yield name, game

context = {
    "rr": "..",
    "active_list": "actived",
    "uri_to_html_image": image.uri_to_html_image,
    "get": get,
    "ts_to_rfc5322": ts_to_rfc5322
}

def render(games, env, lctx, output):
    context.update(lctx)
    language = lctx["lang"]

    context["games"] = list_games(games)
    with openw_with_sm(output, os.path.join(language, "list.html"), priority="0.6") as f:
        f.write(env.get_template("header.html").render(context))
        f.write(env.get_template("list.html").render(context))
        f.write(env.get_template("footer.html").render(context))

    if args.args.with_rss:
        context["games"] = islice(strip_games_expunge(sorted_games_by_mtime(games)).items(), 30)
        with open(os.path.join(output, language, "feed.xml"), "w") as f:
            f.write(env.get_template("rss_feed.xml").render(context))
