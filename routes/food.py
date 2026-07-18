from flask import Blueprint, render_template
from services.food_service import get_food_by_id

food_bp = Blueprint("food", __name__)

@food_bp.route("/food/<food_id>")
def food_details(food_id):

    food = get_food_by_id(food_id)

    return render_template(
        "food/food_details.html",
        food=food
    )