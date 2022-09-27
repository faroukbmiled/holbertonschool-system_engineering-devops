#!/usr/bin/python3
"""returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = headers = {'User-Agent': 'Mozilla/5.0'}
    with requests.session() as client:
        req = client.get(url, headers=headers, allow_redirects=False).json()
    try:
        return req.get('data', {}).get('subscribers')
    except Exception:
        return 0
