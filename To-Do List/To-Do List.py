tasks = []

while True:
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    action = input("\nAdd, Remove, or Quit? ").lower()
    if action == "add":
        task = input("Enter a task: ")
        tasks.append(task)
    elif action == "remove":
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
        else:
            print("Invalid task number!")
    elif action == "quit":
        break
    else:
        print("Invalid action!")