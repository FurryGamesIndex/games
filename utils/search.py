# -*- coding: utf-8 -*-

class searchdb:
    def __init__(self, stub=False):
        self.db = {}
        self.db["rtag"] = {}
        self.stub = stub

    def update(self, game):
        if self.stub:
            return
        for ns, tags in game["tags"].items():
            for v in tags:
                tag = ns + ":" + v
                if tag not in self.db["rtag"]:
                    self.db["rtag"][tag] = []
                self.db["rtag"][tag].append(game["id"])
