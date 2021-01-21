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

from fgi.plugin import Plugin

_cdn_list = {
    "china": "https://media.st.dl.pinyuncloud.com/",
    "akamai-old": "https://steamcdn-a.akamaihd.net/",
    "akamai": "https://cdn.akamai.steamstatic.com/",
    "cf": "https://cdn.cloudflare.steamstatic.com/",
}

class SteamCDNUnitePlugin(Plugin):
    def __init__(self, options):
        self.verbose = False
        self.cdn = "akamai"

        super().__init__(options)

        self._bad_cdns = _cdn_list.copy()
        self._bad_cdns.pop(self.cdn)
        self._unified_cdn_uri_base = _cdn_list[self.cdn]

    def _replace_uri(self, uri):
        for _, prefix in self._bad_cdns.items():
            if uri.startswith(prefix):
                uri = uri.replace(prefix, self._unified_cdn_uri_base)
                if self.verbose:
                    print(f"[info] [steam-cdn-unite] replace uri from {prefix} to {uri}")
                return uri

        return uri

    def image_post_html_image_done(self, hi, *args, **kwargs):
        for i in hi.sources:
            img = i.srcset
            if img.is_remote:
                img.uri = self._replace_uri(img.uri)

impl = SteamCDNUnitePlugin
