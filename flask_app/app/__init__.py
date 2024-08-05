from flask import Flask
from flask_pymongo import PyMongo
from Config import Config
from flask import Blueprint


bp = Blueprint('controllers', __name__)


mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    mongo.init_app(app)
    with app.app_context():
      from routes import user_routes  
    app.register_blueprint(user_routes.app)
       
       

        
    return app