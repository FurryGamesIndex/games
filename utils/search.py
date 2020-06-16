# -*- coding: utf-8 -*-

from utils import image

class searchdb:
    def __init__(self, stub=False):
        self.db = {}
        self.db["rtag"] = {}
        self.db["data"] = {}
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

        self.db["data"][game["id"]] = {}
        self.db["data"][game["id"]]["name"] = game["name"]
        self.db["data"][game["id"]]["description"] = game["description"]
        self.db["data"][game["id"]]["thumbnail"] = image.uri("..", game["thumbnail"], game["id"])
        self.db["data"][game["id"]]["tr"] = game["tr"]
