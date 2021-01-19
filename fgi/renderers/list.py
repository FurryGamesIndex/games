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

from fgi.renderer import Renderer
from fgi.i18n import get
from fgi.base import sorted_games_by_mtime, strip_games_expunge

def ts_to_rfc5322(ts):
    dt = datetime.fromtimestamp(ts, tz=timezone.utc)
    return email.utils.format_datetime(dt)

def list_games(games):
    for name, game in games.items():
        if "replaced-by" in game \
                or "expunge" in game:
            continue
        yield name, game

class RendererList(Renderer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.basectx = {
            "rr": "..",
            "active_list": "actived",
            "get": get,
            "ts_to_rfc5322": ts_to_rfc5322,
        }

        self.games = self.lctx["games"]

    def render(self):
        context = self.new_context()

        context["games"] = list_games(self.games)
        with self.sm_openw("list.html", priority="0.6") as f:
            f.write(self.env.get_template("list.html").render(context))

        if self.fctx.args.with_rss:
            context["games"] = islice(strip_games_expunge(sorted_games_by_mtime(self.games)).items(), 30)
            with open(self.getpath("feed.xml"), "w") as f:
                f.write(self.env.get_template("rss_feed.xml").render(context))

impl = RendererList
