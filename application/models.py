from flask_login import UserMixin
from application import db
from datetime import datetime

# Define your models here

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(200))

class Review(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(1000), nullable=False)
    creation_date = db.Column(db.Date, default=datetime.utcnow)

# Create a user loader function for Flask-Login
from application import login_manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
