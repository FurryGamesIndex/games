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
from itertools import islice
from datetime import datetime, timezone
import email.utils

from fgi.renderer import Renderer
from fgi.base import sorted_games_by_mtime, strip_games_expunge, make_wrapper
from fgi.game import Tag

def ts_to_rfc5322(ts):
    dt = datetime.fromtimestamp(ts, tz=timezone.utc)
    return email.utils.format_datetime(dt)

def list_games(games, chain):
    for gid, game in games.items():
        if game.expunge or \
                game.replaced_by:
            continue

        ignored_by_filter = False
        for i in chain:
            if not i(game):
                ignored_by_filter = True
                break

        if ignored_by_filter:
            continue

        yield gid, game

class ListKlass:
    def __init__(self, nameid):
        self.nameid = nameid
        self.filters = list()

    def insert(self, index, filteR):
        filteR.set_klass(self)
        self.filters.insert(index, filteR)

    def add(self, filteR):
        filteR.set_klass(self)
        self.filters.append(filteR)

class ListFilter:
    def __init__(self, magic, nameid, template = None):
        self.magic = magic
        self.nameid = nameid
        self.template = template

    def __call__(self, game):
        return True

    def set_klass(self, klass):
        self.klass = klass

class ListFilterTag(ListFilter):
    def __init__(self, *args, tags = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.tags = tags

    def __call__(self, game):
        for tag in self.tags:
            if game.has_tag(tag):
                return True

        return False

class ListFilterAllNot(ListFilter):
    def __init__(self, *args, inputs = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.inputs = inputs

    def __call__(self, game):
        for i in self.inputs:
            if i(game):
                return False

        return True

def sorted_magic(magic):
    magic = ''.join(sorted(magic))

    if magic != "":
        magic = "-" + magic

    return magic

class RendererList(Renderer):
    def __init__(self, *args, **kwargs):
        self.basectx = {
            "rr": "..",
            "active_list": "activated",
            "ts_to_rfc5322": ts_to_rfc5322,
            "sorted_magic": sorted_magic,
        }

        super().__init__(*args, **kwargs)

        self.games = self.lctx["games"]

        self.klasses = list()

        sub_lists = not self.fctx.args.no_sub_lists

        if sub_lists:
            klass_genre = ListKlass("genre")
            klass_genre.add(ListFilter('', "genre-all"))
            klass_genre.add(ListFilterTag('v', "genre-vn-ds", tags=[
                Tag("type", "visual-novel"),
                Tag("type", "dating-sim"),
            ]))
            klass_genre.add(ListFilterTag('a', "genre-action", tags=[
                Tag("type", "action"),
            ]))
            klass_genre.add(ListFilterTag('r', "genre-rpg", tags=[
                Tag("type", "role-playing"),
            ]))
            klass_genre.add(ListFilterTag('d', "genre-adventure", tags=[
                Tag("type", "adventure"),
            ]))
            klass_genre.add(ListFilterTag('f', "genre-fighting", tags=[
                Tag("type", "fighting"),
            ]))
            klass_genre.add(ListFilterTag('s', "genre-shooter", tags=[
                Tag("type", "shooter"),
            ]))
            klass_genre.add(ListFilterTag('p', "genre-puzzle", tags=[
                Tag("type", "puzzle"),
            ]))
            klass_genre.add(ListFilterAllNot('o', "genre-others", inputs=klass_genre.filters[1:].copy()))

            self.klasses.append(klass_genre)

            klass_orientation = ListKlass("orientation")
            klass_orientation.add(ListFilter('', "orientation-all"))
            klass_orientation.add(ListFilterTag('g', "orientation-bara", tags=[
                Tag("type", "bara"),
            ]))
            klass_orientation.add(ListFilterTag('l', "orientation-yuri", tags=[
                Tag("type", "yuri"),
            ]))
            klass_orientation.add(ListFilterAllNot('x', "orientation-others", inputs=klass_orientation.filters[1:].copy()))

            self.klasses.append(klass_orientation)

            klass_platform = ListKlass("platform")
            klass_platform.add(ListFilter('', "platform-all"))
            klass_platform.add(ListFilterTag('D', "platform-desktop", tags=[
                Tag("platform", "windows"),
                Tag("platform", "macos"),
                Tag("platform", "linux"),
            ]))
            klass_platform.add(ListFilterTag('M', "platform-mobile", tags=[
                Tag("platform", "android"),
                Tag("platform", "ios"),
            ]))
            klass_platform.add(ListFilterTag('W', "platform-web", tags=[
                Tag("platform", "web"),
                Tag("platform", "shockwave-flash"),
            ]))
            klass_platform.add(ListFilterTag('C', "platform-console", tags=[
                Tag("platform", "nds"),
                Tag("platform", "2ds"),
                Tag("platform", "3ds"),
                Tag("platform", "wii-u"),
                Tag("platform", "nintendo-switch"),
                Tag("platform", "playstation"),
                Tag("platform", "psv"),
                Tag("platform", "psp"),
                Tag("platform", "playstation2"),
                Tag("platform", "playstation3"),
                Tag("platform", "playstation4"),
                Tag("platform", "playstation5"),
                Tag("platform", "xbox"),
                Tag("platform", "xbox-one"),
                Tag("platform", "xbox-360"),
                Tag("platform", "xbox-series-x"),
                Tag("platform", "xbox-series-s"),
            ]))

            self.klasses.append(klass_platform)

            klass_status = ListKlass("status")
            klass_status.add(ListFilter('', "status-all"))
            klass_status.add(ListFilterTag('F', "status-others", tags=[
                Tag("misc", "work-in-process"),
                Tag("misc", "died"),
                Tag("misc", "suspended"),
            ]))
            klass_status.insert(1, ListFilterAllNot('R', "status-released", inputs=klass_status.filters[1:].copy()))

            self.klasses.append(klass_status)

        klass_view = ListKlass("view")
        klass_view.add(ListFilter('', "view-standard", template="list.html"))
        klass_view.add(ListFilter('c', "view-complex", template="list-complex.html"))

        self.klasses.append(klass_view)


    def render(self):
        context = self.new_context()
        context["klasses"] = self.klasses

        chains = list()
        for klass in self.klasses:
            if chains:
                tmp = list()
                for i in chains:
                    for f in klass.filters:
                        ni = i.copy()
                        ni.append(f)
                        tmp.append(ni)

                chains = tmp
            else:
                for f in klass.filters:
                    chains.append([f])

        for chain in chains:
            template = None
            magic = ""

            for f in chain:
                if f.template:
                    template = f.template

                magic = magic + f.magic

            magic = sorted_magic(magic)
            #print(f"  => list{magic}")

            klassmagics = dict()
            for klass in self.klasses:
                klassmagics[klass] = ""
                for f in chain:
                    if f.klass is not klass:
                        klassmagics[klass] += f.magic

            noindex = (magic != "")

            context["noindex"] = noindex
            context['klassmagics'] = klassmagics
            context["chain"] = chain
            context["chain_set"] = set(chain)
            context["games"] = list_games(self.games, chain)
            with self.sm_openw(f"list{magic}.html", sm = not noindex, priority="0.6") as f:
                f.write(self.env.get_template(template).render(context))

        context = self.new_context()
        if self.fctx.args.with_rss:
            context["games"] = islice(strip_games_expunge(sorted_games_by_mtime(self.games)).items(), 30)
            with open(self.getpath("feed.xml"), "w") as f:
                f.write(self.env.get_template("rss_feed.xml").render(context))

impl = RendererList
