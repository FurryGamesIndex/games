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

class HTMLBaseMedia:
    def __init__(self):
        self.sensitive = False

class HTMLMiscellaneousMedia(HTMLBaseMedia):
    def __init__(self, outerHTML, sensitive):
        super().__init__()
        self.outerHTML = outerHTML
        self.sensitive = sensitive

    def dom(self, rr, **kwargs):
        if self.sensitive:
            data = base64.b64encode(self.outerHTML.encode('utf-8')).decode()
            return f'<script type="text/x-FGI-sensitive-media-misc">{data}</script>'
        else:
            return self.outerHTML

class HTMLImageMedia(HTMLBaseMedia):
    def __init__(self, hi, sensitive):
        super().__init__()
        self.hi = hi
        self.sensitive = sensitive

    def dom(self, rr, alt=None, **kwargs):
        if self.sensitive:
            data = base64.b64encode(json.dumps({
                "type": "image",
                "data": self.hi.with_rr(rr).dict()
            }, separators=(',', ':')).encode('utf-8')).decode()
            return f'<script type="text/x-FGI-sensitive-media">{data}</script>'
        else:
            return self.hi.with_rr(rr).html(alt=alt)

class HTMLSteamWidgetMedia(HTMLBaseMedia):
    def __init__(self, swid):
        super().__init__()
        self.id = swid

    def dom(self, rr, **kwargs):
        html = f'<iframe sandbox="allow-popups allow-popups-to-escape-sandbox allow-scripts allow-forms allow-same-origin" src="https://store.steampowered.com/widget/{self.id}/" frameborder="0" width="100%" height="190"></iframe>'
        data = base64.b64encode(html.encode('utf-8')).decode()
        return f'<script type="text/x-FGI-steam-widget">{data}</script>'


class MediaFactory:
    def __init__(self, fctx):
        self.fctx = fctx

    def uri_to_html_image(self, imageuri, gameid):
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
                image.uri = path
        else:
            path = "assets/" + gameid + "/" + image.uri
            image.path = os.path.join(self.fctx.args.output, path)
            if os.path.exists(image.path):
                image.mtime = os.path.getmtime(image.path)
            image.uri = path

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
            hi, origin_uri = imageuri, gameid = gameid)
        return hi


    def _create_image_media(self, uri, gameid, sensitive = False):
        hi = self.uri_to_html_image(uri, gameid)
        return HTMLImageMedia(hi, sensitive)

    def create_media(self, media, gameid):
        mtype = "image"
        sensitive = False

        if type(media) is str:
            return self._create_image_media(media, gameid)
        else:
            if "type" in media:
                mtype = media["type"]

            if "sensitive" in media:
                sensitive = media["sensitive"]

        if mtype == "image":
            return self._create_image_media(media["uri"], gameid, sensitive=sensitive)

        elif mtype == "youtube":
            if "id" in media:
                videoid = media["id"]
            else:
                videoid = media["uri"].split(":")[1]
            return HTMLMiscellaneousMedia(f'<iframe width="100%%" height="342" src="https://www.youtube.com/embed/{videoid}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>', sensitive)

        elif mtype == "video":
            elm = '<video controls width="100%">'
            for i in media["src"]:
                elm += '<source src="%s" type="%s">' % (i["uri"], i["mime"])
            return HTMLMiscellaneousMedia(elm + "</video>", sensitive)

        elif mtype == "steam-widget":
            return HTMLSteamWidgetMedia(media["id"])

        else:
            raise ValueError(f"Unknown media type '{mtype}'")
