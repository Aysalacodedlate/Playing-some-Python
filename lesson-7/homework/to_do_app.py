#I liked the idea of creating an app for to does. 
#Because I personally myself always struggled with finding a proper app for tracking my daily activities
#so, yeyyy

import csv
import json
from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
       
        return {
            "Task ID": self.task_id,
            "Title": self.title,
            "Description": self.description,
            "Due Date": self.due_date,
            "Status": self.status,
        }

    @staticmethod
    def from_dict(data):
    
        return Task(
            task_id=data["Task ID"],
            title=data["Title"],
            description=data["Description"],
            due_date=data.get("Due Date"),
            status=data["Status"],
        )


class FileHandler:

    @staticmethod
    def save_to_json(file_name, tasks):
        
        with open(file_name, "w") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)

    @staticmethod
    def load_from_json(file_name):
        
        tasks = []
        try:
            with open(file_name, "r") as f:
                data = json.load(f)
                for item in data:
                    tasks.append(Task.from_dict(item))
        except FileNotFoundError:
            pass
        return tasks


class ToDoApp:
    def __init__(self, file_name, file_format="csv"):
        self.file_name = file_name
        self.file_format = file_format
        self.tasks = self.load_tasks()

    def save_tasks(self):
        
        if self.file_format == "csv":
            FileHandler.save_to_csv(self.file_name, self.tasks)
        elif self.file_format == "json":
            FileHandler.save_to_json(self.file_name, self.tasks)

    def load_tasks(self):
        
        if self.file_format == "csv":
            return FileHandler.load_from_csv(self.file_name)
        elif self.file_format == "json":
            return FileHandler.load_from_json(self.file_name)
        return []

    def add_task(self):
        
        task_id = input("Enter Task ID: ")
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD) [optional]: ") or None
        status = input("Enter Status (Pending/In Progress/Completed): ")
        new_task = Task(task_id, title, description, due_date, status)
        self.tasks.append(new_task)
        print("Task added successfully!")

    def view_tasks(self):
        
        if not self.tasks:
            print("No tasks available.")
            return
        print("\nTasks:")
        for task in self.tasks:
            print(f"{task.task_id}, {task.title}, {task.description}, {task.due_date}, {task.status}")

if __name__ == "__main__":
    file_format = input("Enter file format (csv/json): ").strip().lower()
    file_name = "tasks." + file_format
    app = ToDoApp(file_name, file_format)
    app.menu()


#brain is not braining, 

