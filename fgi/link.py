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

from fgi.misc.icon import link_icons as icons

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

def link_info(fctx, link, l10n_data, ui_l10n_data, language):
    name = link["name"]
    a = {}

    link["uri"] = fctx.pmgr.invoke_plugins("link_pre_uri_convert", link["uri"], link, l10n_data, ui_l10n_data, language)
    a["href"] = uri_to_src(link["uri"])

    icon = '<i class="fas fa-external-link-alt fa-fw"></i>'

    if name[0] == '.':
        if name[1:] in icons:
            icon = icons[name[1:]]
        a["content"] = ui_l10n_data["stock-link-" + name[1:]]
    else:
        l10n_name = l10n_data.get(language, {}).get("links-tr", {}).get(name)
        if l10n_name is not None:
            a["content"] = l10n_name
        else:
            a["content"] = name

    if "icon" in link:
        icon = icons[link["icon"]]
    a["content"] = icon + "<span>" + a["content"] + "</span>"

    if "rel" in link:
        a["rel"] = link["rel"]

    fctx.pmgr.invoke_plugins("link_post_process", a, link, l10n_data, ui_l10n_data, language)
    return a
