#!/usr/bin/python3
"""Module to fetch the user count of a subreddit"""

import requests
import sys


def number_of_subscribers(subreddit):
    req_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Switch value to prevent breaking"
    }
    r = requests.get(req_url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        bulk_resp = r.json()
        return bulk_resp.get('data').get('subscribers')
    return 0


if __name__ == "__main__":
    number_of_subscribers(sys.argv[1])
