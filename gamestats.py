import json
from pprint import pprint

from networking import Networking


class GameStats:
    def __init__(self, n: Networking, steamid):
        self.steamid = steamid
        self.n = n
        self.game_stats = json.loads(
            self.n.do_request(
                f"ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key={self.n.get_api_key()}&steamid={self.steamid}").text
        )

    def get_gamestats(self):
        return self.game_stats

    def get_kills(self):
        return self.get_stat_by_name("total_kills")

    def get_deaths(self):
        return self.get_stat_by_name("total_deaths")

    def get_kd(self):
        return self.get_stat_by_name("total_kills")/self.get_stat_by_name("total_deaths")

    def get_stat_by_name(self, name):
        for entry in self.game_stats["playerstats"]["stats"]:
            if name == entry["name"]:
                return entry["value"]
        return 0
