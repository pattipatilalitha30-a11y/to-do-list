#!/usr/bin/env python3
"""
CLI To-Do List Application
Internship Project 7: To-Do List

A clean, modular, beginner-friendly command-line To-Do List application
built with Python standard libraries.
"""

import argparse
import json
import os
import sys

TASKS_FILE = "tasks.json"


def load_tasks(filepath=TASKS_FILE):
    """
    Load tasks from the JSON file.
    Gracefully handles missing, empty, or malformed files.
    """
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                return []
            data = json.loads(content)
            if isinstance(data, list):
                return data
            else:
                print(f"Warning: Expected a list in '{filepath}', but found {type(data).__name__}. Starting with empty tasks.")
                return []
    except (json.JSONDecodeError, OSError) as e:
        print(f"Warning: Could not read or parse '{filepath}' ({e}). Starting with an empty task list.")
        return []


def save_tasks(tasks, filepath=TASKS_FILE):
    """
    Save the list of tasks to the JSON file.
    """
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
    except OSError as e:
        print(f"Error: Unable to save tasks to '{filepath}' ({e}).", file=sys.stderr)


def get_next_id(tasks):
    """
    Generate the next unique integer ID for a new task.
    """
    if not tasks:
        return 1
    existing_ids = [task.get("id", 0) for task in tasks if isinstance(task, dict) and isinstance(task.get("id"), int)]
    return max(existing_ids, default=0) + 1


def add_task(description, filepath=TASKS_FILE):
    """
    Add a new task with unique ID, text, and completed status (False).
    """
    clean_desc = description.strip()
    if not clean_desc:
        print("Error: Task description cannot be empty.")
        return

    tasks = load_tasks(filepath)
    new_id = get_next_id(tasks)

    new_task = {
        "id": new_id,
        "task": clean_desc,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks, filepath)
    print(f'Task added successfully (ID: {new_id}): "{clean_desc}"')


def list_tasks(filepath=TASKS_FILE):
    """
    Display all tasks with their ID, description, and status.
    """
    tasks = load_tasks(filepath)

    if not tasks:
        print("No tasks found. Your to-do list is empty!")
        return

    print("=" * 60)
    print(f"{'ID':<6}{'Status':<14}{'Task Description'}")
    print("-" * 60)

    for item in tasks:
        if not isinstance(item, dict):
            continue
        task_id = item.get("id", "?")
        desc = item.get("task", "(No description)")
        is_completed = item.get("completed", False)

        status_str = "[X] Done" if is_completed else "[ ] Pending"
        print(f"{task_id:<6}{status_str:<14}{desc}")

    print("=" * 60)


def mark_done(task_id, filepath=TASKS_FILE):
    """
    Mark a task as completed by its ID.
    """
    tasks = load_tasks(filepath)

    if not tasks:
        print(f"Error: No tasks available. Task ID {task_id} does not exist.")
        return

    target_task = None
    for task in tasks:
        if isinstance(task, dict) and task.get("id") == task_id:
            target_task = task
            break

    if target_task is None:
        print(f"Error: Task with ID {task_id} not found.")
        return

    if target_task.get("completed") is True:
        print(f"Notice: Task {task_id} (\"{target_task.get('task')}\") is already marked as done.")
        return

    target_task["completed"] = True
    save_tasks(tasks, filepath)
    print(f'Task {task_id} marked as done: "{target_task.get("task")}"')


def create_parser():
    """
    Build and return the argument parser.
    """
    parser = argparse.ArgumentParser(
        prog="python todo.py",
        description="A simple, beginner-friendly CLI To-Do List application."
    )

    subparsers = parser.add_subparsers(
        dest="command",
        title="Commands",
        description="Available operations"
    )

    # Subcommand: add
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="The task description")

    # Subcommand: list
    subparsers.add_parser("list", help="Display all tasks")

    # Subcommand: done
    done_parser = subparsers.add_parser("done", help="Mark a task as completed")
    done_parser.add_argument("id", type=int, help="The ID of the task to mark as done")

    return parser


def main():
    """
    Main entry point of the CLI application.
    """
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        mark_done(args.id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
