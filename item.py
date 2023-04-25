import json
import pprint


class Item:
    def __init__(self, itemjson):
        pprint.pprint(itemjson)
        self.name = itemjson["name"]
        self.description = itemjson["descriptions"][1]["value"]
        self.type = itemjson["type"]

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_type(self):
        return self.type
