from flask import Flask
from flask_pymongo import PyMongo
from .Config import Config
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    jwt = JWTManager(app)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'your_strong_secret_key'
    app.config["JWT_SECRET_KEY"] = 'your_jwt_secret_key'
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    
    mongo.init_app(app)
    with app.app_context():
       from .routes import user_routes
       app.register_blueprint(user_routes.app)

        
    return app