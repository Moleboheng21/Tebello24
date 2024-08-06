from bson import ObjectId
from ..models.user import User
from flask import flash, jsonify, request, redirect, url_for, render_template
from .. import mongo

def signup():
    if request.method == "POST":
        # Declare variables
        name = jsonify.get["name"]
        surname = jsonify.get["surname"]
        email = jsonify.get["email"]
        password = jsonify.get["password"]
        
        # Check if the user exists in the database USING EMAIL
        if User.user_exist(email):
            flash("User with this email already exists.", "danger")
            return jsonify({"error": "User with this email already exists."}), 400
        
        # Adding user to the database
        client_data = {"name": name, "surname": surname, "email": email, "password": password}
        User.register_user(client_data)   
  
    try:
        data = ()
        new_user = User.register_user(data)
        user_data = {
            'id': new_user.id,
            'name': new_user.name,
            'email': new_user.email,
            'created_at': new_user.created_at.isoformat(),
            'updated_at': new_user.updated_at.isoformat()
        }
        return jsonify(user_data), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
   
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



