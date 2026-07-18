from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)

db = client["food_junction"]

collections = {
    "users": db["users"],
    "foods": db["foods"],
    "categories": db["categories"],
    "cart": db["cart"],
    "orders": db["orders"],
    "payments": db["payments"],
    "wishlist": db["wishlist"],
    "reviews": db["reviews"],
    "admins": db["admins"]
}