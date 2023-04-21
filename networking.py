import requests


class Networking:
    def __init__(self, apikey):
        self.apiKey = apikey

    def do_request(self, command):
        return requests.get("https://api.steampowered.com/" + command)

    def get_api_key(self):
        return self.apiKey

