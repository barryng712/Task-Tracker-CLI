# Task-Tracker-CLI
<<<<<<< HEAD

Task-Tracker-CLI is a simple command-line interface (CLI) application for managing and tracking your tasks. It allows you to add, update, delete, and list tasks, as well as mark their status.

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as in progress or done
- List all tasks or filter by status

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/barryng712/task-tracker-cli.git
   cd task-tracker-cli
   ```

2. Ensure you have Python 3.x installed on your system.

## Usage

Run the CLI application using Python:
```
python cli.py <command> [options]
```

### Commands

- `add <description>`: Add a new task.
- `update <id> <description>`: Update an existing task.
- `delete <id>`: Delete a task.
- `mark-in-progress <id>`: Mark a task as in progress.
- `mark-done <id>`: Mark a task as done.
- `list`: List all tasks.
- `list <status>`: List tasks by status (e.g., `list in-progress` or `list done`).

### Example

Add a new task:
```
python cli.py add "Buy groceries"
```

Update a task:
```
python cli.py update 1 "Buy groceries and vegetables"
```

Delete a task:
```
python cli.py delete 2
```

Mark a task as in progress:
```
python cli.py mark-in-progress 3
```

Mark a task as done:
```
python cli.py mark-done 4
```

List all tasks:
```
python cli.py list
```

List tasks by status:
```
python cli.py list in-progress
```

source: https://roadmap.sh/projects/task-tracker
=======
Task tracker is a project used to track and manage your tasks. It is a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on.
>>>>>>> 1b124b04c0b27e097d96f93dce2e155e0b313abe
