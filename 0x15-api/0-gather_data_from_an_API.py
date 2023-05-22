#!/usr/bin/python3

"""
This script retrieves the TODO list progress for a given employee ID.
It uses the JSONPlaceholder API to fetch the data.
"""

import requests


def get_employee_todo_list(employee_id):
    """
    Retrieves the TODO list progress for the given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    url = 'https://jsonplaceholder.typicode.com'
    employee = f'{url}/users/{employee_id}'
    todo_list = f'{url}/todos?userId={employee_id}'

    employee_req = requests.get(employee)
    employee_data = employee_req.json()
    employee_name = employee_data.get('name')

    todo_list__response = requests.get(todo_list)
    todo_list_data = todo_list__response.json()

    total_tasks = len(todo_list_data)
    finished_tasks = sum(1 for todo in todo_list_data if todo.get('completed'))

    print(f"Employee {employee_name} is done with tasks ({finished_tasks}/{total_tasks}):")
    for todo in todo_list_data:
        if todo.get('completed'):
            print(f"\t\t{todo.get('title')}")


if __name__ == "__main__":
    get_employee_todo_list(1)


