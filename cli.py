import json
import sys
from datetime import datetime
import os

TASK_FILE = "tasks.json"

def load():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as f:
        return json.load(f)

def save(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add(description):
    tasks = load()
    new_task = {
        "id": get_new_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

def get_new_id(tasks):
    return max([task["id"] for task in tasks], default=0) + 1

def update(id, description):
    tasks = load()
    for task in tasks:
        if task['id'] == id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save(tasks)
            print(f"Task updated successfully (ID: {id})")
            return
    print(f"Task with ID {id} not found")

def delete(id):
    tasks = load()
    original_length = len(tasks)
    tasks = [task for task in tasks if task['id'] != id]
    if len(tasks) < original_length:
        save(tasks)
        print(f"Task with ID {id} deleted successfully")
    else:
        print(f"Task with ID {id} not found")

def mark(status, id):
    tasks = load()
    for task in tasks:
        if task['id'] == id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save(tasks)
            return
    print(f"Task with ID {id} not found")

def list_tasks(status=None):
    tasks = load()
    if status:
        tasks = [task for task in tasks if task['status'] == status]
    if tasks:
        for task in tasks:
            print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']}")
    else:
        print("No tasks found")

def main():
    if len(sys.argv) < 2:
        print("Missing command. Usage: python cli.py <command> [options]")
        return

    action = sys.argv[1]

    try:
        if action == "add" and len(sys.argv) == 3:
            add(sys.argv[2])
        elif action == "update" and len(sys.argv) == 4:
            update(int(sys.argv[2]), sys.argv[3])
        elif action == "delete" and len(sys.argv) == 3:
            delete(int(sys.argv[2]))
        elif action in ["mark-in-progress", "mark-done"] and len(sys.argv) == 3:
            action = "in progress" if action == "mark-in-progress" else "done"
            mark(action, int(sys.argv[2]))
        elif action == "list":
            if len(sys.argv) == 2:
                list_tasks()
            elif len(sys.argv) == 3:
                list_tasks(sys.argv[2])
            else:
                raise ValueError("Invalid number of arguments for list command")
        else:
            raise ValueError("Invalid command")
    except ValueError as e:
        print(f"Error: {str(e)}")
        print("Usage: python cli.py <command> [options]")
        print("Commands: add, update, delete, mark-in-progress, mark-done, list")

if __name__ == "__main__":
    main()