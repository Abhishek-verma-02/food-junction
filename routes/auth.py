from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from services.auth_service import register_user, login_user

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        success, message = register_user(name, email, password)

        flash(message)

        if success:
            return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        success, result = login_user(email, password)

        if success:
            session["user_id"] = str(result["_id"])
            session["user_name"] = result["name"]

            flash("Login Successful")
            return redirect(url_for("home.home"))

        flash(result)

    return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():

    session.clear()

    flash("Logged Out Successfully")

    return redirect(url_for("home.home"))