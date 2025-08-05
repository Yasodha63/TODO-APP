from pymongo import MongoClient
from datetime import datetime

# Replace with your own MongoDB URI (MongoDB Atlas or localhost)
MONGO_URI = "mongodb://localhost:27017"  # or use Atlas URI

client = MongoClient(MONGO_URI)
db = client["todo_app"]

users_col = db["users"]
tasks_col = db["tasks"]

def add_user(username, password):
    if users_col.find_one({"username": username}):
        return False
    users_col.insert_one({"username": username, "password": password})
    return True

def authenticate_user(username, password):
    return users_col.find_one({"username": username, "password": password}) is not None

def get_tasks(username):
    return list(tasks_col.find({"username": username}))

def add_task(username, title):
    task = {
        "username": username,
        "title": title,
        "status": "Pending",
        "date_created": datetime.now().strftime("%Y-%m-%d")
    }
    tasks_col.insert_one(task)

def update_task_status(task_id, status):
    tasks_col.update_one({"_id": task_id}, {"$set": {"status": status}})

def delete_task(task_id):
    tasks_col.delete_one({"_id": task_id})
