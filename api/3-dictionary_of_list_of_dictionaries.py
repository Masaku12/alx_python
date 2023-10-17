#!/usr/bin/python3

"""
This script retrieves and exports information on all employees' TODO lists
using REST API in JSON format. It provides details about each employee's
completed tasks alongside their titles in a JSON file.

Usage: 3-export_all_to_JSON.py
"""

import json
import urllib.request


def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

    try:
        with urllib.request.urlopen(employee_url) as response:
            if response.getcode() == 200:
                employee_data = json.loads(response.read().decode())
                employee_name = employee_data["username"]
            else:
                print(f"Error: Unable to fetch employee details. Status Code: {response.getcode()}")
                return None

        with urllib.request.urlopen(todo_url) as response:
            if response.getcode() == 200:
                todo_data = json.loads(response.read().decode())
            else:
                print(f"Error: Unable to fetch TODO list. Status Code: {response.getcode()}")
                return None

        return [{"username": employee_name, "task": task["title"], "completed": task["completed"]} for task in todo_data]

    except urllib.error.URLError as e:
        print(f"Error: {e}")
        return None

def export_all_employee_tasks_to_json():
    all_employees_tasks = {}

    for employee_id in range(1, 11):
        employee_tasks = get_employee_todo_progress(employee_id)

        if employee_tasks:
            user_id = f"{employee_id}"
            all_employees_tasks[user_id] = employee_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees_tasks, json_file)

if __name__ == "__main__":
    export_all_employee_tasks_to_json()