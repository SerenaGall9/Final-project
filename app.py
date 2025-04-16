from flask import Flask
from flask_login import LoginManager
from food_for_thought.models import db, User
from food_for_thought import app
#
app = Flask(__name__)
# app.secret_key = "super-secret-key"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///foodforthought.db"
#
# db.init_app(app)

# # Flask-Login setup
# login_manager = LoginManager()
# login_manager.login_view = 'login'
# login_manager.init_app(app)


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


if __name__ == "__main__":
    app.run(debug=True)
