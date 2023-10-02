import requests
import sys
import json

def export_todo_to_json(employee_id):
    # Get employee details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data["name"]

    # Get TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare data in the desired format
    tasks_list = [{
        "task": task["title"],
        "completed": task["completed"],
        "username": employee_name
    } for task in todos_data]
    data = {str(employee_id): tasks_list}

    # Write data to JSON file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as file:
        json.dump(data, file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py EMPLOYEE_ID")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        export_todo_to_json(employee_id)
    except ValueError:
        print("Please provide a valid employee ID.")
