import json
import os
import datetime

# File to store to-do tasks
TasksFile = "tasks.json"
today = datetime.date.today()

class Menu:
    def __init__(self):
        self.tasks = self.load_tasks()

    def display_menu(self):
        print("\nTo-Do List App:")
        print(f"\n{today}\n")
        print("1. View tasks")
        print("2. Add new task")
        print("3. Complete task")
        print("4. View completed tasks")
        print("5. Delete all completed tasks")
        print("6. Exit")

    def load_tasks(self):
        if os.path.exists(TasksFile):
            with open(TasksFile, 'r') as file:
                return json.load(file)
        return {"tasks": [], "completed": []}

    def save_tasks(self):
        with open(TasksFile, 'w') as file:
            json.dump(self.tasks, file)

    def view_tasks(self):
        if not self.tasks["tasks"]:
            print("You don't have any tasks")
        else:
            for index, task in enumerate(self.tasks["tasks"], 1):
                print(f"{index}. {task}")

    def view_completed_tasks(self):
        if not self.tasks["completed"]:
            print("You have no completed tasks")
        else:
            print("You have completed all your tasks:")
            for index, task in enumerate(self.tasks["completed"], 1):
                print(f"{index}. {task}")

    def add_task(self):
        task = input("Please enter task to add: ")
        self.tasks["tasks"].append(task)
        self.save_tasks()
        print(f"Task '{task}' has been added")

    def complete_task(self):
        self.view_tasks()
        if self.tasks["tasks"]:
            try:
                task_num = int(input("Enter the task number to mark as complete: "))
                if 1 <= task_num <= len(self.tasks["tasks"]):
                    completed_task = self.tasks["tasks"].pop(task_num - 1)
                    self.tasks["completed"].append(completed_task)
                    self.save_tasks()
                    print(f"Task '{completed_task}' has been completed")
                else:
                    print("No such task exists. Please enter a valid task number")
            except ValueError:
                print("Please enter a valid number.")

    def delete_completed_tasks(self):
        self.tasks["completed"].clear()
        self.save_tasks()
        print("All completed tasks have been deleted")
