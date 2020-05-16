# -*- coding: utf-8 -*-

icons = {
    'website': '<i class="fas fa-home"></i>',
    'steam': '<i class="fab fa-steam-symbol"></i>',
    'itch.io': '<i class="fab fa-itch-io"></i>',
    'twitter': '<i class="fab fa-twitter"></i>',
    'patreon': '<i class="fab fa-patreon"></i>',
    'weibo': '<i class="fab fa-weibo"></i>',
}

def uri_to_src(uri):
    res = uri.split(':', 1)
    if (res[0] == 'steam'):
        return "https://store.steampowered.com/app/%s" % res[1]
    elif (res[0] == 'twitter'):
        return "https://twitter.com/%s/" % res[1]
    elif (res[0] == 'patreon'):
        return "https://www.patreon.com/%s" % res[1]
    else:
        return uri

def link_info(link, l10n_data, ui_l10n_data, language):
    name = link["name"]
    a = {}
    a["href"] = uri_to_src(link["uri"])

    icon = '<i class="fas fa-external-link-alt"></i>'

    if name[0] == '.':
        if name[1:] in icons:
            icon = icons[name[1:]]
        a["content"] = icon + "&nbsp;" + ui_l10n_data["stock-link-" + name[1:]]
    else:
        l10n_name = l10n_data.get(language, {}).get("links-tr", {}).get(name)
        if l10n_name is not None:
            a["content"] = l10n_name
        else:
            a["content"] = name

        if "icon" in link:
            icon = icons[link["icon"]]
        a["content"] = icon + "&nbsp;" + a["content"]

    return a
