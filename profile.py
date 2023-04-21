from networking import Networking
from gamestats import Gamestats
import json


class Profile:
    def __init__(self, n: Networking, steamid):
        self.n = n
        self.pjson = json.loads(self.n.do_request(f"ISteamUser/GetPlayerSummaries/v0002/?key={self.n.get_api_key()}&steamids={steamid}").text)["response"]["players"][0]
        self.steamid = self.pjson["steamid"]
        self.name = self.pjson["personaname"]
        self.gamestats = None
    def get_json(self):
        return self.pjson

    def get_gamestats(self):
        if self.gamestats is None:
            self.gamestats = Gamestats()
            self.csjson = json.loads(self.n.do_request(f"ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key={self.n.get_api_key()}&steamid={self.steamid}").text)
            return self.csjson
        else:
            return self.csjson
