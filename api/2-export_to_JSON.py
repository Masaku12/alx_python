#!/usr/bin/python3

"""
This script retrieves and exports information on an employee's TODO list
using REST API in JSON format. It accepts employee ID as a param and provides details
about the employee's completed tasks alongside their titles in a JSON file.

Usage: 2-export_to_JSON.py <employee_id>
"""

import json
import requests
import sys


def export_employee_todo_data(employee_id):
    """Fetches the employee's TODO list and progress from the JSON Placeholder API,
    and exports the data to a JSON file.

    Args:
        employee_id: The employee ID (should be a positive integer).

    This function fetches the employee's tasks and details, and exports them to a JSON file
    named USER_ID.json, where USER_ID is the employee's ID.
    """
    if not employee_id.isdigit() or int(employee_id) <= 0:
        print("Please enter a valid positive integer for the employee ID.")
        return

    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

    try:
        response = requests.get(employee_url)
        employee_data = json.loads(response.content.decode())
        employee_name = employee_data["username"]

        response = requests.get(todo_url)
        todo_data = json.loads(response.content.decode())

        tasks = []
        for task in todo_data:
            task_entry = {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_name
            }
            tasks.append(task_entry)

        json_data = {employee_id: tasks}

        filename = f"{employee_id}.json"

        with open(filename, "w") as f:
            json.dump(json_data, f)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = sys.argv[1]
        export_employee_todo_data(employee_id)
    except ValueError:
        print("Please enter a valid integer for the employee ID.")
