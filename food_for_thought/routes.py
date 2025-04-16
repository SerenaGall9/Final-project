from flask import request, redirect, url_for, render_template, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from flask import flash
from flask import render_template, url_for, request, redirect, session

from food_for_thought import app
from datetime import datetime

# @app.route('/')
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         user = User.query.filter_by(email=request.form['email']).first()
#         if user and check_password_hash(user.password, request.form['password']):
#             login_user(user)
#             return redirect(url_for('profile'))
#         flash('Invalid credentials.')
#     return render_template('layout2.html')
#
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('home'))
#
# @app.route('/vibes')
# def get_vibes():
#     return render_template('layout2.html')
# # banner, carousel, confirm button, I can't choose button
#
# @app.route('/cuisines')
# def get_cuisine():
#     return render_template(cuisines.html)
# # dynamic dropdown menu, back button, I can't choose button
#
#
# @app.route('/all_restaurants')
# def get_all_restaurants():
#     return render_template(all_restaurants.html)
# # takes input from the first 2 pages into the filtering criteria,
# # interacts with the database to filter based on other criteria (session handling; price, vibe,cuisine,location)
#
#
#
# @app.route('/all_restaurants/<int:restaurant_id>')
# # this needs to display the signle restaurant page with image, menu link, details, leave review button and reviews from database
# def restaurant_by_id(restaurant_id):
#     # Fetch the project from the database
#     restaurants = get_restaurant_by_id(restaurant_id)
#
#     if not restaurant:
#         return render_template('404.html'), 404
#
#     # Time-based greeting
#     time_slot = get_time_of_day(datetime.now().hour)
#
#     # Get all projects to create next/previous navigation links
#     all_restaurants = get_restaurants()
#     total = len(all_restaurants)
#
#     # Generate URLs for next and previous projects
#     next_url = url_for('restaurant_by_id', restaurant_id=restaurant_id + 1) if restaurant_id + 1 < 4 else None
#     previous_url = url_for('restaurant_by_id', restaraunt_id=restaurant_id - 1) if restaurant_id > 0 else None
#
#
#     return render_template(
#         'restaurant.html',  # Render project.html
#         restaurant=restaurant,
#         time_slot=time_slot,
#         next_url=next_url,
#         previous_url=previous_url,
#         image_src=image_src,
#         image_gif=image_gif,
#         title=restaurant['name']
#     )
#
# @app.route('/restaurant_detail/<int:restaurant_id>')
# def restaurant_detail(restaurant_id):
#     # Fetch the restaurant from the database by its ID
#     restaurant = get_restaurant_by_id(restaurant_id)
#
#     if not restaurant:
#         return render_template('404.html'), 404  # Handle the case where the restaurant doesn't exist
#
#     return render_template('restaurant_details.html', project=restaurant)
#
#
# @app.route('/account')
# def get_account():
#     return render_template('account.html')
#
# @app.route('/review/<int:restaurant_id>', methods=['GET', 'POST'])
# # prefilled form with restaurant name
# @login_required
# def review(restaurant_id):
#     restaurant = Restaurant.query.get_or_404(restaurant_id)
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
#
# # review url->pass in restaurant id->got into database, get restaurant name, put it in a label
# # do stars from bootstrap
# # dropdown/stars for different things/ tick boxes (would you go here again?), structure, prepopulate the label


@app.route('/health')
def get_health():
    return "I am healthy"
