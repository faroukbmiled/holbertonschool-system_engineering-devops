#!/usr/bin/python3
"""returns the number of subscribers"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    url = 'https://api.reddit.com/r/{}/hot?after={}'.format(subreddit, after)
    headers = headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;rv:68.0)'}
    req = requests.get(url, headers=headers, allow_redirects=False)
    if req.status_code == 200:
        data = req.json().get('data').get('children')
        chk = req.json().get('data').get('after')
        for elem in data:
            hot_list.append(elem.get('data').get('title'))
        if chk is None:
            recurse(subreddit, hot_list, after)
        return hot_list
    elif req.status_code == 404:
        return None
