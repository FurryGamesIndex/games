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

import re
import os
import hashlib
from shutil import copyfile
from html import escape
from utils.webutils import dl
from utils import webp
from __main__ import args

regexp = re.compile("^[a-zA-Z0-9\-]+:/{0,2}[^/]+")

class Image:
    def __init__(self, uri):
        self.uri = uri
        self.is_remote = regexp.match(uri)

def _uri(rr, image, gameid):
    if image.is_remote:
        if args.download_external_images:
            path = image.uri
            sum = hashlib.sha1(image.uri.encode("utf-8")).hexdigest()
            path = "assets/" + gameid + "/" + sum + os.path.splitext(image.uri)[1]
            image.path = os.path.join(args.output, path)

            if not os.path.isfile(image.path):
                if args.use_external_images_cache is not None:
                    cached_image = os.path.join(args.use_external_images_cache, path)
                    if os.path.isfile(cached_image):
                        copyfile(cached_image, image.path)
                    else:
                        print("cache missing, downloading %s %s" % (sum, image.uri))
                        dl(image.uri, image.path)
                else:
                    print("downloading %s %s" % (sum, image.uri))
                    dl(image.uri, os.path.join(args.output, path))

            image.is_remote = False
            image.uri = rr + "/" + path
    else:
        path = "assets/" + gameid + "/" + image.uri
        image.path = os.path.join(args.output, path)
        image.uri = rr + "/" + path

def uri(rr, imageuri, gameid):
    img = Image(imageuri)
    _uri(rr, img, gameid)

    path = img.path

    if args.images_to_webp \
            and not img.is_remote \
            and webp.can_convert(path):
        img.uri += ".webp"
        img.path += ".webp"

        if not os.path.exists(img.path) \
                and os.path.exists(path):
            webp.cwebp(path, img.path)
            os.remove(path)

    return img.uri

def _media_image(rr, image, gameid, name):
    if "sensitive" in image and image["sensitive"] == True:
        return '<img class="sensitive_img hide" data-realsrc="%s" src="data:image/png;base64,">' % uri(rr, image["uri"], gameid)
    else:
        return '<img alt="%s" src="%s">' % (escape(name), uri(rr, image["uri"], gameid))

def _media_youtube(rr, image, gameid, name):
    return '<iframe width="100%%" height="342" src="https://www.youtube.com/embed/%s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>' % image["uri"].split(":")[1]

def _media_video(rr, image, gameid, name):
    elm = '<video controls width="100%">'
    for i in image["src"]:
        elm += '<source src="%s" type="%s">' % (i["uri"], i["mime"])
    return elm + "</video>"

def dom(rr, image, gameid, name = ""):
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

    return mode(rr, image_meta, gameid, name)
