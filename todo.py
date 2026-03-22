FILE_NAME = "tasks.txt"

def load_tasks():
    """Load tasks from file"""
    tasks = []
    try:
        with open(FILE_NAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    """Save tasks to file"""
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Display all tasks"""
    if not tasks:
        print("\n📭 No tasks available\n")
    else:
        print("\n📌 Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()

def add_task(tasks):
    """Add a new task"""
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        print("✅ Task added\n")
    else:
        print("⚠️ Task cannot be empty\n")

def delete_task(tasks):
    """Delete a task"""
    show_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"🗑️ Removed: {removed}\n")
        else:
            print("❌ Invalid task number\n")
    except ValueError:
        print("⚠️ Please enter a valid number\n")

def main():
    tasks = load_tasks()

    while True:
        print("===== 📝 TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("💾 Tasks saved. Exiting... Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
