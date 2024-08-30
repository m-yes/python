# main.py
from console_menu import ConsoleMenu
from task_manager import TaskManager

def main():
    task_manager = TaskManager()
    console_menu = ConsoleMenu(task_manager)
    console_menu.show_menu()

if __name__ == "__main__":
    main()
