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
import heapq
from copy import copy

import PIL.Image
from html import escape

from fgi.utils.uriutils import append_query

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
        self.is_remote = regexp.match(uri) is not None
        self.path = None
        self.mtime = None

    def get_uri(self, rr):
        if rr is None or self.is_remote:
            return self.uri
        else:
            return rr + "/" + self.uri

class HTMLPictureSource:
    def __init__(self, srcset, mime):
        self.srcset = srcset
        self.type = mime

    def __lt__(self, other):
        return mimenice[self.type] < mimenice[other.type]

class HTMLImage:
    def __init__(self):
        self.sources = []
        self._src = None
        self.width = 0
        self.height = 0
        self.query = dict()
        self.rr = None
        pass

    @property
    def src(self):
        return self._src.srcset.get_uri(self.rr)

    @src.setter
    def src(self, value):
        self._src = value

    def with_rr(self, rr):
        tmp = copy(self)
        tmp.rr = rr
        return tmp

    def add_source(self, source, mime, as_src = False):
        if mime is None:
            sfx = os.path.splitext(source.uri)[1]
            if sfx in mimemap:
                mime = mimemap[sfx]
            else:
                raise ValueError(f"Can not recognize MIME for {source.uri}")

        picture_source = HTMLPictureSource(source, mime)
        if as_src:
            self.src = picture_source

        heapq.heappush(self.sources, picture_source)

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def html(self, node_class=None, use_picture=True, alt=None):
        code = None
        node = ""

        if self.src is None:
            raise ValueError("Fallback image src required")

        if alt is None:
            alt = ""

        if node_class is not None:
            node += f"class='{node_class}' "

        if self.width > 0:
            node += f"width='{self.width}' height='{self.height}' "

        if use_picture:
            code = "<picture>"
            for i in self.sources:
                code += f"<source srcset='{append_query(i.srcset.get_uri(self.rr), self.query)}' type='{i.type}'>"
            code += f"<img {node}src='{append_query(self.src, self.query)}' alt='{escape(alt)}'></picture>"
        else:
            code = f"<img {node}src='{append_query(self.src, self.query)}' alt='{escape(alt)}'>"

        return code

    def set_size_by_image_softfail(self, image):
        try:
            im = PIL.Image.open(image.path)
            self.set_size(*im.size)
        except:
            print(f"[warning] can not load image '{image.path}' for setting html image size")

    def dict(self):
        if self.src is None:
            raise ValueError("Fallback image src required")

        tmp = dict()
        tmp["src"] = append_query(self.src, self.query)
        tmp["src_remote"] = self._src.srcset.is_remote
        tmp["source"] = list()

        for i in self.sources:
            source = dict()
            source["srcset"] = append_query(i.srcset.get_uri(self.rr), self.query)
            source["type"] = i.type
            source["remote"] = i.srcset.is_remote
            tmp["source"].append(source)

        return tmp

    @staticmethod
    def from_image(image):
        hi = HTMLImage()
        hi.add_source(image, None, True)

        if not image.is_remote \
                and os.path.exists(image.path):
            hi.set_size_by_image_softfail(image)

        if image.mtime:
            hi.query["hc"] = "uquery"
            hi.query["t"] = int(image.mtime)

        return hi
