from flask import render_template, url_for, request, redirect, session, flash
from application import app, data_access
from app import bcrypt
from application.data_access import get_db_connection


@app.route('/vibes')
def show_vibes(name=None):
    vibes = data_access.get_all_vibes()
    return render_template('vibes.html', vibes=vibes, name=name)

@app.route('/cuisines/<int:vibe_id>')
def display_cuisines(vibe_id):
    selected_vibe = data_access.get_vibe_by_id(vibe_id)
    if not selected_vibe:
        return "Vibe not found", 404
    cuisines = data_access.get_all_cuisines()
    return render_template('cuisine.html', cuisines=cuisines, vibe=selected_vibe)

@app.route('/all_restaurants')
def all_restaurants():
    restaurants = data_access.get_all_restaurants()
    return render_template('restaurants.html', restaurants=restaurants)

@app.route('/all_restaurants/<int:restaurant_id>')
def restaurant_by_id(restaurant_id):
    restaurant = data_access.get_restaurant_by_id(restaurant_id)
    if not restaurant:
        return render_template('404.html'), 404
    all_restaurants = data_access.get_all_restaurants()
    next_url = url_for('restaurant_by_id', restaurant_id=restaurant_id + 1) if restaurant_id + 1 < len(all_restaurants) else None
    previous_url = url_for('restaurant_by_id', restaurant_id=restaurant_id - 1) if restaurant_id > 0 else None
    return render_template('restaurant.html', restaurant=restaurant, next_url=next_url, previous_url=previous_url, title=restaurant['name'])

@app.route('/restaurant/<int:restaurant_id>')
def show_restaurant(restaurant_id):
    restaurant = data_access.get_restaurant_by_id(restaurant_id)
    reviews = data_access.get_reviews_for_restaurant(restaurant_id)
    return render_template('restaurant_detail.html', restaurant=restaurant, reviews=reviews)

@app.route('/restaurant/<int:restaurant_id>/review', methods=['GET', 'POST'])
def review_restaurant(restaurant_id):
    restaurant = data_access.get_restaurant_by_id(restaurant_id)
    if not restaurant:
        return render_template('404.html'), 404

    if request.method == 'POST':
        overall = int(request.form['overall_rating'])
        ambience = int(request.form['ambience_rating'])
        service = int(request.form['service_rating'])
        location = int(request.form['location_rating'])
        value = int(request.form['value_rating'])
        comment = request.form['comment']

        data_access.save_review(restaurant_id, overall, ambience, service, location, value, comment)
        return redirect(url_for('show_restaurant', restaurant_id=restaurant_id))

    return render_template('review_form.html', restaurant=restaurant)

@app.route('/account')
def get_account():
    return render_template('account.html')

@app.route("/ethos")
def ethos():
    return render_template("ethos.html", title="Our Ethos")

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        entered_password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user WHERE email = %s", (email,))
        user = cursor.fetchone()

        if not user:
            conn.close()
            return render_template('login.html', error="User not found. Please sign up first.")

        stored_password = user['password']
        try:
            if bcrypt.check_password_hash(stored_password, entered_password):
                session['email'] = email
                session['loggedIn'] = True
                conn.close()
                return redirect(url_for('show_vibes'))
        except ValueError:
            if stored_password == entered_password:
                new_hash = bcrypt.generate_password_hash(entered_password).decode('utf-8')
                cursor.execute("UPDATE user SET password = %s WHERE email = %s", (new_hash, email))
                conn.commit()
                session['email'] = email
                session['loggedIn'] = True
                conn.close()
                return redirect(url_for('show_vibes'))

        conn.close()
        return render_template('login.html', error="Invalid credentials.")

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            return render_template('register.html', error="User already exists. Please log in.")

        cursor.execute("INSERT INTO user (email, password) VALUES (%s, %s)", (email, password_hash))
        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session['loggedIn'] = False
    return redirect(url_for('login'))