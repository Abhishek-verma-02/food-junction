from flask import Blueprint, request, session, redirect, url_for, flash

from services.cart_service import fetch_cart, empty_cart
from services.order_service import place_order

payment_bp = Blueprint("payment", __name__)


@payment_bp.route("/payment-success", methods=["POST"])
def payment_success():

    items = fetch_cart(session["user_id"])

    total = sum(item["price"] * item["quantity"] for item in items)

    order = {
        "user_id": session["user_id"],
        "customer_name": session["user_name"],
        "phone": request.form.get("phone"),
        "address": request.form.get("address"),
        "payment_method": "Razorpay",
        "payment_id": request.form.get("razorpay_payment_id"),
        "items": items,
        "total": total,
        "status": "Paid"
    }

    place_order(order)

    empty_cart(session["user_id"])

    flash("Payment Successful!")

    return redirect(url_for("orders.order_history"))