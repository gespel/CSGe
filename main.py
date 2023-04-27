from pprint import pprint

from networking import Networking
from profile import Profile

if __name__ == '__main__':
    n = Networking("")
    p = Profile(n, "76561198024898448")
    pprint(p.load_gamestats().get_gamestats())
    si = p.load_inventory().get_sorted_inventory()
    for l in si:
        pprint(l)
