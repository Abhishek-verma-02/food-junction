from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from services.admin_service import login_admin
from database.mongodb import db
from bson import ObjectId

admin_bp = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)

foods = db["foods"]


# ------------------ ADMIN LOGIN ------------------

@admin_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        admin = login_admin(
            request.form["email"],
            request.form["password"]
        )

        if admin:

            session["admin_id"] = str(admin["_id"])
            session["admin_name"] = admin["name"]

            return redirect(url_for("admin.dashboard"))

        flash("Invalid Email or Password")

    return render_template("admin/login.html")


# ------------------ DASHBOARD ------------------

@admin_bp.route("/")
def dashboard():

    if "admin_id" not in session:
        return redirect(url_for("admin.login"))

    total_foods = db["foods"].count_documents({})
    total_orders = db["orders"].count_documents({})
    total_users = db["users"].count_documents({})

    return render_template(
        "admin/dashboard.html",
        total_foods=total_foods,
        total_orders=total_orders,
        total_users=total_users
    )


# ------------------ VIEW FOODS ------------------

@admin_bp.route("/foods")
def manage_foods():

    if "admin_id" not in session:
        return redirect(url_for("admin.login"))

    all_foods = list(foods.find())

    return render_template(
        "admin/manage_foods.html",
        foods=all_foods
    )


# ------------------ ADD FOOD ------------------

@admin_bp.route("/add-food", methods=["GET", "POST"])
def add_food():

    if "admin_id" not in session:
        return redirect(url_for("admin.login"))

    if request.method == "POST":

        foods.insert_one({
            "name": request.form["name"],
            "category": request.form["category"],
            "price": int(request.form["price"]),
            "image": request.form["image"],
            "description": request.form["description"]
        })

        flash("Food Added Successfully")

        return redirect(url_for("admin.manage_foods"))

    return render_template("admin/add_food.html")


# ------------------ DELETE FOOD ------------------

@admin_bp.route("/delete-food/<food_id>")
def delete_food(food_id):

    if "admin_id" not in session:
        return redirect(url_for("admin.login"))

    foods.delete_one({
        "_id": ObjectId(food_id)
    })

    flash("Food Deleted Successfully")

    return redirect(url_for("admin.manage_foods"))


# ------------------ LOGOUT ------------------

@admin_bp.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("admin.login"))