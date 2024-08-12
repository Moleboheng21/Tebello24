from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from ..models.user import User

def register():
    # Extract form data
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    surname = data.get('surname')
    password = data.get('password')

    # Set The Default Role To User 
    role = data.get('role', 'user')

    if User.find_by_email(email):
        return jsonify({"msg": "User already exists"}), 409

    hashed_password = generate_password_hash(password)
    new_user = User(email=email, name=name, surname=surname, password=hashed_password, role=role)
    new_user.save()

    return jsonify({"msg": "User registered successfully"}), 201
    
    

def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.find_by_email(email)
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity={"email": user.email, "role": user.role})
        return jsonify({"access token": access_token ,"role": user.role,"password":user.password} ), 200

    return jsonify({"msg": "Invalid credentials"}), 401
    





