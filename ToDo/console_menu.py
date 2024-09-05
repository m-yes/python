class ConsoleMenu:
    def __init__(self, task_manager):
        self.task_manager = task_manager

    def show_menu(self):
        while True:
            print("\nTo-Do App Menu:")
            print("1. Add Task")
            print("2. List Tasks")
            print("3. Complete Task")
            print("4. Complete All Tasks")
            print("5. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                task = input("Enter the task: ")
                self.task_manager.add_task(task)
                print(f"Task added: {task}")
            elif choice == '2':
                self.list_tasks()
            elif choice == '3':
                self.remove_task()
            elif choice == '4':
                self.remove_all_tasks()
            elif choice == '5':
                print("Have a productive day! Exiting...")
                break
            else:
                print("Invalid option. Please try again.")

    def list_tasks(self):
        tasks = self.task_manager.get_tasks()
        if not tasks:
            print("No tasks available. Please add tasks.")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    def remove_task(self):
        tasks = self.task_manager.get_tasks()
        if not tasks:
            print("No tasks to complete. Please add tasks.")
            return
        self.list_tasks()
        try:
            task_number = int(input("Enter the task number to complete: "))
            task = tasks[task_number - 1]
            self.task_manager.remove_task(task)
            print(f"Task completed: {task}")
        except (ValueError, IndexError):
            print("Invalid task number.")

    def remove_all_tasks(self):
        tasks = self.task_manager.get_tasks()
        if not tasks:
            print("No tasks to complete. Please add tasks.")
        else:
            confirm = input("Are you sure you want to complete all tasks? (y/n): ")
            if confirm.lower() == 'y':
                self.task_manager.remove_all_tasks()
            else:
                print("Operation canceled.")
