# Simple To-Do List Program

# Initialize an empty list to store tasks
tasks = []

def add_task():
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"'{task}' has been added to your to-do list.")

def view_tasks():
    if tasks:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number you want to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"'{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def insert_task():
    task = input("Enter the task you want to insert: ")
    try:
        position = int(input(f"Enter the position (1 to {len(tasks) + 1}) to insert the task: "))
        if 1 <= position <= len(tasks) + 1:
            tasks.insert(position - 1, task)
            print(f"'{task}' has been inserted at position {position}.")
        else:
            print("Invalid position!")
    except ValueError:
        print("Please enter a valid number.")

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Insert Task")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            insert_task()
        elif choice == '5':
            print("Exiting the To-Do List Program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
