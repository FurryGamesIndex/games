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

from fgi.misc.icon import link_icons as icons, link_fallback_icon

def uri_to_src(uri):
    res = uri.split(':', 1)
    if res[0] == 'steam':
        return "https://store.steampowered.com/app/%s" % res[1]
    elif res[0] == 'twitter':
        return "https://twitter.com/%s/" % res[1]
    elif res[0] == 'furaffinity':
        return "https://www.furaffinity.net/user/%s/" % res[1]
    elif res[0] == 'patreon':
        return "https://www.patreon.com/%s" % res[1]
    elif res[0] == 'tumblr':
        return "https://%s.tumblr.com/" % res[1]
    elif res[0] == 'pixiv':
        return "https://www.pixiv.net/users/%s" % res[1]
    elif res[0] == 'google-play-store':
        return "https://play.google.com/store/apps/details?id=%s" % res[1]
    elif res[0] == 'youtube':
        return "https://www.youtube.com/%s" % res[1]
    elif res[0] == 'facebook':
        return "https://www.facebook.com/%s" % res[1]
    else:
        return uri

class Link:
    def __init__(self, data):
        self.stock = False
        self.icon = link_fallback_icon
        self.html_attrs = dict()
        self.l10n_names = dict()

        name = data["name"]
        if name[0] == '.':
            name = name[1:]
            self.stock = True
            self.set_icon(name)

        self.name = name

        if "icon" in data:
            self.set_icon(data["icon"])

        if "rel" in data:
            self.add_html_attr("rel", data["rel"])

        self.uri = data["uri"]
        self.href = uri_to_src(self.uri)

    def set_icon(self, name):
        if name in icons:
            self.icon = icons[name]

    def add_html_attr(self, name, value):
        self.html_attrs[name] = value

    def add_l10n_name_from_trdata(self, ln, trdata):
        if self.stock:
            return

        if self.name in trdata:
            self.l10n_names[ln] = trdata[self.name]

    def html(self, uil10n, ln, node_class=None, target=None):
        name = self.name

        if self.stock:
            name = uil10n["stock-link-" + name]
        elif ln in self.l10n_names:
            name = self.l10n_names[ln]

        content = self.icon + "<span>" + name + "</span>"

        outer = '<a href="' + self.href + '"'
        if node_class:
            outer = outer + ' class="' + node_class + '"'
        if target:
            outer = outer + ' target="' + target + '"'

        if self.html_attrs:
            for k, v in self.html_attrs.items():
                outer = f'{outer} {k}="{v}"'

        outer = outer + ">" + content + "</a>"
        return outer
