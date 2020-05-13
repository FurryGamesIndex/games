# -*- coding: utf-8 -*-

def get(game, language, key):
    l10n_value = game["tr"].get(language, {}).get(key)
    if l10n_value is not None:
        return l10n_value
    else:
        return game[key]
