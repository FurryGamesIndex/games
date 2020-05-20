# -*- coding: utf-8 -*-

class searchdb:
    def __init__(self):
        self.db = {}
        self.db["rtag"] = {}

    def update(self, game):
        for ns, tags in game["tags"].items():
            for v in tags:
                tag = ns + ":" + v
                if tag not in self.db["rtag"]:
                    self.db["rtag"][tag] = []
                self.db["rtag"][tag].append(game["id"])
