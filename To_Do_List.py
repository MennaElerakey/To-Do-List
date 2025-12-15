tasks = []

print("=" * 45)
print("        Simple To-Do List Application")
print("=" * 45)
print("Menu:")
print("1 - Add a new task")
print("2 - View tasks")
print("3 - Mark a task as completed")
print("4 - Exit")

while True:
    choice = input("\nSelect an option (1-4): ").strip()

    if choice == "1":
        task = input("Enter a new task: ").strip()
        if task:
            tasks.append(task)
            print("Task added successfully.")
        else:
            print("Task cannot be empty.")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks available to complete.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_num = input("Enter the task number to mark as completed: ").strip()

            if task_num.isdigit():
                task_index = int(task_num) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index] = "[Completed] " + tasks[task_index]
                    print("Task marked as completed.")
                else:
                    print("Task number is out of range.")
            else:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Exiting the application. Have a productive day!")
        break

    else:
        print("Invalid option. Please choose between 1 and 4.")
