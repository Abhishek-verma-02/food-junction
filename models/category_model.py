from database.mongodb import db

categories = db["categories"]


def get_all_categories():
    return list(categories.find())


def create_category(category):
    return categories.insert_one(category)