# To Do List Application


import json
import os
import tkinter as tk
from tkinter import messagebox
import setuptools

# File to store to do tasks
TasksFile = "tasks.json"


# Main menu
def display_menu():
    print("\nTo-Do List App:")
    print("1. View tasks")
    print("2. Add new task")
    print("3. Complete task")
    print("4. View completed tasks")
    print("5. Delete all completed task")
    print("6. Exit")


# Read file and load any existing tasks
def load_tasks():
    if os.path.exists(TasksFile):
        with open(TasksFile, 'r') as file:
            return json.load(file)
    return {"tasks": [], "completed": []}


def save_tasks(tasks):
    with open(TasksFile, 'w') as file:
        json.dump(tasks, file)


def view_tasks(tasks):
    if not tasks["tasks"]:
        print("No tasks exist")
    else:
        for index, task in enumerate(tasks["tasks"], 1):
            print(f"{index}. {task}")


def view_completed_tasks(tasks):
    if not tasks["completed"]:
        print("No completed tasks")
    else:
        print("Completed Tasks:")
        for index, task in enumerate(tasks["completed"], 1):
            print(f"{index}. {task}")


def add_task(tasks):
    task = input("Enter task: ")
    # Append to "tasks" list within the dict
    tasks["tasks"].append(task)
    save_tasks(tasks)
    print(f"Task '{task}' has been added")


# This marks a task as "completed" by moving it to the "completed" list
def complete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter task number to complete: "))
            if 1 <= task_num <= len(tasks):
                completed_task = tasks["tasks"].pop(task_num - 1)
                # Append to "completed" list within the dict
                tasks["completed"].append(completed_task)
                save_tasks(tasks)
                print(f"Task '{completed_task}' has been completed")
            else:
                print("No such task exists")
        except ValueError:
            print("Please enter a valid number.")


# This deletes all tasks that have been marked completed
def delete_completed_tasks(tasks):
    tasks["completed"].clear()
    save_tasks(tasks)
    print("All completed tasks have been deleted")


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
                complete_task(tasks)
            elif choice == 4:
                view_completed_tasks(tasks)
            elif choice == 5:
                delete_completed_tasks(tasks)
            elif choice == 6:
                print("Have a productive day!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")


# GUI interface
class GUI:

    def __init__(self):

        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="To-Do List", font=("Helvetica", 20))
        self.label.pack(padx=12, pady=12)

        self.textbox = tk.Text(self.root, height=5, font=("Helvetica", 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack()

        self.check_state = tk.IntVar()

        self.check_button = tk.Checkbutton(self.root, text="View Tasks", font=("Heltecia", 16), variable=self.check_state)
        self.check_button.pack()

        self.button = tk.Button(self.root, text="View Tasks", font=("Helvetica", 16))
        self.button.pack(padx=12, pady=12)

        self.root.mainloop()


    def shortcut(self, event):
        pass


    def view_tasks_button(self):
        if self.check_state.get() == 0:
            print(self.textbox.get("1.0", tk.END))
        else:
            messagebox.showinfo(title="Task", message=self.textbox.get("1.0", tk.END))


# GUI interface for app
root = tk.Tk()


root.geometry("300x300")
root.title("To-Do List")


label = tk.Label(root, text="To-Do List", font=("Helvetica", 18))
label.pack()


textbox = tk.Text(root, font=("Helvetica", 16), height=5, width=50)
textbox.pack(padx=10)


# Press button to display menu
button = tk.Button(root, text="Show Menu", command=display_menu)
button.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.rowconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.rowconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.rowconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=("Helvetica", 18))
# Sticky to stretch the buttons across the whole row
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="2", font=("Helvetica", 18))
# Sticky to stretch the buttons across the whole row
btn1.grid(row=1, column=0, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonframe, text="3", font=("Helvetica", 18))
# Sticky to stretch the buttons across the whole row
btn1.grid(row=2, column=0, sticky=tk.W+tk.E)


# Stretch into x-axis
buttonframe.pack(fill='x')


# Run GUI
root.mainloop()


# Main function
if __name__ == "__main__":
    main()
