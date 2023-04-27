from networking import Networking
from gamestats import GameStats
from inventory import Inventory
import json


class Profile:
    def __init__(self, n: Networking, steamid):
        self.n = n
        self.pjson = json.loads(self.n.do_request(f"ISteamUser/GetPlayerSummaries/v0002/?key={self.n.get_api_key()}&steamids={steamid}").text)["response"]["players"][0]
        self.steamid = self.pjson["steamid"]
        self.name = self.pjson["personaname"]
        self.gamestats = None
        self.inventory = None
    def get_json(self):
        return self.pjson

    def load_gamestats(self):
        if self.gamestats is None:
            self.gamestats = GameStats(self.n, self.steamid)
            return self.gamestats
        else:
            return self.gamestats

    def load_inventory(self):
        if self.inventory is None:
            self.inventory = Inventory(self.n, self.steamid)
            return self.inventory
        else:
            return self.inventory
