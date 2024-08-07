
from flask import flash, request, jsonify ,session
from ..models.user import User
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

def signup():
    if request.method == "POST":
        # Declare variables
        client_data = {
            
           "name": request.json.get("name"),
           "surname": request.json.get("surname"),
           "email": request.json.get("email"),
           "password": request.json.get("password"),
        }
        
        # # Check if the user exists in the database USING EMAIL
        # if User.user_exist(email):
        #     flash("User with this email already exists.", "danger")
        #     return jsonify({"error": "User with this email already exists."}), 400
        
        # # Adding user to the database
        # client_data = {"name": name, "surname": surname, "email": email, "password": password}
        User.register_user(client_data)   
    return jsonify({"message": "User registered successfully."}), 201
    
    
    
   
def login():
    if request.method == "POST":
        user_id= "user_id"
        client_details = {
                
           "email": request.json.get("email"),
           "password": request.json.get("password"),
        }
        
        User.login_user(client_details,user_id)
        session['user_id'] = ()
        return jsonify({"message": "Login successful."}), 200
    else:
        return jsonify({"error": "Method not allowed."}), 405
    
    
def signup_admin():
    if request.method == "POST":
        # Declare variables
        admin_data = {
            
           "name": request.json.get("name"),
           "surname": request.json.get("surname"),
           "email": request.json.get("email"),
           "password": request.json.get("password"),
        }
        
        # # Check if the user exists in the database USING EMAIL
        # if User.user_exist(email):
        #     flash("User with this email already exists.", "danger")
        #     return jsonify({"error": "User with this email already exists."}), 400
        
        # # Adding user to the database
        # client_data = {"name": name, "surname": surname, "email": email, "password": password}
        User.register_admin(admin_data)   
    return jsonify({"message": "Admin registered successfully."}), 201
    
    
def login_admin():
    data = request.get_json()
    email = data['email']
    password = data['password']
    print('Received data:',  email , password)

    user = User.query_filter_by (email, password).first()

    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify({'message': 'Login Success', 'access_token': access_token})
    else:
        return jsonify({'message': 'Login Failed'}), 401



