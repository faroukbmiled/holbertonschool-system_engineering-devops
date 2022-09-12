#!/usr/bin/python3
"""returns information about his/her TOD_O list progress."""
from json import dump
from requests import get

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user = get('{}/users'.format(url)).json()
    target = get('{}/todos'.format(url)).json()
    data = {}
    for i in user:
        data[i['id']] = []
        for x in target:
            fmt = {'username': i['username'], 'task': x['title'],
                   'completed': x['completed']}
            if x['userId'] == i['id']:
                data[i['id']].append(fmt)
    json = 'todo_all_employees.json'
    with open(json, 'w') as result:
        dump(data, result)
