#!/usr/bin/python3
"""returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = headers = {'User-Agent': 'Mozilla/5.0'}
    req = requests.get(url.format(subreddit), headers=headers)
    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
