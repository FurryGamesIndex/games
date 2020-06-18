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

        data = {}
        data["tr"] = {}
        data["name"] = game["name"]
        data["description"] = game["description"]
        data["thumbnail"] = image.uri("..", game["thumbnail"], game["id"])

        for lang in game["tr"]:
            data["tr"][lang] = {}
            if "name" in game["tr"][lang]:
                data["tr"][lang]["name"] = game["tr"][lang]["name"]
            if "description" in game["tr"][lang]:
                data["tr"][lang]["description"] = game["tr"][lang]["description"]

        self.db["data"][game["id"]] = data
