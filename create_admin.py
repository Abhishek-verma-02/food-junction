from database.mongodb import db

db["admins"].insert_one({
    "name": "Administrator",
    "email": "admin@foodjunction.com",
    "password": "admin123"
})

print("Admin Created Successfully")