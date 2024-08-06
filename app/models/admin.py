from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    @classmethod
    def user_exist(cls, email, is_admin=None):
        if is_admin is None:
            return cls.query.filter_by(email=email).first()
        else:
            return cls.query.filter_by(email=email, is_admin=is_admin).first()

    @classmethod
    def register_user(cls, data):
        hashed_password = generate_password_hash(data['password'])
        new_user = cls(name=data['name'], surname=data['surname'], email=data['email'], password=hashed_password, is_admin=data.get('is_admin', False))
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @classmethod
    def login_user(cls, password, hashed_password):
        return check_password_hash(hashed_password, password)