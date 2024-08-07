from flask import Blueprint
from ..controllers import User_controller


app = Blueprint('products', __name__)

# app.route("/")(User_controller.index)

app.route("/signup", methods=['POST','GET'])(User_controller.signup)

app.route("/login", methods=['POST','GET'])(User_controller.login)