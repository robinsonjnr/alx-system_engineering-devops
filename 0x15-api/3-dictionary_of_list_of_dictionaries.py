#!/usr/bin/python3
# using this REST API, for all employees ID,
# returns information about users TODO list progress
# to export data in the JSON format.
import json
from requests import get
from sys import argv


def api_to_data():
    data = {}
    url = "https://jsonplaceholder.typicode.com/"
    users = get(url + "users").json()
    for user in users:
        user_id = user.get("id")
        task_list = []
        tasks = get(url + "todos?userId={}".format(user_id)).json()
        for task in tasks:
            tdict = {}
            tdict["username"] = user.get("username")
            tdict["task"] = task.get("title")
            tdict["completed"] = task.get("completed")
            task_list.append(tdict)
        data[user_id] = task_list
    with open("todo_all_employees.json", 'w', newline='') as json_file:
        json.dump(data, json_file)

if __name__ == "__main__":
    api_to_data()
