from flask import Flask
from config import Config

from routes import home_bp, auth_bp, profile_bp, food_bp, cart_bp, checkout_bp, orders_bp, payment_bp, admin_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(food_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(checkout_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(admin_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)