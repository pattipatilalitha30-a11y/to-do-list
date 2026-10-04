# Project 7: Python CLI To-Do List Application

A clean, modular, and beginner-friendly Command-Line Interface (CLI) To-Do List application built entirely in Python using standard library modules.

---

## Table of Contents
- [Project Title](#project-7-python-cli-to-do-list-application)
- [Description](#description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Commands and Usage Examples](#commands-and-usage-examples)
- [JSON Storage Explanation](#json-storage-explanation)
- [Example Output](#example-output)
- [Error Handling](#error-handling)

---

## Description
This project is an internship command-line task manager designed to help users track their daily tasks efficiently from the terminal. All tasks are persisted locally in a structured JSON file (`tasks.json`). The code emphasizes modular architecture, robust error handling, clean formatting, and zero external dependencies.

---

## Features
- **Add Tasks**: Add tasks with an auto-incremented unique ID and default status of pending (`False`).
- **List Tasks**: View all tasks in a formatted table showing ID, status, and task description.
- **Mark as Done**: Mark existing tasks as completed using their unique ID.
- **Data Persistence**: Tasks are saved to `tasks.json` automatically after every change and loaded on startup.
- **Resilient & Fault-Tolerant**: Safely handles missing, empty, or corrupted JSON files without crashing.
- **Graceful Error Reporting**: Informative, user-friendly messages for invalid IDs, duplicate operations, and invalid inputs.
- **Zero Dependencies**: Uses only standard Python modules.

---

## Technologies Used
- **Language**: Python 3 (compatible with Python 3.7+)
- **Standard Library Modules**:
  - `argparse` - Command-line parsing, subcommands, and flags
  - `json` - Serialization and deserialization of task data
  - `os` - File system operations and path existence verification
  - `sys` - Standard error reporting and system hooks

---

## Installation

1. **Clone or navigate** to the project directory:
   ```bash
   cd "to do list"
   ```

2. **Verify Python is installed**:
   ```bash
   python --version
   ```
   *(Requires Python 3.7 or higher)*

3. **Check Dependencies**:
   No external packages or `pip install` commands are needed because this project relies solely on the Python Standard Library. See `requirements.txt`.

---

## How to Run

Run the script using Python through your terminal or command prompt:

```bash
python todo.py <command> [arguments]
```

To view built-in command help:
```bash
python todo.py --help
```

---

## Commands and Usage Examples

### 1. Add a Task (`add`)
Adds a new task to your list.
```bash
python todo.py add "Buy milk"
python todo.py add "Complete Project 7"
```

### 2. List All Tasks (`list`)
Displays all saved tasks in a formatted table.
```bash
python todo.py list
```

### 3. Mark a Task as Completed (`done`)
Marks the task with the given numeric ID as done.
```bash
python todo.py done 1
```

---

## JSON Storage Explanation

Tasks are stored in `tasks.json` in the root project directory. Each task is a JSON object with three fields:
- `id` (`int`): Unique integer identifier for the task.
- `task` (`string`): The description of the task.
- `completed` (`boolean`): Completion status (`false` for pending, `true` for done).

### Sample `tasks.json`:
```json
[
    {
        "id": 1,
        "task": "Buy milk",
        "completed": true
    },
    {
        "id": 2,
        "task": "Complete Project 7",
        "completed": false
    }
]
```

---

## Example Output

### Adding tasks:
```text
$ python todo.py add "Buy milk"
Task added successfully (ID: 1): "Buy milk"

$ python todo.py add "Complete Project 7"
Task added successfully (ID: 2): "Complete Project 7"
```

### Listing tasks:
```text
$ python todo.py list
============================================================
ID    Status        Task Description
------------------------------------------------------------
1     [ ] Pending   Buy milk
2     [ ] Pending   Complete Project 7
============================================================
```

### Marking a task as done:
```text
$ python todo.py done 1
Task 1 marked as done: "Buy milk"
```

### Listing tasks after completion:
```text
$ python todo.py list
============================================================
ID    Status        Task Description
------------------------------------------------------------
1     [X] Done      Buy milk
2     [ ] Pending   Complete Project 7
============================================================
```

---

## Error Handling

The application handles edge cases and common user errors gracefully:
1. **Missing `tasks.json`**:
   - If the file does not exist, the app initializes an empty task list without throwing `FileNotFoundError`. The file is created automatically on the first `add` operation.
2. **Empty or Malformed `tasks.json`**:
   - If `tasks.json` is empty (0 bytes) or corrupted with invalid JSON syntax, a friendly warning is displayed, and the app safely defaults to an empty task list without crashing.
3. **Invalid Task ID (Non-existent)**:
   - When attempting to mark an ID that does not exist (e.g., `python todo.py done 999`), an error message is shown: `Error: Task with ID 999 not found.`
4. **Already Completed Task**:
   - If a task is already marked done, it informs the user: `Notice: Task 1 ("Buy milk") is already marked as done.`
5. **Invalid Command / Missing Arguments**:
   - Executing without arguments or with invalid commands displays clear help usage generated by `argparse`.
6. **Non-numeric ID**:
   - Passing an invalid type such as `python todo.py done abc` results in an informative validation error from `argparse`.
7. **Empty Task Description**:
   - Attempting to add an empty task (`python todo.py add "   "`) outputs `Error: Task description cannot be empty.`
