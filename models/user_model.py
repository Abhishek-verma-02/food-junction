from database.mongodb import db

users = db["users"]


def create_user(user_data):
    return users.insert_one(user_data)


def get_user_by_email(email):
    return users.find_one({"email": email})


def get_user_by_id(user_id):
    return users.find_one({"_id": user_id})