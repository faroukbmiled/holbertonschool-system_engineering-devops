#!/usr/bin/python3
"""returns information about his/her TOD_O list progress."""
from requests import get
from sys import argv
from csv import writer
import csv

if __name__ == "__main__":
    id = argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user = get("{}/users/{}".format(url, id)).json()
    target = get("{}/users/{}/todos".format(url, id)).json()
    u_name = user.get('username')
    file_format = '{}.csv'.format(id)
    with open(file_format, 'w') as result:
        for data in target:
            data = [data['userId'], u_name, data['completed'], data['title']]
            fmt = writer(result, quoting=csv.QUOTE_ALL)
            fmt.writerow(data)
