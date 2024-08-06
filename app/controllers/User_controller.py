from flask import flash, request, jsonify ,session
from ..models.user import User

def signup():
    if request.method == "POST":
        # Declare variables
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        password = request.form["password"]
        
        # Check if the user exists in the database USING EMAIL
        if User.user_exist(email):
            flash("User with this email already exists.", "danger")
            return jsonify({"error": "User with this email already exists."}), 400
        
        # Adding user to the database
        client_data = {"name": name, "surname": surname, "email": email, "password": password}
        User.register_user(client_data)   
    return jsonify({"message": "User registered successfully."}), 201
    
    
   
# def login():
#     if request.method == "POST":
#         user_id = request.form.get("id")
#         email = request.form["email"]
#         password = request.form["password"]

#         # Check if the user exists in the database
#         user = User.user_exist(email=email)()
        
#         if user and User.login_user(password):
#             session['user_id'] = (user_id)
#             return jsonify({"message": "Login successful."}), 200
#         else:
#             flash("Invalid email or password.", "danger")
#             return jsonify({"error": "Invalid email or password."}), 401

#     return jsonify({"error": "Method not allowed."}), 405



