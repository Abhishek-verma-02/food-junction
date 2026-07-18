from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import create_user, get_user_by_email


def register_user(name, email, password):

    if get_user_by_email(email):
        return False, "Email already registered"

    hashed_password = generate_password_hash(password)

    user = {
        "name": name,
        "email": email,
        "password": hashed_password
    }

    create_user(user)

    return True, "Registration Successful"


def login_user(email, password):

    user = get_user_by_email(email)

    if not user:
        return False, "User not found"

    if not check_password_hash(user["password"], password):
        return False, "Invalid password"

    return True, user