import json
from networking import Networking


class GameStats:
    def __init__(self, n: Networking, steamid):
        self.steamid = steamid
        self.n = n
        self.game_stats = json.loads(
            self.n.do_request(f"ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key={self.n.get_api_key()}&steamid={self.steamid}").text()
        )

    def get_game_stats(self):
        return self.game_stats
