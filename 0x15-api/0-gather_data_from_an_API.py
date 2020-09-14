#!/usr/bin/python3
""" Script to have TODO list"""

import requests
import sys


if __name__ == "__main__":

    if sys.argv[1].isdigit():
        # user id
        user_id = sys.argv[1]

        # URLS to get data
        todos_url = "https://jsonplaceholder.typicode.com/todos/"
        employee_url = "https://jsonplaceholder.typicode.com/users/" + user_id

        # Request
        employee_todos = requests.get(todos_url)
        employee_data = requests.get(employee_url)

        # Converting into DICT
        json_employee = employee_data.json()
        json_todos = employee_todos.json()

        # Extracting TODO data of employee
        total_todos = 0
        done_todos = 0
        done_tasks = []
        for each_dict in json_todos:
            if each_dict['userId'] == int(user_id):
                if each_dict['completed']:
                    done_tasks.append(each_dict['title'])
                    done_todos += 1
                total_todos += 1
        # Ouputting the data
        text = 'Employee {} is done with tasks({}/{}):\
    '.format(json_employee['name'], done_todos, total_todos)
        print(text)
        for task in done_tasks:
            print('\t {}'.format(task))
