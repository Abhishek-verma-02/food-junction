from database.mongodb import db
from bson import ObjectId

cart = db["cart"]


def add_to_cart(cart_item):
    return cart.insert_one(cart_item)


def get_cart_items(user_id):
    return list(cart.find({"user_id": user_id}))


def remove_cart_item(cart_id):
    return cart.delete_one({"_id": ObjectId(cart_id)})


def update_quantity(cart_id, quantity):
    return cart.update_one(
        {"_id": ObjectId(cart_id)},
        {"$set": {"quantity": quantity}}
    )
from bson import ObjectId

def get_cart_item(user_id, food_id):
    return cart.find_one({
        "user_id": user_id,
        "food_id": food_id
    })


def increase_quantity(cart_id):
    return cart.update_one(
        {"_id": ObjectId(cart_id)},
        {"$inc": {"quantity": 1}}
    )


def decrease_quantity(cart_id):
    return cart.update_one(
        {"_id": ObjectId(cart_id)},
        {"$inc": {"quantity": -1}}
    )
    
def clear_cart(user_id):
    return cart.delete_many({"user_id": user_id})