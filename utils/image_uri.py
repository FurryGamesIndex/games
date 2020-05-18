# -*- coding: utf-8 -*-

import re

regexp = re.compile("^[a-zA-Z0-9\-]+:/{0,2}[^/]+")

def image_uri(rr, image, game_name):
    if (regexp.match(image)):
        return image
    else:
        return rr + "/assets/" + game_name + "/" + image
