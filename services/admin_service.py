from database.mongodb import db

admins = db["admins"]


def login_admin(email, password):
    return admins.find_one({
        "email": "admin@foodjunction.com",
        "password": "admin123"
    })