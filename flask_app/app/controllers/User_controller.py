from flask import flash, request, redirect, url_for, render_template
from ..models.user import User


def signup():
    if request.method == "POST":
        # Declare variables
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        password = request.form["password"]
        
        # Adding user to the database//
        cust_data = {"name": name, "surname": surname, "email": email, "password": password }
        
       # Check if the user exists in the database USING EMAIL
        if User.user_exist(email):
            return redirect(url_for('login.signup'))
        
        User.register_user(cust_data)