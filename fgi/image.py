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
import heapq
import PIL.Image
from shutil import copyfile
from html import escape

from .utils.webutils import dl
from .utils import webp
from fgi import args

regexp = re.compile("^[a-zA-Z0-9\-]+:/{0,2}[^/]+")

mimemap = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".gif": "image/gif",
    ".webp": "image/webp",
}

mimenice = {
    "image/webp": 10,
    "image/jpeg": 20,
    "image/png": 30,
    "image/gif": 20
}

class Image:
    def __init__(self, uri):
        self.uri = uri
        self.is_remote = regexp.match(uri)
        self.path = None

class HTMLPictureSource:
    def __init__(self, srcset, mime):
        self.srcset = srcset
        self.type = mime

    def __lt__(self, other):
        return mimenice[self.type] < mimenice[other.type]

class HTMLImage:
    def __init__(self):
        self.sources = []
        self.src = None
        self.alt = None
        self.width = 0
        self.height = 0
        pass

    def add_source(self, source, mime, as_src = False):
        if mime is None:
            sfx = os.path.splitext(source)[1]
            if sfx in mimemap:
                mime = mimemap[sfx]
            else:
                # TODO: force disable "HTML picture" mode while mime is unknown
                #       That will always make only a single <img> element
                raise NotImplementedError(f"Can not recognize mime for {source}")

        if as_src:
            self.src = source

        heapq.heappush(self.sources, HTMLPictureSource(source, mime))

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def html(self, node_class=None, use_picture=True):
        code = None
        node = ""

        if self.src is None:
            raise ValueError("No failback image src")

        if self.alt is None:
            self.alt = ""

        if node_class is not None:
            node += f"class='{node_class}' "

        if self.width > 0:
            node += f"width='{self.width}' height='{self.height}' "

        if len(self.sources) > 1 and use_picture:
            code = "<picture>"
            for i in self.sources:
                code += f"<source srcset='{i.srcset}' type='{i.type}'>"
            code += f"<img {node}src='{self.src}' alt='{escape(self.alt)}'></picture>"
        else:
            code = f"<img {node}src='{self.src}' alt='{escape(self.alt)}'>"

        return code

    @staticmethod
    def from_image(image):
        hi = HTMLImage()
        hi.add_source(image.uri, None, True)

        if not image.is_remote \
                and os.path.exists(image.path):
            try:
                im = PIL.Image.open(image.path)
                hi.set_size(*im.size)
            except:
                print(f"[warning] can not load image {image.path}")

        return hi


def _uri(rr, image, gameid):
    if image.is_remote:
        if args.args.download_external_images:
            path = image.uri
            sum = hashlib.sha1(image.uri.encode("utf-8")).hexdigest()
            path = "assets/" + gameid + "/" + sum + os.path.splitext(image.uri)[1]
            image.path = os.path.join(args.args.output, path)

            if not os.path.isfile(image.path):
                if args.args.use_external_images_cache is not None:
                    cached_image = os.path.join(args.args.use_external_images_cache, path)
                    if os.path.isfile(cached_image):
                        copyfile(cached_image, image.path)
                    else:
                        print("cache missing, downloading %s %s" % (sum, image.uri))
                        dl(image.uri, image.path)
                else:
                    print("downloading %s %s" % (sum, image.uri))
                    dl(image.uri, os.path.join(args.args.output, path))

            image.is_remote = False
            image.uri = rr + "/" + path
    else:
        path = "assets/" + gameid + "/" + image.uri
        image.path = os.path.join(args.args.output, path)
        image.uri = rr + "/" + path

def uri_to_html_image(rr, imageuri, gameid, alt = None):
    img = Image(imageuri)
    _uri(rr, img, gameid)

    path = img.path

    if args.args.images_to_webp \
            and not img.is_remote \
            and webp.can_convert(path):

        img.uri += ".webp"
        img.path += ".webp"

        if os.path.exists(path):
            if not os.path.exists(img.path):
                try:
                    webp.cwebp(path, img.path)
                except:
                    print(f"[warning] {path} can not be converted to webp")
            os.remove(path)

    hi = HTMLImage.from_image(img)
    hi.alt = alt

    if args.args.images_candidate_webp \
            and not img.is_remote \
            and webp.can_convert(path) \
            and os.path.exists(path):
        webpfn = img.path + ".webp"

        if not os.path.exists(webpfn):
            webp.cwebp(path, webpfn)

        hi.add_source(img.uri + ".webp", "image/webp", False)

    return hi

# TODO: remove deprecated function uri
def uri(rr, imageuri, gameid):
    return uri_to_html_image(rr, imageuri, gameid).src


def _media_image(rr, image, gameid, name):
    if "sensitive" in image and image["sensitive"] == True:
        # TODO: use HTMLImage for sensitive images
        return '<img class="sensitive_img hide" data-realsrc="%s" src="data:image/png;base64,">' % uri(rr, image["uri"], gameid)
    else:
        return uri_to_html_image(rr, image["uri"], gameid, alt=name).html()

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
