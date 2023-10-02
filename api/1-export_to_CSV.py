import requests
import sys
import csv


def export_todo_to_csv(employee_id):
    # Get employee details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data["name"]

    # Get TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Write data to CSV
    filename = f"{employee_id}.csv"
    with open(filename, mode="w", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([employee_id, employee_name,
                            task["completed"], task["title"]])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_todo_to_csv(employee_id)
    except ValueError:
        print("Please provide a valid employee ID.")
