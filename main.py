# main.py

import os
import json

PATH = "task.json"
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Add successfully")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Remove successfully")

        else:
            print("Task Not Found")

    def view_all_task(self):
        if not self.tasks:
            print("\nNo Task Available\n")
            
        else:
            for i, task in enumerate(self.tasks, start = 1):
                print("\nALL TASK\n"
                      f"{i}. {task}")


Todo = TodoList()

while True:
    choice = input(
        "\n OPTIONS \n"
        "1. Add Task\n"
        "2. Remove Task\n"
        "3. View All Task\n"
        "4. Exit program\n"
        "Enter your Choice: ")
    
    if choice == '1':
        task = input("Enter Task: ")
        Todo.add_task(task)

    elif choice == '2':
        task == input("Enter task: ")
        Todo.remove_task(task)

    elif choice == '3':
        Todo.view_all_task()

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid Choice...")
