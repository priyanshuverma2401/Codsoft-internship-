import os
import json
import time
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    else:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    time.sleep(5)

def add_task(tasks, new_task):
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{new_task}' added successfully.")
    time.sleep(2)

def remove_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task}' removed successfully.")
    else:
        print("Invalid task index.")
    time.sleep(2)

def update_task(tasks, task_index, new_task):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1] = new_task
        save_tasks(tasks)
        print(f"Task updated successfully.")
        time.sleep(2)
    else:
        print("Invalid task index.")
        time.sleep(2)

def main():
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List =====")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. update task")
        print("5. exit")
        time.sleep(3)
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == "3":
            task_index = int(input("Enter the task index to remove: "))
            remove_task(tasks, task_index)
        elif choice=="4":

            task_index = int(input("Enter the task index to update: "))
            new_task = input("Enter the new task: ")
            update_task(tasks, task_index, new_task)
        elif choice == "5":
            print("Exiting the To-Do List application.")
            time.sleep(2)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            time.sleep(2)

if __name__ == "__main__":
    main()
