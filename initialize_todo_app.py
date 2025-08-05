from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId

# MongoDB connection string
# Replace with your MongoDB Atlas URI if needed
client = MongoClient("mongodb://localhost:27017")

# Step 1: Create or connect to database
db = client["todo_app"]

# Step 2: Create or connect to collections
users_col = db["users"]
tasks_col = db["tasks"]

# Step 3: Insert a sample user
user_data = {
    "username": "admin",
    "password": "admin123"
}

# Insert only if user doesn't exist
if not users_col.find_one({"username": user_data["username"]}):
    users_col.insert_one(user_data)
    print("✅ User created successfully!")
else:
    print("⚠️ User already exists.")

# Step 4: Insert a sample task
task_data = {
    "username": "admin",
    "title": "Create To-Do App UI",
    "status": "Pending",
    "date_created": datetime.now().strftime("%Y-%m-%d")
}

tasks_col.insert_one(task_data)
print("✅ Sample task added!")

# Step 5: Print inserted data
print("\n📂 Users:")
for user in users_col.find():
    print(user)

print("\n📝 Tasks:")
for task in tasks_col.find():
    print(task)
