
tasks = []


def add_task(task):
    tasks.append(task)
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def update_task(task_index, new_task):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task index.")


def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Task '{deleted_task}' deleted successfully!")
    else:
        print("Invalid task index.")


while True:
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()
        task_index = int(input("Enter the task number to update: "))
        new_task = input("Enter the new task: ")
        update_task(task_index, new_task)
    elif choice == '4':
        view_tasks()
        task_index = int(input("Enter the task number to delete: "))
        delete_task(task_index)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
