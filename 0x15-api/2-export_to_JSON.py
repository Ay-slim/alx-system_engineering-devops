#!/usr/bin/python3
"""Module to fetch and export API data to JSON(single user)"""

import json
import requests
import sys


def api_req_json_unique():
    """Api request function to fetch API data and export to JSON"""
    emp_id = int(sys.argv[1])
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    r_user = requests.get(user_url)
    u_name = r_user.json().get('username')
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    r_todo = requests.get(todo_url)
    all_todos = r_todo.json()
    emp_todos = list(
            filter(lambda x: x.get('userId') == emp_id, all_todos))
    user_todos = list(
            map(lambda x: {
                "task": x.get('title'),
                "completed": x.get('completed'),
                "username": u_name}, emp_todos))
    json_object = json.dumps({emp_id: user_todos})
    filename = "{}.json".format(emp_id)
    with open(filename, "w") as f:
        f.write(json_object)


if __name__ == "__main__":
    api_req_json_unique()
