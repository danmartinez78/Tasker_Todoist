#!/usr/bin/python

import sys
import todoist

keyfile = open('key.txt', 'r')
key = keyfile.readline()

api = todoist.TodoistAPI(key)
api.sync()

task = ' '.join(sys.argv[1:])

for item in api['items']:
    if item['content'] == task:
        api.items.update_date_complete(item['id'])
        api.commit()
        break