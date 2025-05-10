def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        f.write("\n".join(tasks))

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            idx = int(input("Enter task number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                save_tasks(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
