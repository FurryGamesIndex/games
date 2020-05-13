# -*- coding: utf-8 -*-

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

    if name[0] == '.':
        a["content"] = ui_l10n_data["stock-link-" + link["name"][1:]]
    else:
        l10n_name = l10n_data.get(language, {}).get("links-tr", {}).get(name)
        if l10n_name is not None:
            a["content"] = l10n_name
        else:
            a["content"] = name
        a["content"] = '<i class="fas fa-external-link-alt"></i> ' + a["content"]

    return a
