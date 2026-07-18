from models.cart_model import (
    add_to_cart,
    get_cart_items,
    remove_cart_item,
    update_quantity
)

from services.food_service import get_food_by_id


from models.cart_model import (
    add_to_cart,
    get_cart_items,
    get_cart_item,
    increase_quantity
)

from services.food_service import get_food_by_id


def add_food_to_cart(user_id, food_id):

    existing = get_cart_item(user_id, food_id)

    if existing:
        increase_quantity(existing["_id"])
        return

    food = get_food_by_id(food_id)

    cart_item = {
        "user_id": user_id,
        "food_id": str(food["_id"]),
        "name": food["name"],
        "price": food["price"],
        "image": food["image"],
        "quantity": 1
    }

    add_to_cart(cart_item)


def fetch_cart(user_id):
    return get_cart_items(user_id)


from models.cart_model import clear_cart

def empty_cart(user_id):
    clear_cart(user_id)