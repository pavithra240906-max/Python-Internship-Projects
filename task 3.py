tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, task)

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, task)
            try:
                num = int(input("Enter task number to delete: "))
                tasks.pop(num - 1)
                print("Task deleted!")
            except:
                print("Invalid number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")