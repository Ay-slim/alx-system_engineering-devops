#!/usr/bin/python3
"""Module to fetch and export API data"""

import csv
import requests
import sys


def api_req_csv():
    """Api request function"""
    emp_id = int(sys.argv[1])
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    r_user = requests.get(user_url)
    u_name = r_user.json().get('username')
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    r_todo = requests.get(todo_url)
    all_todos = r_todo.json()
    emp_todos = list(
            filter(lambda x: x.get('userId') == emp_id, all_todos))
    csv_prep = list(map(
        lambda x: '"{}","{}","{}","{}"'.format(
            emp_id, u_name, x.get('completed'), x.get('title')), emp_todos))
    with open('2.csv', mode='w', newline='') as f:
        writer = csv.writer(f, quotechar='', quoting=csv.QUOTE_NONE)
        for row in csv_prep:
            writer.writerow(row.split(','))


if __name__ == "__main__":
    api_req_csv()
