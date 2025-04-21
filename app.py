from application import app
from flask import render_template
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
app.secret_key = '123'
if __name__ == "__main__":
    app.run(debug=True)


