from flask import Flask
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


from food_for_thought import routes
# from food_for_thought import errors