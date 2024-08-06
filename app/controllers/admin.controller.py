from flask import flash, request, jsonify ,session
from ..models.user import User


def admin_signup():
    if request.method == "POST":
        # Declare variables
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        password = request.form["password"]
        is_admin = True  # Set the user as an admin

        # Check if the user exists in the database USING EMAIL
        if User.user_exist(email):
            flash("User with this email already exists.", "danger")
            return jsonify({"error": "User with this email already exists."}), 400

        # Adding user to the database
        client_data = {"name": name, "surname": surname, "email": email, "password": password, "is_admin": is_admin}
        User.register_user(client_data)

        return jsonify({"message": "Admin registered successfully."}), 201

    return jsonify({"error": "Method not allowed."}), 405

def admin_login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Check if the user exists in the database and is an admin
        user = User.user_exist(email=email, is_admin=True)
        if user and User.login_user(password, user.password):
            session['user_id'] = user.id
            session['is_admin'] = True
            return jsonify({"message": "Admin login successful."}), 200
        else:
            flash("Invalid email or password.", "danger")
            return jsonify({"error": "Invalid email or password."}), 401

    return jsonify({"error": "Method not allowed."}), 405