from flask import Blueprint, render_template

from services.food_service import get_all_foods

from services.category_service import fetch_categories

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():

    foods = get_all_foods()

    categories = fetch_categories()

    return render_template(
        "index.html",
        foods=foods,
        categories=categories
    )