from flask import Blueprint, session, redirect, url_for, render_template

from services.cart_service import (
    add_food_to_cart,
    fetch_cart
)

cart_bp = Blueprint("cart", __name__)


@cart_bp.route("/add-to-cart/<food_id>")
def add_cart(food_id):

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    add_food_to_cart(
        session["user_id"],
        food_id
    )

    return redirect(url_for("cart.view_cart"))


@cart_bp.route("/cart")
def view_cart():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    items = fetch_cart(session["user_id"])

    total = sum(
        item["price"] * item["quantity"]
        for item in items
    )

    return render_template(
        "cart/cart.html",
        items=items,
        total=total
    )
    
from models.cart_model import (
    increase_quantity,
    decrease_quantity,
    remove_cart_item
)


@cart_bp.route("/cart/increase/<cart_id>")
def increase(cart_id):

    increase_quantity(cart_id)

    return redirect(url_for("cart.view_cart"))


@cart_bp.route("/cart/decrease/<cart_id>")
def decrease(cart_id):

    items = fetch_cart(session["user_id"])

    for item in items:

        if str(item["_id"]) == cart_id:

            if item["quantity"] > 1:
                decrease_quantity(cart_id)
            else:
                remove_cart_item(cart_id)

            break

    return redirect(url_for("cart.view_cart"))

@cart_bp.route("/cart/remove/<cart_id>")
def remove(cart_id):

    remove_cart_item(cart_id)

    return redirect(url_for("cart.view_cart"))