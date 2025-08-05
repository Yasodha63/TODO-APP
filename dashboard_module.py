import tkinter as tk
import json
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def open_dashboard(username):
    tasks = load_tasks().get(username, [])

    def show_all():
        listbox.delete(0, tk.END)
        for task in tasks:
            listbox.insert(tk.END, f"{task['title']} - {task['status']}")

    def show_pending():
        listbox.delete(0, tk.END)
        for task in tasks:
            if task['status'] == "Pending":
                listbox.insert(tk.END, f"{task['title']} - Pending")

    def show_completed():
        listbox.delete(0, tk.END)
        for task in tasks:
            if task['status'] == "Completed":
                listbox.insert(tk.END, f"{task['title']} - Completed")

    window = tk.Tk()
    window.title("Dashboard")

    tk.Label(window, text=f"Welcome, {username}").pack()
    tk.Label(window, text=f"Date: {datetime.now().strftime('%Y-%m-%d')}").pack()

    listbox = tk.Listbox(window, width=50)
    listbox.pack()

    tk.Button(window, text="All Tasks", command=show_all).pack()
    tk.Button(window, text="Pending", command=show_pending).pack()
    tk.Button(window, text="Completed", command=show_completed).pack()

    show_all()
    window.mainloop()
