from GUI import GUI
from menu import Menu

def main():
    menu = GUI()
    # menu = Menu()  # Uncomment to use the console version

    '''
    while True:
        menu.display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                print(menu.view_tasks())
            elif choice == 2:
                task = input("Enter task: ")
                menu.add_task(task)
            elif choice == 3:
                task_num = int(input("Enter task number to complete: "))
                menu.complete_task(task_num)
            elif choice == 4:
                print(menu.view_completed_tasks())
            elif choice == 5:
                menu.delete_completed_tasks()
            elif choice == 6:
                print("Have a productive day!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 6.")
        except ValueError:
            print("Please enter a valid number.")
    '''

if __name__ == "__main__":
    main()
