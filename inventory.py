import json
from networking import Networking
from item import Item


class Inventory:
    def __init__(self, n: Networking, steamid):
        self.n = n
        self.steamid = steamid

        self.inventoryjson = json.loads(
            self.n.do_community_request(f"inventory/{self.steamid}/730/2?l=english&count=2000").text
        )
        if self.inventoryjson != None:
            self.itemlist = self.parse_inventory_json()

    def get_inventory_json(self):
        return self.inventoryjson

    def get_inventory_item_names(self):
        out = []
        for item in self.itemlist:
            out.append(item.get_name())
        return out

    def parse_inventory_json(self):
        out = []
        for x in self.inventoryjson["descriptions"]:
            i = Item(x)
            out.append(i)
        return out

    def get_inventory_items_with_description(self):
        out = []
        for item in self.itemlist:
            out.append((item.get_name(), item.get_description()))
        return out

    def get_inventory_items_with_type(self):
        out = []
        for item in self.itemlist:
            out.append((item.get_name(), item.get_type()))
        return out

    def get_sorted_inventory(self):
        out = []
        unsorted = self.get_inventory_items_with_type()
        for item in unsorted:
            if not out:
                sublist = [item]
                out.append(sublist)
            listexists = False
            for sublist in out:
                if sublist[0][1] == item[1]:
                    sublist.append(item)
                    listexists = True
            if not listexists:
                sublist = [item]
                out.append(sublist)
        return out
