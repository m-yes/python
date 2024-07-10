# To Do List Application

import json
import os

# File to store to do tasks
TasksFile = "tasks.json"


def display_menu():
    print("\nTo-Do List App:")
    print("1. View tasks")
    print("2. New task")
    print("3. Completed tasks")
    print("4. Exit")


# Read file and load any existing tasks
def load_tasks():
    if os.path.exists(TasksFile):
        with open(TasksFile, 'r') as file:
            return json.load(file)
    return []


def load_tasks():
    if os.path.exists(TasksFile):
        with open(TasksFile, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TasksFile, 'w') as file:
        json.dump(tasks, file)

def view_tasks(tasks):
    if not tasks:
        print("No tasks exist")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' has been added")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                save_tasks(tasks)
                print(f"Task '{removed_task}' has been deleted")
            else:
                print("No such task exists")
        except ValueError:
            print("Please enter a valid number.")

# Main function to run the app
def main():
    tasks = load_tasks()

    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                view_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                delete_task(tasks)
            elif choice == 4:
                print("Exiting the app. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
