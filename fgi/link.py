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

from fgi.icon import IconFactory

ua_wellknown_uri_set = { "http", "https", "ftp", "mailto" }

simple_uri_scheme_map = {
    "steam": "https://store.steampowered.com/app/%s",
    "twitter": "https://twitter.com/%s/",
    "furaffinity": "https://www.furaffinity.net/user/%s/",
    "patreon": "https://www.patreon.com/%s",
    "tumblr": "https://%s.tumblr.com/",
    "pixiv": "https://www.pixiv.net/users/%s",
    "google-play-store": "https://play.google.com/store/apps/details?id=%s",
    "youtube": "https://www.youtube.com/%s",
    "facebook": "https://www.facebook.com/%s",
    "discord": "https://discord.gg/%s",
    "FGI-misc-page": "/misc/%s.html",
}

def uri_to_ua_uri(uri):
    if uri[0] == '/':
        return uri

    res = uri.split(':', 1)
    if len(res) < 2:
        raise ValueError(f"Invalid URI '{uri}': missing scheme part")

    scheme = res[0]

    if scheme in ua_wellknown_uri_set:
        return uri

    if scheme not in simple_uri_scheme_map:
        raise ValueError(f"URI with scheme '{scheme}' is neither UA-wellknown URI nor FGI's simple URI")

    return simple_uri_scheme_map[scheme] % res[1]

class Link:
    def __init__(self, data, ifac: IconFactory):
        self.stock = False
        self.html_attrs = dict()
        self.l10n_names = dict()

        name = data["name"]
        if name[0] == '.':
            name = name[1:]
            self.stock = True

        if "icon" in data:
            self.icon = ifac.site_icon(data["icon"])
        elif self.stock:
            self.icon = ifac.site_icon(name)
        else:
            self.icon = ifac.site_icon("fallback")

        self.name = name

        if "rel" in data:
            self.add_html_attr("rel", data["rel"])

        self.uri = data["uri"]
        self.href = uri_to_ua_uri(self.uri)

    def add_html_attr(self, name, value):
        self.html_attrs[name] = value

    def add_l10n_name_from_trdata(self, ln, trdata):
        if self.stock:
            return

        if self.name in trdata:
            self.l10n_names[ln] = trdata[self.name]

    def html(self, uil10n, ln, rr=None, node_class=None, target=None):
        name = self.name

        if self.stock:
            name = uil10n["stock-link-" + name]
        elif ln in self.l10n_names:
            name = self.l10n_names[ln]

        content = self.icon + "<span>" + name + "</span>"

        href = self.href
        if href.startswith('/'):
            if not rr:
                raise ValueError("rr is required for in-site links")

            href = rr + href

        outer = '<a href="' + href + '"'
        if node_class:
            outer = outer + ' class="' + node_class + '"'
        if target:
            outer = outer + ' target="' + target + '"'

        if self.html_attrs:
            for k, v in self.html_attrs.items():
                outer = f'{outer} {k}="{v}"'

        outer = outer + ">" + content + "</a>"
        return outer
