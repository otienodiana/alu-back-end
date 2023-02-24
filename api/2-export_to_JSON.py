#!/usr/bin/python3
""" Library to gather data from an API """

import json
import requests
import sys

""" Function to gather data from an API """

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todo = "https://jsonplaceholder.typicode.com/todos?userId={}"
    todo = todo.format(employee_id)

    user_info = requests.request("GET", url).json()
    todo_info = requests.request("GET", todo).json()

    employee_username = user_info.get("username")

    todos_info_sorted = [
        dict(zip(["task", "completed", "username"],
                 [task["title"], task["completed"], employee_username]))
        for task in todo_info]

    user_dict = {str(employee_id): todos_info_sorted}
    with open(str(employee_id) + '.json', "w") as f:
        f.write(json.dumps(user_dict))
