from flask import Blueprint, render_template, session, redirect, url_for
from database.mongodb import db
from bson import ObjectId

orders_bp = Blueprint("orders", __name__)

orders = db["orders"]


@orders_bp.route("/orders")
def order_history():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    all_orders = list(
        orders.find({
            "user_id": session["user_id"]
        })
    )

    return render_template(
        "orders/orders.html",
        orders=all_orders
    )


@orders_bp.route("/admin/orders")
def admin_orders():

    if "admin_id" not in session:
        return redirect(url_for("admin.login"))

    all_orders = list(orders.find())

    return render_template(
        "admin/manage_orders.html",
        orders=all_orders
    )


@orders_bp.route("/admin/order/<order_id>/<status>")
def change_status(order_id, status):

    if "admin_id" not in session:
        return redirect(url_for("admin.login"))

    orders.update_one(
        {"_id": ObjectId(order_id)},
        {
            "$set": {
                "status": status
            }
        }
    )

    return redirect(url_for("orders.admin_orders"))