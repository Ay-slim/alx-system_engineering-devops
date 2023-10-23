#!/usr/bin/python3
"""Module to fetch and export API data to JSON"""

import json
import requests
import sys


def api_req_json():
    """Functiobn to fetch API data and export to JSON"""
    user_url = "https://jsonplaceholder.typicode.com/users"
    r_user = requests.get(user_url)
    users_list = r_user.json()
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    r_todo = requests.get(todo_url)
    all_todos = r_todo.json()
    json_prep = {}
    user_map = {}
    for x in users_list:
        user_map[x.get('id')] = x
        json_prep[x.get('id')] = []
    for y in all_todos:
        userId = y.get('userId')
        json_prep[userId].append({
            "username": user_map.get(userId).get('username'),
            "task": y.get('title'),
            "completed": y.get('completed')
            })
    json_object = json.dumps(json_prep)
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        f.write(json_object)


if __name__ == "__main__":
    api_req_json()
