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

        if "type" in image and image["type"] == "youtube":
            return '<iframe width="100%%" height="342" src="https://www.youtube.com/embed/%s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>' % image["uri"].split(":")[1]

        return '<img src="%s">' % uri(rr, image, game_name)
