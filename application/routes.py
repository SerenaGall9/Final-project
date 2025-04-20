from flask import request, redirect, url_for, render_template, flash
from flask import flash
from flask import render_template, url_for, request, redirect, session

from application import app
from datetime import datetime
from app import bcrypt
from application.data_access import get_db_connection
import mysql


@app.route('/', methods=['GET', 'POST'])
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
            # Try checking as if it's a hashed password
            if bcrypt.check_password_hash(stored_password, entered_password):
                session['email'] = email
                session['loggedIn'] = True
                conn.close()
                return redirect(url_for('get_vibes'))

        except ValueError:
            # ValueError means the stored password was not a valid hash

            if stored_password == entered_password:
                # If correct, rehash the password and store it
                new_hash = bcrypt.generate_password_hash(entered_password).decode('utf-8')
                cursor.execute("UPDATE user SET password = %s WHERE email = %s", (new_hash, email))
                conn.commit()

                session['email'] = email
                session['loggedIn'] = True
                conn.close()
                return redirect(url_for('vibes'))

        # If password check failed
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
            return render_template('signup.html', error="User already exists. Please log in.")

        cursor.execute("INSERT INTO user (email, password) VALUES (%s, %s)", (email, password_hash))
        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    return render_template('signup.html')


# @app.route('/logout')
# def logout():
#         # remove the username from the session if it is there
#     session.pop('username', None)
#
#     session['loggedIn'] = False
#     return redirect(url_for('all_cats'))

@app.route('/vibes')
def get_vibes():
    return render_template('layout2.html')
# # banner, carousel, confirm button, I can't choose button
#
@app.route('/cuisines')
def get_cuisine():
    return render_template('cuisines.html')
# dynamic dropdown menu, back button, I can't choose button

#

@app.route('/restaurant/<id>')
def get_restaurant(id):
    restaurant = find_restaurant(id)
    # cuisine = find_cuisine_to_restaurant(id)
    if restaurant is not None:
        name = restaurant["name"]
        phone_number = restaurant["phone_number"]
        address = restaurant["address"]
        website = restaurant["website"]
        cuisine = find_cuisine_from_id(restaurant["cuisine_id"])
        vibe = find_vibe_from_id(restaurant["vibe_id"])
        if cuisine is None:
            cuisine = "Unknown cuisine"
        # vibe = restaurant["vibe_id"]
        return render_template('restaurant.html', name=name, phone_number=phone_number, address=address, website=website, cuisine=cuisine, vibe=vibe)
    else:
        return render_template("404.html")

def find_cuisine_from_id(cuisine_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    sql = "SELECT name FROM cuisine WHERE cuisine_id = %s"

    cursor.execute(sql, (cuisine_id,))
    cuisine = cursor.fetchone()
    connection.close()

    if cuisine is not None:
        return cuisine[0]
    return None

def find_vibe_from_id(vibe_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    sql = "SELECT name FROM vibetype WHERE vibe_id = %s"

    cursor.execute(sql, (vibe_id,))
    vibe = cursor.fetchone()
    connection.close()

    if vibe is not None:
        return vibe[0]
    return None

def find_restaurant(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    sql = "SELECT name, address, location_id, phone_number, website, cuisine_id, vibe_id FROM restaurants WHERE restaurant_id = %s"
    cursor.execute(sql, (id,))

    restaurant = cursor.fetchone()
    connection.close()

    if restaurant:
        return {
            'name': restaurant[0],
            'address': restaurant[1],
            'location_id': restaurant[2],
            'phone_number': restaurant[3],
            'website': restaurant[4],
            'cuisine_id': restaurant[5],
            'vibe_id': restaurant[6],
        }
    return None


@app.route('/all_restaurants')
def get_all_restaurants():
    return render_template(all_restaurants.html)
# takes input from the first 2 pages into the filtering criteria,
# interacts with the database to filter based on other criteria (session handling; price, vibe,cuisine,location)

#
#
@app.route('/all_restaurants/<int:restaurant_id>')
# this needs to display the signle restaurant page with image, menu link, details, leave review button and reviews from database
def restaurant_by_id(restaurant_id):
    # Fetch the project from the database
    restaurants = get_restaurant_by_id(restaurant_id)

    if not restaurant:
        return render_template('404.html'), 404

    # Time-based greeting
    time_slot = get_time_of_day(datetime.now().hour)

    # Get all projects to create next/previous navigation links
    all_restaurants = get_restaurants()
    total = len(all_restaurants)

    # Generate URLs for next and previous projects
    next_url = url_for('restaurant_by_id', restaurant_id=restaurant_id + 1) if restaurant_id + 1 < 4 else None
    previous_url = url_for('restaurant_by_id', restaraunt_id=restaurant_id - 1) if restaurant_id > 0 else None


    return render_template(
        'restaurant.html',  # Render project.html
        restaurant=restaurant,
        time_slot=time_slot,
        next_url=next_url,
        previous_url=previous_url,
        image_src=image_src,
        image_gif=image_gif,
        title=restaurant['name']
    )

@app.route('/restaurant_detail/<int:restaurant_id>')
def restaurant_detail(restaurant_id):
    # Fetch the restaurant from the database by its ID
    restaurant = get_restaurant_by_id(restaurant_id)

    if not restaurant:
        return render_template('404.html'), 404  # Handle the case where the restaurant doesn't exist

    return render_template('restaurant_details.html', project=restaurant)


@app.route('/account')
def get_account():
    return render_template('account.html')

@app.route('/review/<int:restaurant_id>', methods=['GET', 'POST'])
# prefilled form with restaurant name
def review(restaurant_id):
    restaurant = Restaurant.query.get_or_404(restaurant_id)

    if request.method == 'POST':
        new_review = Review(
            restaurant_id=restaurant.id,
            user_id=current_user.id,
            rating=int(request.form['rating']),
            comment=request.form['comment']
        )
        db.session.add(new_review)
        db.session.commit()
        flash('Review added successfully!')
        return redirect(url_for('restaurant_detail', id=restaurant.id))

    return render_template('review.html', restaurant=restaurant)

# review url->pass in restaurant id->got into database, get restaurant name, put it in a label
# do stars from bootstrap
# dropdown/stars for different things/ tick boxes (would you go here again?), structure, prepopulate the label


@app.route('/health')
def get_health():
    return "I am healthy"
