from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="your_user",
    password="your_password",
    database="projectdb"
)
cursor = conn.cursor(dictionary=True)

@app.route('/top-service')
def top_service_restaurants():
    query = """
        SELECT 
            r.restaurant_id, 
            res.name,
            AVG(r.Service) AS avg_service_rating,
            COUNT(*) AS num_reviews
        FROM Review r
        JOIN Restaurants res ON r.restaurant_id = res.restaurant_id
        GROUP BY r.restaurant_id
        ORDER BY avg_service_rating DESC
        LIMIT 5;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    return render_template("top_service.html", restaurants=results)