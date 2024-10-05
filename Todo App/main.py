# create a function to add tasks to the list

def add_task(task_list, task):
    task_list.append(task)
    print(f"Task '{task}' added successfully.")

# create a function to remove tasks from the list

def remove_task(task_list, task):
    if task in task_list:
        task_list.remove(task)
        print(f"Task '{task}' removed successfully.")
    else:
        print(f"Task '{task}' not found in the list.")

# create a function to view all tasks in the list

def view_tasks(task_list):
    if len(task_list) == 0:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task in task_list:
            print(task)

# create a function to mark a task as completed

def mark_completed(task_list, task):
    if task in task_list:
        task_list.remove(task)
        print(f"Task '{task}' marked as completed.")
    else:
        print(f"Task '{task}' not found in the list.")

# create a function to mark all tasks as completed

def mark_all_completed(task_list):
    task_list.clear()
    print("All tasks marked as completed.")

# create a main function to handle user interactions

def main():
    task_list = []

    while True:
        print("\nTodo App")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Mark Task as Completed")
        print("5. Mark All Tasks as Completed")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter the task to add: ")
            add_task(task_list, task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            remove_task(task_list, task)
        elif choice == "3":
            view_tasks(task_list)
        elif choice == "4":
            task = input("Enter the task to mark as completed: ")
            mark_completed(task_list, task)
        elif choice == "5":
            mark_all_completed(task_list)
            continue
        elif choice == "6":
            print("Goodbye!")
            break

main()





