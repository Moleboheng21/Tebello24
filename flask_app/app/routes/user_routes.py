from flask import Blueprint
from ..controllers import User_controllers


app = Blueprint('signup', __name__)
app = Blueprint('login', __name__)

app.route("/")(User_controllers.index)

app.route("/signup", methods=['POST','GET'])(User_controllers.signup)

app.route("/login", methods=['POST','GET'])(User_controllers.login)