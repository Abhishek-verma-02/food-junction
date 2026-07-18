from database.mongodb import db

orders = db["orders"]

def create_order(order):
    return orders.insert_one(order)

def get_orders(user_id):
    return list(orders.find({"user_id": user_id}))