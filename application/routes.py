from flask import flash
from flask import render_template, url_for, request, redirect, session

from application import app
from app import bcrypt
from application.data_access import get_db_connection, find_cuisine_from_id, find_vibe_from_id, find_restaurant, \
    get_all_vibes, get_vibe_by_id, get_all_cuisines, get_reviews_by_restaurant_id, save_review, get_user, \
    get_reviews_by_user, get_reviews_by_restaurant_id


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    # 1. Prepare the carousel data
    team_members = [
        { 'name': 'Renée', 'photo': 'images/members/renee.png' },
        { 'name': 'Milena', 'photo': 'images/members/milena.png' },
        { 'name': 'Serena', 'photo': 'images/members/serena.png' },
        { 'name': 'Eleanor', 'photo': 'images/members/eleanor.png' },
        { 'name': 'Khrisha', 'photo': 'images/members/khrisha.png' },
    ]
    restaurant_partners = [
        { 'name': 'Gymkhana', 'description': 'A Michelin-starred Indian restaurant.', 'image': 'images/restaurantimages/gymkhana.png' },
        { 'name': 'Dishoom', 'description': 'Bombay-inspired cafés with bold flavors.', 'image': 'images/restaurantimages/dishoom.png' },
        { 'name': 'Beit El Zaytoun', 'description': 'Authentic Palestinian cuisine.', 'image': 'images/restaurantimages/beit.png' },
        { 'name': 'Inamo Sukoshi', 'description': 'Pan-Asian fusion with interactive tables.', 'image': 'images/restaurantimages/inamo.png' },
        { 'name': 'La Tagliata', 'description': 'Traditional Italian trattoria.', 'image': 'images/restaurantimages/tagliata.png' },
    ]

    error = None
    if request.method == 'POST':
        # — your existing login logic —
        email = request.form['email']
        pw    = request.form['password']
        conn  = get_db_connection()
        cur   = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM user WHERE email = %s", (email,))
        user = cur.fetchone()

        if not user:
            error = "User not found. Please sign up first."
        else:
            stored = user['password']
            try:
                if bcrypt.check_password_hash(stored, pw):
                    # success
                    session.update({
                      'email': email,
                      'username': user['user_name'],
                      'loggedIn': True,
                      'user_id': user['user_id'],
                    })
                    conn.close()
                    return redirect(url_for('show_vibes'))
            except ValueError:
                # legacy plaintext
                if stored == pw:
                    new_hash = bcrypt.generate_password_hash(pw).decode('utf-8')
                    cur.execute("UPDATE user SET password = %s WHERE email = %s", (new_hash, email))
                    conn.commit()
                    session.update({
                      'email': email,
                      'username': user['user_name'],
                      'loggedIn': True,
                      'user_id': user['user_id'],
                    })
                    conn.close()
                    return redirect(url_for('show_vibes'))
            error = "Invalid email or password, please try again."
        conn.close()

    # render the landing page (which includes the login form in section 3)
    return render_template(
      'layout_landing.html',
      team_members=team_members,
      restaurant_partners=restaurant_partners,
      error=error
    )


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        password = request.form['password']
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            conn.close()
            return render_template('signup.html', error="User already exists. Please login instead.")

        cursor.execute("INSERT INTO user (email, password,name,surname) VALUES (%s, %s,%s,%s)", (email, password_hash, name, surname))
        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/forgot-password', methods=['GET','POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        surname = request.form['surname']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            return render_template('forgot_password.html', error="Passwords do not match.")

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user WHERE email = %s AND surname = %s", (email, surname))
        user = cursor.fetchone()

        if not user:
            conn.close()
            return render_template('forgot_password.html', error="User not found. Please check your email and surname.")

        new_hash = bcrypt.generate_password_hash(new_password).decode('utf-8')
        cursor.execute("UPDATE user SET password = %s WHERE email = %s", (new_hash, email))
        conn.commit()
        conn.close()

        return render_template('forgot_password.html', success="Password updated. You can now log in.")

    return render_template('forgot_password.html')


@app.route('/vibes')
def show_vibes(name=None):
    vibes = get_all_vibes()
    return render_template('vibes.html', vibes=vibes, name=name)


@app.route('/cuisines/<int:vibe_id>')
def display_cuisines(vibe_id):
    selected_vibe = get_vibe_by_id(vibe_id)
    if not selected_vibe:
        return "Vibe not found", 404

    session['selected_vibe_id'] = vibe_id
    cuisines = get_all_cuisines()
    return render_template('cuisines.html', cuisines=cuisines, vibe=selected_vibe)


@app.route('/select_cuisine/<int:cuisine_id>')
def select_cuisine(cuisine_id):
    session['selected_cuisine_id'] = cuisine_id  # Use the value from the URL
    return redirect(url_for('all_restaurants'))


@app.route('/logout')
def logout():
        # remove the username from the session if it is there
    session.pop('email', None)

    session['loggedIn'] = False
    return redirect(url_for('login'))


# @app.route('/all_restaurants')
# def all_restaurants():
#     # Get selected filters from query string
#     selected_cuisine = request.args.get('cuisine', type=int)
#     selected_vibe = request.args.get('vibe', type=int)
#     selected_location = request.args.get('location', type=int)
#     selected_rating = request.args.get('rating', type=float)
#     selected_ambiance = request.args.get('ambience', type=float)
#     selected_service = request.args.get('service', type=float)
#     selected_value = request.args.get('value', type=float)
#     selected_location_rating = request.args.get('location_rating', type=float)
#     selected_price_range = request.args.get('price_range', type=float)
#
#     if selected_cuisine is None and selected_vibe is None:
#         selected_cuisine = session.get('selected_cuisine_id')
#         selected_vibe = session.get('selected_vibe_id')
#     else:
#
#         session['selected_cuisine_id'] = selected_cuisine
#         session['selected_vibe_id'] = selected_vibe
#
#     conn = get_db_connection()
#     cursor = conn.cursor(dictionary=True)
#
#     # Fetch filter options for dropdowns
#     cursor.execute("SELECT cuisine_id, name FROM Cuisine")
#     cuisines = cursor.fetchall()
#
#     cursor.execute("SELECT vibe_id, name FROM vibetype")
#     vibes = cursor.fetchall()
#
#     cursor.execute("SELECT location_id, direction FROM londonlocation")
#     locations = cursor.fetchall()
#
#     # Main query with filters
#     query = """
#     SELECT
#         r.restaurant_id,
#         r.name,
#         r.address,
#         r.website,
#         r.price_range,
#         c.name AS cuisine,
#         v.name AS vibe,
#         l.direction AS location,
#         r.price_range AS price_range,
#         AVG(rv.rating) AS avg_rating,
#         AVG(rv.ambience) AS avg_ambiance,
#         AVG(rv.service) AS avg_service,
#         AVG(rv.value_for_money) AS avg_value,
#         AVG(rv.location) AS avg_location_rating
#     FROM Restaurants r
#     JOIN Cuisine c ON r.cuisine_id = c.cuisine_id
#     JOIN vibetype v ON r.vibe_id = v.vibe_id
#     JOIN londonlocation l ON r.location_id = l.location_id
#     LEFT JOIN Review rv ON r.restaurant_id = rv.restaurant_id
#     WHERE
#         (%s IS NULL OR r.cuisine_id = %s) AND
#         (%s IS NULL OR r.vibe_id = %s) AND
#         (%s IS NULL OR r.location_id = %s) AND
#         (%s IS NULL OR r.price_range = %s)
#     GROUP BY r.restaurant_id
#     HAVING
#         (%s IS NULL OR avg_rating >= %s) AND
#         (%s IS NULL OR avg_ambiance >= %s) AND
#         (%s IS NULL OR avg_service >= %s) AND
#         (%s IS NULL OR avg_value >= %s) AND
#         (%s IS NULL OR avg_location_rating >= %s)
#     """
#
#     params = [
#         selected_cuisine, selected_cuisine,
#         selected_vibe, selected_vibe,
#         selected_location, selected_location,
#         selected_price_range, selected_price_range,
#         selected_rating, selected_rating,
#         selected_ambiance, selected_ambiance,
#         selected_service, selected_service,
#         selected_value, selected_value,
#         selected_location_rating, selected_location_rating
#     ]
#
#     cursor.execute(query, params)
#     restaurants = cursor.fetchall()
#     image_mapping = {
#         "Dishoom Covent Garden": "dishoom.png",
#         "Coco Grill & Lounge": "coco.png",
#         "Olives and Meze": "olive.png",
#         "Scarpetta Canary Wharf": "scarpetta.png",
#         "Alexander The Great Greek Restaurant": "alexander.png",
#         "Gloria Trattoria": "gloria.png",
#         "Chutney Mary": "chutney.png",
#         "Gymkhana": "gymkhana.png",
#         "Babel grill house": "babel.png",
#         "Baba ghanouj": "baba.png",
#         "Mazar": "mazar.png",
#         "Beit El Zaytoun": "beit.png",
#         "NIJŪ": "nijo.png",
#         "Inamo sukoshi": "inamo.png",}
#
#     for r in restaurants:
#         r['image_filename'] = image_mapping.get(r['name'], 'default.jpg')
#     conn.close()
#
#     return render_template(
#         "all_restaurants.html",
#         restaurants=restaurants,
#         cuisines=cuisines,
#         vibes=vibes,
#         locations=locations,
#         selected_cuisine=selected_cuisine,
#         selected_price_range=selected_price_range,
#         selected_vibe=selected_vibe,
#         selected_location=selected_location,
#         selected_rating=selected_rating,
#         selected_ambiance=selected_ambiance,
#         selected_service=selected_service,
#         selected_value=selected_value,
#         selected_location_rating=selected_location_rating
#     )

# @app.route('/restaurant/<int:id>')
# def get_restaurant(id):
#     restaurant = find_restaurant(id)
#
#     # Dictionary: hardcode restaurant_id → image filename
#     image_filenames = {
#         2: 'coco.png',
#         3: 'olive.png',
#         4: 'scarpetta.png',
#         5: 'alexander.png',
#         6: 'latagliata.png',
#         7: 'gloria.png',
#         8: 'chutney.png',
#         9: 'dishoom.png',
#         10: 'gymkhana.png',
#         11: 'babel.png',
#         12: 'baba.png',
#         13: 'mazar.png',
#         14: 'beit.png',
#         15: 'nijo.png',
#         16: 'inamo.png'
#     }
#
#     if restaurant is not None:
#         name = restaurant["name"]
#         phone_number = restaurant["phone_number"]
#         address = restaurant["address"]
#         website = restaurant["website"]
#         price_range = restaurant["price_range"]
#         cuisine = find_cuisine_from_id(restaurant["cuisine_id"])
#         vibe = find_vibe_from_id(restaurant["vibe_id"])
#         description = restaurant['description']
#         menu_link = restaurant['menu_link']
#         reviews = get_reviews_by_restaurant_id(id)
#         restaurant_id = id
#
#         # ✅ Get the correct image filename from the dictionary
#         image_filename = image_filenames.get(id, 'default.jpg')  # fallback if not found
#
#         if cuisine is None:
#             cuisine = "Unknown cuisine"
#
#         return render_template(
#             'restaurant.html',
#             name=name,
#             phone_number=phone_number,
#             address=address,
#             website=website,
#             price_range=price_range,
#             cuisine=cuisine,
#             vibe=vibe,
#             description=description,
#             menu_link=menu_link,
#             reviews=reviews,
#             restaurant_id=restaurant_id,
#             image_filename=image_filename  # Pass it here!
#         )
#     else:
#         return render_template("404.html")

@app.route('/all_restaurants')
def all_restaurants():
    # Get selected filters from query string
    selected_cuisine = request.args.get('cuisine', type=int)
    selected_vibe = request.args.get('vibe', type=int)
    selected_location = request.args.get('location', type=int)
    selected_rating = request.args.get('rating', type=float)
    selected_ambiance = request.args.get('ambience', type=float)
    selected_service = request.args.get('service', type=float)
    selected_value = request.args.get('value', type=float)
    selected_location_rating = request.args.get('location_rating', type=float)
    selected_price_range = request.args.get('price_range', type=float)
    sort_option = request.args.get('sort')  # NEW: Sorting option

    # Use session-stored cuisine/vibe if not selected
    if not request.args:
        selected_cuisine = session.get('selected_cuisine_id')
        selected_vibe = session.get('selected_vibe_id')
    else:
        session['selected_cuisine_id'] = selected_cuisine
        session['selected_vibe_id'] = selected_vibe

    # Connect to database
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Fetch filter options for dropdowns
    cursor.execute("SELECT cuisine_id, name FROM Cuisine")
    cuisines = cursor.fetchall()

    cursor.execute("SELECT vibe_id, name FROM vibetype")
    vibes = cursor.fetchall()

    cursor.execute("SELECT location_id, direction FROM londonlocation")
    locations = cursor.fetchall()

    # Main query with filters
    query = """
    SELECT
        r.restaurant_id,
        r.name,
        r.address,
        r.website,
        r.price_range,
        c.name AS cuisine,
        v.name AS vibe,
        l.direction AS location,
        r.price_range AS price_range,
        AVG(rv.rating) AS avg_rating,
        AVG(rv.ambience) AS avg_ambiance,
        AVG(rv.service) AS avg_service,
        AVG(rv.value_for_money) AS avg_value,
        AVG(rv.location) AS avg_location_rating
    FROM Restaurants r
    JOIN Cuisine c ON r.cuisine_id = c.cuisine_id
    JOIN vibetype v ON r.vibe_id = v.vibe_id
    JOIN londonlocation l ON r.location_id = l.location_id
    LEFT JOIN Review rv ON r.restaurant_id = rv.restaurant_id
    WHERE 
        (%s IS NULL OR r.cuisine_id = %s) AND
        (%s IS NULL OR r.vibe_id = %s) AND
        (%s IS NULL OR r.location_id = %s) AND
        (%s IS NULL OR r.price_range = %s)
    GROUP BY r.restaurant_id
    HAVING
        (%s IS NULL OR avg_rating >= %s) AND
        (%s IS NULL OR avg_ambiance >= %s) AND
        (%s IS NULL OR avg_service >= %s) AND
        (%s IS NULL OR avg_value >= %s) AND
        (%s IS NULL OR avg_location_rating >= %s)
    """

    params = [
        selected_cuisine, selected_cuisine,
        selected_vibe, selected_vibe,
        selected_location, selected_location,
        selected_price_range, selected_price_range,
        selected_rating, selected_rating,
        selected_ambiance, selected_ambiance,
        selected_service, selected_service,
        selected_value, selected_value,
        selected_location_rating, selected_location_rating
    ]

    # Add sorting logic
    if sort_option == 'top5':
        query += " ORDER BY avg_rating DESC LIMIT 5"
    elif sort_option == 'bottom5':
        query += " ORDER BY avg_rating ASC LIMIT 5"
    else:
        query += " ORDER BY avg_rating DESC"  # Default sorting

    # Execute query
    cursor.execute(query, params)
    restaurants = cursor.fetchall()
    conn.close()

    return render_template(
        'all_restaurants.html',
        cuisines=cuisines,
        vibes=vibes,
        locations=locations,
        restaurants=restaurants,
        selected_cuisine=selected_cuisine,
        selected_vibe=selected_vibe,
        selected_location=selected_location,
        selected_rating=selected_rating,
        selected_ambiance=selected_ambiance,
        selected_service=selected_service,
        selected_value=selected_value,
        selected_location_rating=selected_location_rating,
        selected_price_range=selected_price_range,
        sort_option=sort_option  # Pass the sort option for button highlighting
    )


# takes input from the first 2 pages into the filtering criteria,
# interacts with the database to filter based on other criteria (session handling; price, vibe,cuisine,location)
import os
@app.route('/restaurant/<int:id>')
def get_restaurant(id):
    restaurant = find_restaurant(id)
    if restaurant is not None:

        name = restaurant["name"]
        phone_number = restaurant["phone_number"]
        address = restaurant["address"]
        website = restaurant["website"]
        price_range = restaurant["price_range"]
        cuisine = find_cuisine_from_id(restaurant["cuisine_id"])
        vibe = find_vibe_from_id(restaurant["vibe_id"])
        description = restaurant['description']
        menu_link = restaurant['menu_link']
        reviews = get_reviews_by_restaurant_id(id)
        restaurant_id = id

        if cuisine is None:
            cuisine = "Unknown cuisine"

        image_folder = os.path.join(app.static_folder, 'restaurant_images', str(restaurant_id))
        banner_image = None
        carousel_images = []

        if os.path.exists(image_folder):

            banner_path = os.path.join(image_folder, 'banner.jpg')
            if os.path.exists(banner_path):
                banner_image = f'restaurant_images/{restaurant_id}/banner.jpg'
            else:
                banner_image = 'default/banner_default.jpg'  # fallback banner


            carousel_images = [
                f'restaurant_images/{restaurant_id}/{filename}'
                for filename in os.listdir(image_folder)
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')) and filename != 'banner.jpg'
            ]
        else:

            banner_image = 'default/banner_default.jpg'
            carousel_images = []

        return render_template(
            'restaurant.html',
            name=name,
            phone_number=phone_number,
            address=address,
            website=website,
            price_range=price_range,
            cuisine=cuisine,
            vibe=vibe,
            description=description,
            menu_link=menu_link,
            reviews=reviews,
            restaurant_id=restaurant_id,
            banner_image=banner_image,     # pass banner image
            images=carousel_images         # pass carousel images
        )
    else:
        return render_template("404.html")



@app.route('/myreviews')
def reviews():
    if 'email' not in session:
        return redirect(url_for('login'))

    email = session['email']
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Get user_id from email
    cursor.execute("SELECT user_id FROM User WHERE email = %s", (email,))
    user = cursor.fetchone()

    if not user:
        cursor.close()
        conn.close()
        return redirect(url_for('login'))

    user_id = user['user_id']

    # Fetch user's reviews with restaurant names
    cursor.execute("""
        SELECT 
            res.name AS restaurant_name,
            r.Rating, r.Ambience, r.Service, r.Location,
            r.Value_for_money,
            r.Overall_review, r.creation_date
        FROM Review r
        JOIN Restaurants res ON r.restaurant_id = res.restaurant_id
        WHERE r.user_id = %s
        ORDER BY r.creation_date DESC
    """, (user_id,))

    reviews = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('myreviews.html', reviews=reviews)

@app.route("/ethos")
def ethos():
    return render_template("ethos.html", title="Our Ethos")

@app.route("/account")
def account():
    try:
        print(session)
        user_id = session['user_id']
        user = get_user(user_id)
    except KeyError:
        return redirect(url_for('login'))

    user_reviews = get_reviews_by_user(user_id)

    for user_review in user_reviews:
        stars = ""
        for i in range(user_review["Rating"]):
            stars = stars + "⭐"
        user_review["stars"] = stars
        user_review["restaurant_name"] = find_restaurant(user_review["restaurant_id"])["name"]


    return render_template("account.html", title="Account", user_name=user["user_name"], surname=user["surname"],
                           email=user["email"], reviews=user_reviews)



# @app.route('/review/<int:restaurant_id>', methods=['GET', 'POST'])
# # prefilled form with restaurant name
# def review(restaurant_id):
#     restaurant = restaurants.query.get_or_404(restaurant_id)
#
#     if request.method == 'POST':
#         new_review = Review(
#             restaurant_id=restaurant.id,
#             user_id=current_user.id,
#             rating=int(request.form['rating']),
#             comment=request.form['comment']
#         )
#         db.session.add(new_review)
#         db.session.commit()
#         flash('Review added successfully!')
#         return redirect(url_for('restaurant_detail', id=restaurant.id))
#
#     return render_template('review.html', restaurant=restaurant)

@app.route('/review/<int:restaurant_id>', methods=['GET', 'POST'])
def review(restaurant_id):
    restaurant = find_restaurant(restaurant_id)

    if not restaurant:
        return "Restaurant not found", 404

    if request.method == 'POST':
        try:
            user_id = session.get('user_id')  # Make sure user is logged in!
            if not user_id:
                flash('You must be logged in to leave a review.')
                return redirect(url_for('login'))

            overall = int(request.form['overall_rating'])
            ambience = int(request.form['ambience_rating'])
            service = int(request.form['service_rating'])
            location = int(request.form['location_rating'])
            value = int(request.form['value_rating'])
            comment = request.form.get('comment', '')

            # Save to database
            save_review(user_id, restaurant_id, overall, ambience, service, location, value, comment)

            flash('Review submitted successfully!')
            return redirect(url_for('get_restaurant', id=restaurant_id))

        except Exception as e:
            print(e)
            flash('There was an error submitting your review. Please try again.')

    # Always render the form if GET or if POST fails
    return render_template('review_form.html', restaurant=restaurant)


# review url->pass in restaurant id->got into database, get restaurant name, put it in a label
# do stars from bootstrap
# dropdown/stars for different things/ tick boxes (would you go here again?), structure, prepopulate the label


@app.route('/health')
def get_health():
    return "I am healthy"
