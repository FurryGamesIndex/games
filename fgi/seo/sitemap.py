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
from datetime import datetime, timezone

class Sitemap:
    def __init__(self, prefix, filename):
        self.uri_prefix = prefix
        self.entries = list()
        self.filename = filename

sitemap_magic = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">"""

class SitemapGenerator:
    def __init__(self):
        self.sitemaps = list()

    def add_site(self, sitemap):
        self.sitemaps.append(sitemap)

    def add_entry(self, filename, priority=None, changefreq=None, lastmod_ts=None, lastmod_file=None):
        for sm in self.sitemaps:
            e = "<url><loc>" + sm.uri_prefix + escape(filename) + "</loc>"

            if priority is not None:
                e += "<priority>" + priority + "</priority>"
            if changefreq is not None:
                e += "<changefreq>" + changefreq + "</changefreq>"
            if lastmod_file is not None or lastmod_ts is not None:
                if lastmod_ts is None:
                    lastmod_ts = os.path.getmtime(lastmod_file)
                dt = datetime.fromtimestamp(lastmod_ts, tz=timezone.utc).isoformat()
                e += "<lastmod>" + dt + "</lastmod>"

            e = e + "</url>"
            sm.entries.append(e)

    def save(self, dirname):
        for sm in self.sitemaps:
            with open(os.path.join(dirname, sm.filename), "w") as f:
                f.write(sitemap_magic)
                for e in sm.entries:
                    f.write(e)
                f.write("</urlset>")
