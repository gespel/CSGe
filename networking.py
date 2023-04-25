import requests
from fake_useragent import UserAgent


class Networking:
    def __init__(self, apikey):
        self.apiKey = apikey
        self.user_agent = UserAgent().firefox
        self.headers = {
            "User-Agent": self.user_agent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "TE": "Trailers"
        }

    def do_request(self, command):
        return requests.get("https://api.steampowered.com/" + command, headers=self.headers)

    def do_community_request(self, command):
        print("https://steamcommunity.com/" + command)
        return requests.get("https://steamcommunity.com/" + command, headers=self.headers)

    def get_api_key(self):
        return self.apiKey

