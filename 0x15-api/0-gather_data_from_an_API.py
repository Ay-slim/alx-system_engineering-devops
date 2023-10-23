#!/usr/bin/python3
"""Module to fetch and print API data"""

import requests
import sys


def api_req():
    """Api request function"""
    emp_id = int(sys.argv[1])
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    r_todo = requests.get(todo_url)
    all_todos = r_todo.json()
    emp_todos = list(
            filter(lambda x: x.get('userId') == emp_id, all_todos))
    done_todos = list(
            filter(lambda x: x.get('completed') is True, emp_todos))
    emp_len = len(emp_todos)
    done_len = len(done_todos)
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    r_user = requests.get(user_url)
    u_name = r_user.json().get('name')
    for done in done_todos:
        print("\t {}".format(done.get('title')))


if __name__ == "__main__":
    api_req()
