import tkinter as tk
from Interface import TodoApp


# class Task:
#     def __init__(self, title, due_date, status="ToDo"):
#         self.title = title
#         self.due_date = due_date
#         self.status = status
#
#     def __str__(self):
#         return f"{self.title} | {self.due_date} | {self.status}"


# class TodoApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("ToDo List App")
#
#         self.tasks = []
#
#         # Create GUI elements
#         self.create_widgets()
#
#     def create_widgets(self):
#         # Title Entry
#         self.title_label = tk.Label(self.root, text="Task Title:")
#         self.title_label.grid(row=0, column=0, padx=10, pady=5)
#         self.title_entry = tk.Entry(self.root, width=40)
#         self.title_entry.grid(row=0, column=1, padx=10, pady=5)
#
#         # Due Date Entry
#         self.due_date_label = tk.Label(self.root, text="Due Date (YYYY-MM-DD):")
#         self.due_date_label.grid(row=1, column=0, padx=10, pady=5)
#         self.due_date_entry = tk.Entry(self.root, width=40)
#         self.due_date_entry.grid(row=1, column=1, padx=10, pady=5)
#
#         # Status Dropdown
#         self.status_label = tk.Label(self.root, text="Status:")
#         self.status_label.grid(row=2, column=0, padx=10, pady=5)
#         self.status_combobox = ttk.Combobox(self.root, values=["ToDo", "In progress", "Done"])
#         self.status_combobox.current(0)
#         self.status_combobox.grid(row=2, column=1, padx=10, pady=5)
#
#         # Add Task Button
#         self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
#         self.add_task_button.grid(row=3, column=0, columnspan=2, pady=10)
#
#         # Task Listbox
#         self.task_listbox = tk.Listbox(self.root, width=80, height=15)
#         self.task_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
#
#         # Delete Task Button
#         self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
#         self.delete_task_button.grid(row=5, column=0, columnspan=2, pady=10)
#
#         # Search Entry
#         self.search_label = tk.Label(self.root, text="Search Task:")
#         self.search_label.grid(row=6, column=0, padx=10, pady=5)
#         self.search_entry = tk.Entry(self.root, width=40)
#         self.search_entry.grid(row=6, column=1, padx=10, pady=5)
#
#         # Search Button
#         self.search_button = tk.Button(self.root, text="Search", command=self.search_task)
#         self.search_button.grid(row=7, column=0, columnspan=2, pady=10)
#
#     def add_task(self):
#         title = self.title_entry.get()
#         due_date = self.due_date_entry.get()
#         status = self.status_combobox.get()
#
#         try:
#             # Validate date
#             datetime.strptime(due_date, "%Y-%m-%d")
#             task = Task(title, due_date, status)
#             self.tasks.append(task)
#             self.update_task_listbox()
#             self.clear_entries()
#         except ValueError:
#             messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format.")
#
#     def delete_task(self):
#         selected_task_index = self.task_listbox.curselection()
#         if selected_task_index:
#             self.tasks.pop(selected_task_index[0])
#             self.update_task_listbox()
#         else:
#             messagebox.showwarning("No Selection", "Please select a task to delete.")
#
#     def update_task_listbox(self):
#         self.task_listbox.delete(0, tk.END)
#         for task in self.tasks:
#             self.task_listbox.insert(tk.END, str(task))
#
#     def clear_entries(self):
#         self.title_entry.delete(0, tk.END)
#         self.due_date_entry.delete(0, tk.END)
#         self.status_combobox.current(0)
#
#     def search_task(self):
#         search_term = self.search_entry.get().lower()
#         self.task_listbox.delete(0, tk.END)
#
#         for task in self.tasks:
#             if search_term in task.title.lower() or search_term in task.status.lower():
#                 self.task_listbox.insert(tk.END, str(task))
#             try:
#                 search_date = datetime.strptime(search_term, "%Y-%m-%d").date()
#                 if datetime.strptime(task.due_date, "%Y-%m-%d").date() == search_date:
#                     self.task_listbox.insert(tk.END, str(task))
#             except ValueError:
#                 pass


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
