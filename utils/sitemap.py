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
from html import escape
from datetime import datetime
from datetime import timezone

ignore = False

base_uri = "https://furrygamesindex.github.io/"

sitemap = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

def openw_with_sm(output_dir, filename, priority=None, changefreq=None, lastmod_file=None):
    global sitemap

    if not ignore:
        sitemap += "<url><loc>" + base_uri + escape(filename) + "</loc>"
        if priority is not None:
            sitemap += "<priority>" + priority + "</priority>"
        if changefreq is not None:
            sitemap += "<changefreq>" + priority + "</changefreq>"
        if lastmod_file is not None:
            dt = datetime.fromtimestamp(os.path.getmtime(lastmod_file), tz=timezone.utc).isoformat()#.strftime('%FT%T:%z')
            sitemap += "<lastmod>" + dt + "</lastmod>"
        sitemap += "</url>"

    return open(os.path.join(output_dir, filename), "w")

def write_to_file(filename):
    if ignore:
        return

    with open(filename, "w") as f:
        f.write(sitemap + "</urlset>")
