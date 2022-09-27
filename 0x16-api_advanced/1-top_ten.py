#!/usr/bin/python3
"""returns the number of subscribers"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;rv:68.0)'}
    req = requests.get(url.format(subreddit), headers=headers,
                       params={"limit": 10}, allow_redirects=False)
    if req.status_code == 200:
        for data in req.json().get('data').get('children'):
            print(data.get('data').get('title'))
    elif req.status_code == 404:
        print("None")
