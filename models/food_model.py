from database.mongodb import db
from bson import ObjectId

foods = db["foods"]


def get_all_foods():
    return list(foods.find())


def get_food_by_id(food_id):
    return foods.find_one({"_id": ObjectId(food_id)})


def add_food(food):
    return foods.insert_one(food)


def update_food(food_id, data):
    return foods.update_one(
        {"_id": ObjectId(food_id)},
        {"$set": data}
    )


def delete_food(food_id):
    return foods.delete_one(
        {"_id": ObjectId(food_id)}
    )