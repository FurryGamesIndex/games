# -*- coding: utf-8 -*-

import re

regexp = re.compile("^[a-zA-Z0-9\-]+:/{0,2}[^/]+")

def uri(rr, image, game_name):
    if (regexp.match(image)):
            return image
    else:
        return rr + "/assets/" + game_name + "/" + image

def dom(rr, image, game_name):
    if type(image) is str:
        return '<img src="%s">' % uri(rr, image, game_name)
    else:
        if "sensitive" in image and image["sensitive"] == True:
            return '<img class="sensitive_img hide" data-realsrc="%s" src="data:image/png;base64,">' % uri(rr, image["uri"], game_name)

        return '<img src="%s">' % uri(rr, image, game_name)
