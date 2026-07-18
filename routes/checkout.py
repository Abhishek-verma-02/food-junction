from flask import Blueprint, render_template, request, session, redirect, url_for, flash

from config import Config
from services.cart_service import fetch_cart, empty_cart
from services.order_service import place_order
from services.payment_service import create_payment

checkout_bp = Blueprint("checkout", __name__)


@checkout_bp.route("/checkout", methods=["GET", "POST"])
def checkout():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    items = fetch_cart(session["user_id"])
    total = sum(item["price"] * item["quantity"] for item in items)

    if request.method == "POST":

        # Cash on Delivery
        if request.form["payment"] == "COD":

            order = {
                "user_id": session["user_id"],
                "customer_name": session["user_name"],
                "phone": request.form["phone"],
                "address": request.form["address"],
                "payment_method": "COD",
                "items": items,
                "total": total,
                "status": "Pending"
            }

            place_order(order)
            empty_cart(session["user_id"])

            flash("Order Placed Successfully")
            return redirect(url_for("orders.order_history"))

        # Razorpay
        session["phone"] = request.form["phone"]
        session["address"] = request.form["address"]

        payment = create_payment(total)

        return render_template(
            "payment/razorpay.html",
            payment=payment,
            key_id=Config.RAZORPAY_KEY_ID
        )

    return render_template(
        "checkout/checkout.html",
        items=items,
        total=total
    )


@checkout_bp.route("/payment-success", methods=["POST"])
def payment_success():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    items = fetch_cart(session["user_id"])
    total = sum(item["price"] * item["quantity"] for item in items)

    order = {
        "user_id": session["user_id"],
        "customer_name": session["user_name"],
        "phone": session.get("phone"),
        "address": session.get("address"),
        "payment_method": "Razorpay",
        "payment_id": request.form.get("razorpay_payment_id"),
        "items": items,
        "total": total,
        "status": "Paid"
    }

    place_order(order)
    empty_cart(session["user_id"])

    session.pop("phone", None)
    session.pop("address", None)

    flash("Payment Successful!")

    return redirect(url_for("orders.order_history"))