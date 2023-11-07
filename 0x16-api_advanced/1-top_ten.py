#!/usr/bin/python3
"""Module to print the top 10 hot posts of a subreddit"""

import requests
import sys


def top_ten(subreddit):
    """
    Prints the top 10 hot posts of a subreddit
    """
    req_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Switch value to prevent breaking"
    }
    params = {
        "limit": 10
    }
    r = requests.get(
            req_url, headers=headers, params=params, allow_redirects=False)
    if r.status_code == 200:
        bulk_resp = r.json()
        children = bulk_resp.get('data').get('children')
        titles = list(map(lambda x: x.get('data').get('title'), children))
        for i in titles:
            print(i)
    else:
        print(None)


if __name__ == "__main__":
    top_ten(sys.argv[1])
