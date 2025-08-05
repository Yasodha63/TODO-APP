import tkinter as tk
from tkinter import messagebox
from db_connect import get_db

def forgot_password_window():
    def reset_password():
        username = entry_username.get()
        new_password = entry_new_password.get()

        db = get_db()
        user = db.users.find_one({"username": username})
        if user:
            db.users.update_one({"username": username}, {"$set": {"password": new_password}})
            messagebox.showinfo("Success", "Password reset successfully!")
            window.destroy()
        else:
            messagebox.showerror("Error", "Username not found")

    window = tk.Tk()
    window.title("Forgot Password")

    tk.Label(window, text="Username").grid(row=0, column=0, pady=5)
    entry_username = tk.Entry(window)
    entry_username.grid(row=0, column=1, pady=5)

    tk.Label(window, text="New Password").grid(row=1, column=0, pady=5)
    entry_new_password = tk.Entry(window, show="*")
    entry_new_password.grid(row=1, column=1, pady=5)

    tk.Button(window, text="Reset Password", command=reset_password).grid(row=2, columnspan=2, pady=10)

    window.mainloop()
