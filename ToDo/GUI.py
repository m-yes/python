import tkinter as tk
from tkinter import messagebox
from menu import Menu

class GUI:
    def __init__(self):
        self.menu = Menu()
        self.root = tk.Tk()
        self.root.geometry("300x550")
        self.root.title("To-Do List")

        self.label = tk.Label(self.root, text="To-Do List: ", font=("Helvetica", 20))
        self.label.pack(padx=12, pady=12)

        self.textbox = tk.Text(self.root, height=5, font=("Helvetica", 16))
        self.textbox.pack()

        self.view_tasks_button = tk.Button(self.root, text="View Tasks", font=("Helvetica", 16), command=self.view_tasks)
        self.view_tasks_button.pack(padx=12, pady=12)

        self.add_task_button = tk.Button(self.root, text="Add Task", font=("Helvetica", 16), command=self.add_task)
        self.add_task_button.pack(padx=12, pady=12)

        self.complete_task_button = tk.Button(self.root, text="Complete Task", font=("Helvetica", 16), command=self.complete_task)
        self.complete_task_button.pack(padx=12, pady=12)

        self.delete_completed_button = tk.Button(self.root, text="Delete Completed Tasks", font=("Helvetica", 16), command=self.delete_completed_tasks)
        self.delete_completed_button.pack(padx=12, pady=12)

        self.exit_button = tk.Button(self.root, text="Exit", font=("Helvetica", 16), command=self.root.quit)
        self.exit_button.pack(padx=12, pady=12)

        self.root.mainloop()

    def view_tasks(self):
        tasks_str = "\n".join(f"{index + 1}. {task}" for index, task in enumerate(self.menu.tasks["tasks"]))
        if tasks_str:
            messagebox.showinfo("Tasks", tasks_str)
        else:
            messagebox.showinfo("Tasks", "No tasks exist")

    def add_task(self):
        task = self.textbox.get("1.0", tk.END).strip()
        if task:
            self.menu.tasks["tasks"].append(task)
            self.menu.save_tasks()
            messagebox.showinfo("Success", f"Task '{task}' has been added")
            self.textbox.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task")

    def complete_task(self):
        task_num = self.get_task_number()
        if task_num is not None:
            completed_task = self.menu.tasks["tasks"].pop(task_num - 1)
            self.menu.tasks["completed"].append(completed_task)
            self.menu.save_tasks()
            messagebox.showinfo("Success", f"Task '{completed_task}' has been completed")

    def delete_completed_tasks(self):
        self.menu.delete_completed_tasks()
        messagebox.showinfo("Success", "All completed tasks have been deleted")

    def get_task_number(self):
        self.view_tasks()
        try:
            task_num = int(self.textbox.get("1.0", tk.END).strip())
            if 1 <= task_num <= len(self.menu.tasks["tasks"]):
                return task_num
            else:
                messagebox.showwarning("Warning", "No such task exists")
                return None
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid number")
            return None
