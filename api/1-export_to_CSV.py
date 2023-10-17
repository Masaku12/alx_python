#!/usr/bin/python

"""
This script retrieves and displays information on an employee's TODO list
using REST API. It accepts employee ID as a param and provides details
about the employee's completed tasks alongside their titles.
It also exports the data to a CSV file.

Usage: 1-export_to_CSV.py <employee_id>
"""

import requests
import sys
import csv


def get_employee_info(employee_id):
    # Defines the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Sends a GET request to retrieve employee details
    employee_response = requests.get(f"{base_url}/users/{employee_id}")

    # Checks if the request was successful
    if employee_response.status_code != 200:
        print("Missing Employee Details")
        return

    employee_data = employee_response.json()
    employee_name = employee_data["name"]

    # Sends a GET request to retrieve the employee TODO list details
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")

    if todos_response.status_code != 200:
        print("Missing TODO List")
        return
    
    todos_data = todos_response.json()
    
    # Creates a CSV file for the employee
    with open(f"{employee_id}.csv", mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for todo in todos_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": str(todo["completed"]),
                "TASK_TITLE": todo["title"],
            })
  
    print(f"Employee {employee_name}'s task data has been exported to {employee_id}.csv")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
