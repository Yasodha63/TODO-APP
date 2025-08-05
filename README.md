# 📝 To-Do List Application (Python + Tkinter + MongoDB)

This project is a **desktop To-Do List Application** developed in **Python** using **Tkinter** for the user interface and **MongoDB** as the backend database. It provides user authentication and an intuitive way to track and manage tasks efficiently.

---

## 🌟 Features

✅ **User Authentication**
- Register a new account
- Login with existing credentials
- Forgot Password functionality to reset your password securely

✅ **Task Management**
- Create new tasks with descriptions
- Mark tasks as complete or incomplete
- Edit and delete tasks
- View tasks by date

✅ **Dashboard**
- Overview of all tasks
- Visual summary of completed vs. pending tasks
- Date-wise and user-specific breakdown

✅ **Database Integration**
- All user and task data are stored in MongoDB
- Secure password handling

---
odo_app/
│
├── app.py
│ Main entry point. Launches the login window.
│
├── auth_window.py
│ Handles user login, registration, and password reset.
│
├── todo_window.py
│ Main interface for adding, editing, completing, and deleting tasks.
│
├── dashboard_window.py
│ Shows task statistics and summary.
│
└── db_connect.py
MongoDB connection settings.

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Yasodha63/TODO-APP.git
cd TODO-APP
2️⃣ Install Dependencies
Make sure you have Python 3 installed, then run:

bash
Copy code
pip install pymongo
3️⃣ Configure MongoDB
Create a MongoDB Atlas cluster or use a local MongoDB server.

In db_connect.py, set your connection string:

python
Copy code
client = pymongo.MongoClient("mongodb://localhost:27017/")
Or for Atlas:

python
Copy code
client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/")
4️⃣ Run the Application
Launch the app with:

bash
Copy code
python app.py

🛠️ Technologies Used
Language: Python 3

GUI: Tkinter

Database: MongoDB (pymongo library)
