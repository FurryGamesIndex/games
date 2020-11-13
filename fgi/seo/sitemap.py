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

base_uri = "https://furrygames.top/"
base_uri_old = "https://furrygamesindex.github.io/"

sitemap_magic = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">"""

sitemap = []
sitemap_old = []

def _sm_url_entry(prefix, filename, priority=None, changefreq=None, lastmod_ts=None, lastmod_file=None):
    e = "<url><loc>" + prefix + escape(filename) + "</loc>"

    if priority is not None:
        e += "<priority>" + priority + "</priority>"
    if changefreq is not None:
        e += "<changefreq>" + changefreq + "</changefreq>"
    if lastmod_file is not None or lastmod_ts is not None:
        if lastmod_ts is None:
            lastmod_ts = os.path.getmtime(lastmod_file)
        dt = datetime.fromtimestamp(lastmod_ts, tz=timezone.utc).isoformat()
        e += "<lastmod>" + dt + "</lastmod>"

    return e + "</url>"

def openw_with_sm(output_dir, filename, priority=None, changefreq=None, lastmod_ts=None, lastmod_file=None):
    global sitemap

    if not ignore:
        sitemap.append(_sm_url_entry(base_uri, filename, priority=priority, changefreq=changefreq, lastmod_ts=lastmod_ts, lastmod_file=lastmod_file))
        sitemap_old.append(_sm_url_entry(base_uri_old, filename, priority=priority, changefreq=changefreq, lastmod_ts=lastmod_ts, lastmod_file=lastmod_file))

    return open(os.path.join(output_dir, filename), "w")

def _write_sm_file(f, arr):
    f.write(sitemap_magic)
    for i in arr:
        f.write(i)
    f.write("</urlset>")

def write_to_file(dirname):
    if ignore:
        return

    with open(os.path.join(dirname, "sitemap.xml"), "w") as f:
        _write_sm_file(f, sitemap_old)

    with open(os.path.join(dirname, "sitemap2.xml"), "w") as f:
        _write_sm_file(f, sitemap)
