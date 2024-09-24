# List to store tasks
tasks = []

# Function to add a task
def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "status": "pending"})  # Mark tasks as 'pending' by default
    print(f"'{task}' has been added.")

# Function to display all tasks
def display_tasks():
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("Your to-do list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['task']} - {task['status']}")  # Include task status

# Function to remove a task by index or task name
def remove_task():
    if not tasks:
        print("No tasks to remove!")
        return
    
    try:
        display_tasks()  # Show the current list before asking for input
        choice = input("Remove by (N)umber or (T)ask name? ").lower()
        if choice == 'n':
            index = int(input("Enter the task number to remove: ")) - 1
            removed_task = tasks.pop(index)
            print(f"Removed task: '{removed_task['task']}'")
        elif choice == 't':
            task_name = input("Enter the task name to remove: ")
            for task in tasks:
                if task["task"].lower() == task_name.lower():
                    tasks.remove(task)
                    print(f"Removed task: '{task_name}'")
                    break
            else:
                print(f"Task '{task_name}' not found.")
        else:
            print("Invalid option.")
    except (ValueError, IndexError):
        print("Invalid input or task number out of range.")

#  Function to mark tasks as completed/pending
def update_task_status():
    if not tasks:
        print("No tasks to update!")
        return
    
    display_tasks()
    try:
        index = int(input("Enter the task number to update: ")) - 1
        new_status = input("Enter new status (completed/pending): ").lower()
        if new_status in ["completed", "pending"]:
            tasks[index]['status'] = new_status
            print(f"Task '{tasks[index]['task']}' marked as {new_status}.")
        else:
            print("Invalid status. Please enter 'completed' or 'pending'.")
    except (ValueError, IndexError):
        print("Invalid input or task number out of range.")

# Main program loop
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Remove Task")
        print("4. Update Task Status (Optional)")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            update_task_status()
        elif choice == '5':
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice, please select a valid option.")

# Run the application
if __name__ == "__main__":
    main()
