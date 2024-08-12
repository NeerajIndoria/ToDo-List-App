class Task:
    def __init__(self, title, due_date, status="ToDo"):
        self.title = title
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.title} | {self.due_date} | {self.status}"
