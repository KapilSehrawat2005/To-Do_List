import pandas as pd
import os

# File to store tasks
task_file = "tasks.csv"

# Function to add a new task
def add_task(description, priority, due_date):
    new_task = {"Description": description, "Priority": priority, "Due Date": due_date, "Completed": False}
    if not os.path.exists(task_file):
        df = pd.DataFrame(columns=["Description", "Priority", "Due Date", "Completed"])
    else:
        df = pd.read_csv(task_file)
    
    df = df.append(new_task, ignore_index=True)
    df.to_csv(task_file, index=False)
    print("Task added successfully!")

# Function to view tasks
def view_tasks(show_completed=False):
    if not os.path.exists(task_file):
        print("No tasks recorded yet.")
        return

    df = pd.read_csv(task_file)
    if not show_completed:
        df = df[df['Completed'] == False]
    
    print(df)

# Function to mark task as complete
def mark_task_complete(task_index):
    if not os.path.exists(task_file):
        print("No tasks recorded yet.")
        return

    df = pd.read_csv(task_file)
    if task_index in df.index:
        df.at[task_index, 'Completed'] = True
        df.to_csv(task_file, index=False)
        print("Task marked as complete!")
    else:
        print("Task not found.")

# Function to delete a task
def delete_task(task_index):
    if not os.path.exists(task_file):
        print("No tasks recorded yet.")
        return

    df = pd.read_csv(task_file)
    if task_index in df.index:
        df = df.drop(task_index)
        df.to_csv(task_file, index=False)
        print("Task deleted!")
    else:
        print("Task not found.")

# Main program loop
def main():
    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter priority (high, medium, low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(description, priority, due_date)
        elif choice == "2":
            view_completed = input("Show completed tasks? (yes/no): ").strip().lower() == 'yes'
            view_tasks(view_completed)
        elif choice == "3":
            task_index = int(input("Enter the task index to mark as complete: "))
            mark_task_complete(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to delete: "))
            delete_task(task_index)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
