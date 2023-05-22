#!/usr/bin/python3
# using this REST API, for a given employee ID,
# returns information about his/her TODO list progress
# to export data in the JSON format.
import json
from requests import get
from sys import argv


def api_to_json(user_id):
    task_list = []
    url = "https://jsonplaceholder.typicode.com/"
    user = get(url + "users/{}".format(user_id)).json()
    tasks = get(url + "todos?userId={}".format(user_id)).json()
    for task in tasks:
        tdict = {}
        tdict["task"] = task.get("title")
        tdict["completed"] = task.get("completed")
        tdict["username"] = user.get("username")
        task_list.append(tdict)
    with open("{}.json".format(user_id), 'w', newline='') as json_file:
        json.dump({argv[1]: task_list}, json_file)

if __name__ == "__main__":
    api_to_json(int(argv[1]))
