# -*- coding: utf-8 -*-

# 
# Copyright (C) 2021 Utopic Panther
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

site_map = {
    "itch.io": "itch-io",
    "gog.com": "gog-com",
    "demo-version-steam": "steam",
    "demo-version-gog.com": "gog-com",
}

platform_map = {
    "web": "safari",
    "playstation2": "playstation",
    "playstation3": "playstation",
    "playstation4": "playstation",
    "playstation5": "playstation",
    "psv": "playstation",
    "psp": "playstation",
    "xbox-one": "xbox",
    "xbox-360": "xbox",
    "xbox-series-x": "xbox",
    "xbox-series-s": "xbox",
}

class IconFactory:
    def __init__(self, data):
        self.data = data
        self.cache = dict()

    def icon(self, name, fallback="misc-fallback", fallback_html=None):
        if fallback and name not in self.data:
            name = fallback
        if fallback_html and name not in self.data:
            return fallback_html

        if name in self.cache:
            return self.cache[name]

        code = self.data[name]
        data_icon = f"&#{code};"

        icon = f'<span class="icon" data-icon="{data_icon}" aria-hidden="true"></span>'
        self.cache[name] = icon
        return icon

    def misc_icon(self, name):
        return self.icon("misc-" + name, fallback=None)

    def os_icon(self, name, fallback_html=None):
        if name in platform_map:
            name = platform_map[name]

        return self.icon("os-" + name, fallback=None, fallback_html=fallback_html)

    def site_icon(self, name):
        if name in site_map:
            name = site_map[name]

        return self.icon("site-" + name, fallback="site-fallback")
