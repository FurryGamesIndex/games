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

import os
import json
import hashlib
import base64
from shutil import copyfile

from fgi.image import HTMLImage, Image
from fgi.utils.webutils import dl
from fgi.utils import webp

class MediaFactory:
    def __init__(self, fctx):
        self.fctx = fctx

    def uri_to_html_image(self, _rr, imageuri, gameid, alt = None):
        rr = _rr if _rr else ""
        image = Image(imageuri)

        if image.is_remote:
            if self.fctx.args.download_external_images:
                sum = hashlib.sha1(image.uri.encode("utf-8")).hexdigest()
                path = "assets/" + gameid + "/" + sum + os.path.splitext(image.uri)[1]
                image.path = os.path.join(self.fctx.args.output, path)

                if not os.path.isfile(image.path):
                    if self.fctx.args.use_external_images_cache is not None:
                        cached_image = os.path.join(self.fctx.args.use_external_images_cache, path)
                        if os.path.isfile(cached_image):
                            copyfile(cached_image, image.path)
                        else:
                            print("cache missing, downloading %s %s" % (sum, image.uri))
                            dl(image.uri, image.path)
                    else:
                        print("downloading %s %s" % (sum, image.uri))
                        dl(image.uri, os.path.join(self.fctx.args.output, path))

                image.is_remote = False
                image.uri = rr + "/" + path
        else:
            path = "assets/" + gameid + "/" + image.uri
            image.path = os.path.join(self.fctx.args.output, path)
            if os.path.exists(image.path):
                image.mtime = os.path.getmtime(image.path)
            image.uri = rr + "/" + path

        path = image.path

        if self.fctx.args.images_to_webp \
                and not image.is_remote \
                and webp.can_convert(path):

            image.uri += ".webp"
            image.path += ".webp"

            if os.path.exists(path):
                if not os.path.exists(image.path):
                    try:
                        webp.cwebp(path, image.path)
                    except:
                        print(f"[warning] {path} can not be converted to webp")
                os.remove(path)

        hi = HTMLImage.from_image(image)
        hi.alt = alt

        if self.fctx.args.images_candidate_webp \
                and not image.is_remote \
                and webp.can_convert(path) \
                and os.path.exists(path):
            webpfn = image.path + ".webp"

            if not os.path.exists(webpfn):
                webp.cwebp(path, webpfn)

            wpi = Image(image.uri + ".webp")
            wpi.path = webpfn
            hi.add_source(wpi, "image/webp", False)

        self.fctx.pmgr.invoke_plugins("image_post_html_image_done",
            hi, rr = _rr, origin_uri = imageuri, gameid = gameid, alt = alt)
        return hi

    def _media_image(self, rr, image, gameid, name):
        hi = self.uri_to_html_image(rr, image["uri"], gameid, alt=name)

        if "sensitive" in image and image["sensitive"] == True:
            data = base64.b64encode(json.dumps({
                "type": "image",
                "data": hi.dict()
            }, separators=(',', ':')).encode('utf-8')).decode()
            return f'<script type="text/x-FGI-sensitive-media">{data}</script>'
        else:
            return hi.html()

    def _media_youtube(self, rr, image, gameid, name):
        return '<iframe width="100%%" height="342" src="https://www.youtube.com/embed/%s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>' % image["uri"].split(":")[1]

    def _media_video(self, rr, image, gameid, name):
        elm = '<video controls width="100%">'
        for i in image["src"]:
            elm += '<source src="%s" type="%s">' % (i["uri"], i["mime"])
        return elm + "</video>"

    def dom(self, rr, image, gameid, name = ""):
        mode = self._media_image
        image_meta = image

        if type(image) is str:
            image_meta = dict()
            image_meta["uri"] = image
        elif "type" in image:
            if image["type"] == "youtube":
                mode = self._media_youtube
            if image["type"] == "video":
                mode = self._media_video

        return mode(rr, image_meta, gameid, name)
