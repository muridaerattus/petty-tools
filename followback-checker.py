import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("--followers", help="file name of exported list of followers from Instagram", 
                    required=False, default="followers_1.html")
parser.add_argument("--following", help="file name of exported list of accounts you follow", 
                    required=False, default="following.html")
args = parser.parse_args()

followers_raw = open(args.followers, "r").read()
following_raw = open(args.following, "r").read()
followers_list = re.findall(">([A-Za-z0-9._]*)</a>", followers_raw)
following_list = re.findall(">([A-Za-z0-9._]*)</a>", following_raw)

followers_set = set(followers_list)
rats = list(filter(lambda x: x not in followers_set, following_list))
for r in rats:
    print(r)
