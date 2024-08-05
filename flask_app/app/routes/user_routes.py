from flask import Blueprint
from ..controllers import User_controllers


app = Blueprint('signup', __name__)
app = Blueprint('login', __name__)

app.route("/")(user_controllers.index)

app.route("/signup", methods=['POST','GET'])(user_controllers.signup)

app.route("/login", methods=['POST','GET'])(user_controllers.login)