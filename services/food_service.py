from bson import ObjectId

def get_food_by_id(food_id):
    return foods.find_one({"_id": ObjectId(food_id)})

from database.mongodb import db

foods = db["foods"]

def get_all_foods():

    return list(foods.find())

def get_food_by_category(category):

    return list(

        foods.find(
            {"category": category}
        )

    )

def search_food(keyword):

    return list(

        foods.find(
            {
                "name":
                {
                    "$regex": keyword,
                    "$options": "i"
                }
            }
        )

    )