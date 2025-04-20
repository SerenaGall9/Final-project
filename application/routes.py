from flask import Flask, render_template, session, redirect, url_for
import mysql.connector

from application import app


def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='your_mysql_user',
        password='your_mysql_password',
        database='ProjectDB3'
    )

@app.route('/account')
def account():
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Ensure user is logged in

    user_id = session['user_id']
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Join Reviews with Restaurants
    cursor.execute("""
        SELECT 
            res.name AS restaurant_name,
            r.Rating, r.Ambience, r.Service, r.Location,
            r.Value_for_money, r.price_range,
            r.Overall_review, r.creation_date
        FROM Review r
        JOIN Restaurants res ON r.restaurant_id = res.restaurant_id
        WHERE r.user_id = %s
        ORDER BY r.creation_date DESC
    """, (user_id,))

    reviews = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('account.html', reviews=reviews)