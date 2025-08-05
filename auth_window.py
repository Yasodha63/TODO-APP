import tkinter as tk
from tkinter import messagebox, simpledialog
from db_connect import get_db
from todo_window import open_todo_window

db = get_db()
users_collection = db["users"]

def register_user(username, password):
    if users_collection.find_one({"username": username}):
        messagebox.showerror("Error", "Username already exists!")
    else:
        users_collection.insert_one({"username": username, "password": password})
        messagebox.showinfo("Success", "Registration Successful!")

def reset_password(username):
    user = users_collection.find_one({"username": username})
    if user:
        new_password = simpledialog.askstring("Reset Password", "Enter new password:", show="*")
        if new_password:
            users_collection.update_one({"username": username}, {"$set": {"password": new_password}})
            messagebox.showinfo("Success", "Password has been reset successfully!")
        else:
            messagebox.showwarning("Cancelled", "Password reset cancelled.")
    else:
        messagebox.showerror("Error", "User not found!")

def login_screen():
    root = tk.Tk()
    root.title("Login")

    tk.Label(root, text="Username").grid(row=0)
    tk.Label(root, text="Password").grid(row=1)

    username_entry = tk.Entry(root)
    password_entry = tk.Entry(root, show="*")
    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)

    def login():
        username = username_entry.get()
        password = password_entry.get()
        user = users_collection.find_one({"username": username, "password": password})
        if user:
            root.destroy()
            open_todo_window(username)
        else:
            messagebox.showerror("Error", "Invalid Credentials!")

    def register():
        register_user(username_entry.get(), password_entry.get())

    def forgot():
        reset_password(username_entry.get())

    tk.Button(root, text="Login", command=login).grid(row=3, column=0)
    tk.Button(root, text="Register", command=register).grid(row=3, column=1)
    tk.Button(root, text="Forgot Password", command=forgot).grid(row=3, column=2)

    root.mainloop()
