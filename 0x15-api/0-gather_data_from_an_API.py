#!/usr/bin/python3
"""returns information about his/her TOD_O list progress."""
from requests import get
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    url = ('https://jsonplaceholder.typicode.com')
    user = get("{}/users/{}".format(url, id)).json()
    target = get("{}/users/{}/todos".format(url, id)).json()
    u_name = user.get('name')
    done = 0
    for i in target:
        if i['completed']:
            done += 1
    print("Employee {} is done with tasks({}/{}):".format(u_name, done,
                                                          len(target)))
    for done in target:
        if done.get('completed'):
            print("\t {}".format(done.get('title')))
