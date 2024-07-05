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
    print("5. Exit")


# Read file and load any existing tasks
def load_tasks():
    if os.path.exists(TasksFile):
        with open(TasksFile, 'r') as file:
            return json.load(file)
    return []


def save_tasks():
    with open(TasksFile, 'w') as file:
        json.dump(tasks, file)

def view_tasks(tasks):


def add_task(tasks):


def delete_task(tasks):


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
