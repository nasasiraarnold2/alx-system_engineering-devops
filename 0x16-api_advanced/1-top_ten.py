#!/usr/bin/python3
"""
Function that  prints the titles
of the first 10 hot posts.
"""

import requests


def top_ten(subreddit):
    """get top ten hot topics"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": 'My agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()

        for post in posts['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
