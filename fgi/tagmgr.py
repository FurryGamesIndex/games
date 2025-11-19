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

"""
FIXME: refactor this file please!
       there are too many fucking things for backward compat!!!!!
"""

from itertools import islice


class TagManager:
    def __init__(self):
        self.tagdep = dict()
        self.tags = dict()
        self.tagalias = dict()
        self.tagns = dict()

    def closure(self, _ns, s):
        r = s.copy()

        for i in s:
            ns = _ns
            prefix = ""
            if ":" in i:
                ns, i = i.split(":")
                prefix = ns + ":"
            if ns in self.tagdep and i in self.tagdep[ns]:
                tmp = self.tagdep[ns][i]
                tmp = set([i if ":" in i else prefix + i for i in tmp])
                r = r.union(self.closure(ns, tmp))

        return r

    # FIXME; loaddep and tag-dependencies are deprecated.
    def loaddep(self, data):
        for ns, v in data.items():
            if ns[0] == "_":
                continue
            for tag, implications in v.items():
                self.set_tag_implication(tag, ns, implications)

    def set_tag_implication(self, tag, ns, implications):
        if ns not in self.tagdep:
            self.tagdep[ns] = dict()
        self.tagdep[ns][tag] = set(implications)

    def closure_all_tagdep(self):
        for ns, v in self.tagdep.items():
            for value, s in v.items():
                self.tagdep[ns][value] = self.closure(ns, s)

    def load(self, data):
        tmp = {k: v for k, v in data.items() if k[0] != "@"}

        for k, v in tmp.items():
            for ns in v["namespaces"]:
                if ns not in self.tags:
                    self.tags[ns] = {}
                    self.tags[ns]["@cur_index"] = 1

                if "order" in v:
                    self.tags[ns][k] = v["order"]
                else:
                    self.tags[ns][k] = self.tags[ns]["@cur_index"] + 6000
                    self.tags[ns]["@cur_index"] += 1

                if "implication" in v:
                    self.set_tag_implication(k, ns, v["implication"])

            if "alias" in v:
                for i in v["alias"]:
                    self.tagalias[i] = k

            self.tagns[k] = v["namespaces"]

        for ns in self.tags:
            del self.tags[ns]["@cur_index"]

        self.closure_all_tagdep()

    def _patch_ns(self, tags, ns, v):
        for i in islice(v, 0, len(v)):
            if i not in self.tagdep[ns]:
                continue

            for j in self.tagdep[ns][i]:
                if ":" in j:
                    nns, j = j.split(":")
                    if nns not in tags:
                        tags[nns] = dict()
                    tags[nns].append(j)
                else:
                    v.append(j)

    def check_and_patch(self, orig_tags, game_id):
        tags = None

        def oldns_workaround(ns):
            if ns in tags:
                for i in tags[ns]:
                    for nns in self.tagns[i]:
                        if nns not in tags:
                            tags[nns] = list()
                        tags[nns].append(i)

                del tags[ns]

        if type(orig_tags) is dict:
            tags = orig_tags.copy()
            oldns_workaround("male")
            oldns_workaround("female")
        else:
            tags = {}

            for t in orig_tags:
                for ns in self.tagns[t]:
                    if ns not in tags:
                        tags[ns] = list()
                    tags[ns].append(t)

        for ns, v in tags.items():
            if ns in self.tagdep:
                self._patch_ns(tags, ns, v)

        for ns in tags:
            if ns == "author":
                continue

            v = list(set(tags[ns]))

            def sort_tag(i):
                if i not in self.tags[ns]:
                    raise ValueError(
                        f"The tag '{ns}:{i}' is not standardized. "
                        "Is it a spelling mistake? If you wish to add tags, please edit the tags.yaml file."
                    )
                return self.tags[ns][i]

            v = sorted(v, key=sort_tag)
            tags[ns] = v

        for i in ["type", "lang", "platform"]:
            if i not in tags:
                print("[warning] missing %s namespace for game '%s'" % (i, game_id))

        return tags
