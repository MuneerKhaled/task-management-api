from datetime import datetime


# =========================
# Task Model
# =========================

class Task:
    def __init__(self, task_id, title, description, priority="medium"):
        self.id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now()

    def complete_task(self):
        self.completed = True

    def update_task(self, title=None, description=None, priority=None):
        if title:
            self.title = title

        if description:
            self.description = description

        if priority:
            self.priority = priority

    def display(self):
        status = "Completed" if self.completed else "Pending"

        print(f"\nTask ID: {self.id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Priority: {self.priority}")
        print(f"Status: {status}")
        print(f"Created: {self.created_at}")


# =========================
# Task Manager
# =========================

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, title, description, priority="medium"):
        task = Task(
            self.next_id,
            title,
            description,
            priority
        )

        self.tasks.append(task)
        self.next_id += 1

        print("\nTask created successfully!")
        return task

    def get_all_tasks(self):
        if not self.tasks:
            print("\nNo tasks found.")
            return

        print("\n========== ALL TASKS ==========")

        for task in self.tasks:
            task.display()

    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task

        return None

    def complete_task(self, task_id):
        task = self.get_task(task_id)

        if task is None:
            print("\nTask not found.")
            return

        task.complete_task()

        print(f"\nTask {task_id} completed successfully!")

    def update_task(
        self,
        task_id,
        title=None,
        description=None,
        priority=None
    ):
        task = self.get_task(task_id)

        if task is None:
            print("\nTask not found.")
            return

        task.update_task(
            title,
            description,
            priority
        )

        print(f"\nTask {task_id} updated successfully!")

    def delete_task(self, task_id):
        task = self.get_task(task_id)

        if task is None:
            print("\nTask not found.")
            return

        self.tasks.remove(task)

        print(f"\nTask {task_id} deleted successfully!")

    def search_tasks(self, keyword):
        results = []

        for task in self.tasks:
            if keyword.lower() in task.title.lower():
                results.append(task)

        if not results:
            print("\nNo matching tasks found.")
            return

        print("\n========== SEARCH RESULTS ==========")

        for task in results:
            task.display()

    def get_completed_tasks(self):
        completed = [
            task for task in self.tasks
            if task.completed
        ]

        if not completed:
            print("\nNo completed tasks.")
            return

        print("\n========== COMPLETED TASKS ==========")

        for task in completed:
            task.display()

    def get_pending_tasks(self):
        pending = [
            task for task in self.tasks
            if not task.completed
        ]

        if not pending:
            print("\nNo pending tasks.")
            return

        print("\n========== PENDING TASKS ==========")

        for task in pending:
            task.display()


# =========================
# Application
# =========================

def show_menu():
    print("\n")
    print("================================")
    print("       TASK MANAGEMENT APP")
    print("================================")
    print("1. Create task")
    print("2. Show all tasks")
    print("3. Complete task")
    print("4. Update task")
    print("5. Delete task")
    print("6. Search task")
    print("7. Show completed tasks")
    print("8. Show pending tasks")
    print("9. Exit")
    print("================================")


def main():
    manager = TaskManager()

    # Example tasks
    manager.create_task(
        "Learn Python",
        "Study Python classes and objects",
        "high"
    )

    manager.create_task(
        "Learn Git",
        "Practice Git commands",
        "medium"
    )

    manager.create_task(
        "Build API",
        "Create a backend REST API",
        "high"
    )

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter description: ")
            priority = input(
                "Enter priority (low/medium/high): "
            )

            manager.create_task(
                title,
                description,
                priority
            )

        elif choice == "2":
            manager.get_all_tasks()

        elif choice == "3":
            task_id = int(
                input("Enter task ID: ")
            )

            manager.complete_task(task_id)

        elif choice == "4":
            task_id = int(
                input("Enter task ID: ")
            )

            title = input(
                "Enter new title: "
            )

            description = input(
                "Enter new description: "
            )

            priority = input(
                "Enter new priority: "
            )

            manager.update_task(
                task_id,
                title,
                description,
                priority
            )

        elif choice == "5":
            task_id = int(
                input("Enter task ID: ")
            )

            manager.delete_task(task_id)

        elif choice == "6":
            keyword = input(
                "Enter search keyword: "
            )

            manager.search_tasks(keyword)

        elif choice == "7":
            manager.get_completed_tasks()

        elif choice == "8":
            manager.get_pending_tasks()

        elif choice == "9":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice.")


# =========================
# Start Application
# =========================

if __name__ == "__main__":
    main()