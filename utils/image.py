# -*- coding: utf-8 -*-

import re
import os
import hashlib
from utils.webutils import dl
from __main__ import args

regexp = re.compile("^[a-zA-Z0-9\-]+:/{0,2}[^/]+")

def uri(rr, image, game_name):
    if (regexp.match(image)):
        if args.download_external_images:
            uri = image
            sum = hashlib.sha1(image.encode("utf-8")).hexdigest();
            image = "assets/" + game_name + "/" + sum + os.path.splitext(uri)[1]

            if not os.path.isfile(os.path.join(args.output, image)):
                print("downloading %s %s" % (sum, uri))
                dl(uri, os.path.join(args.output, image))

            image = rr + "/" + image

        return image
    else:
        return rr + "/assets/" + game_name + "/" + image

def _media_image(rr, image, game_name):
    if "sensitive" in image and image["sensitive"] == True:
        return '<img class="sensitive_img hide" data-realsrc="%s" src="data:image/png;base64,">' % uri(rr, image["uri"], game_name)
    else:
        return '<img src="%s">' % uri(rr, image["uri"], game_name)

def _media_youtube(rr, image, game_name):
    return '<iframe width="100%%" height="342" src="https://www.youtube.com/embed/%s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>' % image["uri"].split(":")[1]

def _media_video(rr, image, game_name):
    elm = '<video controls width="100%">'
    for i in image["src"]:
        elm += '<source src="%s" type="%s">' % (i["uri"], i["mime"])
    return elm + "</video>"

def dom(rr, image, game_name):
    mode = _media_image
    image_meta = image

    if type(image) is str:
        image_meta = dict()
        image_meta["uri"] = image
    elif "type" in image:
        if image["type"] == "youtube":
            mode = _media_youtube
        if image["type"] == "video":
            mode = _media_video

    return mode(rr, image_meta, game_name)
