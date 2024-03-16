class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully!")
    
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed successfully")
        else:
            print(f"Task '{task}' not found")

    def view_tasks(self):
        if self.tasks:
            print("Your tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks found!")

def main():
    todo_list = TodoList()

    while True:
        print("\nChoose an option:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. View tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Exiting....")
            exit()
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
