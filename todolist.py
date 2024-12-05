class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.is_completed = False

    def mark_done(self):
        self.is_completed = True

    def __str__(self):
        status = "✓" if self.is_completed else "✗"
        return f"Title: {self.title}, Status: [{status}], Description: {self.description}"


class TodoList:
    def __init__(self):
        self.taskList = []

    def add_task(self, task):
        self.taskList.append(task)

    def mark_task_complete(self, title):
        for task in self.taskList:
            if task.title == title:
                task.mark_done()
                print(f"Task '{title}' marked as complete.")
                return
        print(f"Task '{title}' not found.")

    def display_tasks(self):
        if not self.taskList:
            print("No tasks available.")
            return
        for task in self.taskList:
            print(task)


def main():
    tl = TodoList()
    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter description of task: ")
            tl.add_task(Task(title, description))
            print(f"Task '{title}' added.")

        elif choice == '2':
            title = input("Enter the title of the task to mark as complete: ")
            tl.mark_task_complete(title)

        elif choice == '3':
            print("\nCurrent Tasks:")
            tl.display_tasks()

        elif choice == '4':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid option. Please choose a valid number.")


if __name__ == "__main__":
    main()
