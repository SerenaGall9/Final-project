from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

# Create the app
app = Flask(__name__)

# Secret key for sessions
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://your_user:your_password@localhost/your_database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database object
db = SQLAlchemy(app)

# Initialize the login manager
login_manager = LoginManager()
login_manager.init_app(app)

# Set the login view (route to redirect if not logged in)
login_manager.login_view = 'login'

# Import routes and models after app and db are initialized to prevent circular imports
from application import routes, models
