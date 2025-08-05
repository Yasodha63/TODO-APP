import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from db_connect import get_db

db = get_db()
tasks_collection = db["tasks"]

def open_todo_window(username):
    window = tk.Tk()
    window.title(f"{username}'s To-Do List")

    task_entry = tk.Entry(window, width=40)
    task_entry.grid(row=0, column=0, padx=10, pady=10)

    def refresh_tasks():
        listbox.delete(0, tk.END)
        for task in tasks_collection.find({"username": username}):
            status = f"[{task['status']}]"
            listbox.insert(tk.END, f"{task['title']} {status}")

    def add_task():
        title = task_entry.get()
        if title:
            tasks_collection.insert_one({
                "username": username,
                "title": title,
                "status": "Pending",
                "date_created": datetime.now().strftime("%Y-%m-%d")
            })
            task_entry.delete(0, tk.END)
            refresh_tasks()

    def mark_done():
        selection = listbox.curselection()
        if selection:
            title = listbox.get(selection[0]).split(" [")[0]
            tasks_collection.update_one(
                {"username": username, "title": title},
                {"$set": {"status": "Completed"}}
            )
            refresh_tasks()

    def delete_task():
        selection = listbox.curselection()
        if selection:
            title = listbox.get(selection[0]).split(" [")[0]
            tasks_collection.delete_one({"username": username, "title": title})
            refresh_tasks()

    def open_dashboard():
        dashboard = tk.Toplevel(window)
        dashboard.title("Dashboard")

        all_tasks = list(tasks_collection.find({"username": username}))
        pending = [t for t in all_tasks if t["status"] == "Pending"]
        completed = [t for t in all_tasks if t["status"] == "Completed"]

        tk.Label(dashboard, text=f"Total Tasks: {len(all_tasks)}").pack()
        tk.Label(dashboard, text=f"Pending: {len(pending)}").pack()
        tk.Label(dashboard, text=f"Completed: {len(completed)}").pack()

        tk.Label(dashboard, text="Date-wise Summary:").pack()
        summary = {}
        for t in all_tasks:
            date = t['date_created']
            summary[date] = summary.get(date, 0) + 1

        for date, count in summary.items():
            tk.Label(dashboard, text=f"{date}: {count} tasks").pack()

    listbox = tk.Listbox(window, width=50)
    listbox.grid(row=1, column=0, columnspan=3)

    tk.Button(window, text="Add Task", command=add_task).grid(row=0, column=1)
    tk.Button(window, text="Mark Done", command=mark_done).grid(row=2, column=0)
    tk.Button(window, text="Delete Task", command=delete_task).grid(row=2, column=1)
    tk.Button(window, text="Dashboard", command=open_dashboard).grid(row=2, column=2)

    refresh_tasks()
    window.mainloop()
