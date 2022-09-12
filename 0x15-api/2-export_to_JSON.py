#!/usr/bin/python3
"""returns information about his/her TOD_O list progress."""
from requests import get
from sys import argv
from json import dump

if __name__ == "__main__":
    id = argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user = get("{}/users/{}".format(url, id)).json()
    target = get("{}/users/{}/todos".format(url, id)).json()
    u_name = user.get('username')
    fmt = {}
    fmt[id] = []
    for i in target:
        append = {'task': i['title'], 'completed': i['completed'],
                  'username': u_name}
        fmt[id].append(append)
    file_format = '{}.csv'.format(id)
    with open(file_format, 'w') as result:
        dump(fmt, result)
