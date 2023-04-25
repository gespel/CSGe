from pprint import pprint

from networking import Networking
from profile import Profile

if __name__ == '__main__':
    n = Networking("E439A9FEF52521F0D816C2EEDA336C9E")
    p = Profile(n, "76561198024898448")
    pprint(p.get_inventory().get_inventory_items_with_type())
