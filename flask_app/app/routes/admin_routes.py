from flask import Blueprint, flash, request, jsonify, session
from ..models.admin import Admin

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/admin/signup', methods=['POST'])
def admin_signup():
    # Same as the admin_signup() function from the previous response
    pass

@auth_bp.route('/admin/login', methods=['POST'])
def admin_login():
    # Same as the admin_login() function from the previous response
    pass

@auth_bp.route('/signup', methods=['POST'])
def signup():
    # Same as the signup() function from the previous response
    pass

@auth_bp.route('/login', methods=['POST'])
def login():
    # Same as the login() function from the previous response
    pass