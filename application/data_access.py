import mysql.connector
from datetime import date

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="projectdb4"
)


def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="projectdb4"
    )

    return mydb

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
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM vibetype WHERE vibe_id = %s"
    cursor.execute(query, (vibe_id,))
    result = cursor.fetchone()  # Might be None if no match
    cursor.close()
    conn.close()  # 🔥 CLOSE IT!

    if result is None:
        print(f"No vibe found with ID: {vibe_id}")
    return result


def get_all_vibes():
        return [
            {"id": 3, "name": "Cozy & Intimate", "image_url": "/static/images/vibes/cosy.png"},
            {"id": 5, "name": "Office Eats", "image_url": "/static/images/vibes/officeeats.png"},
            {"id": 6, "name": "Loud & Lively", "image_url": "/static/images/vibes/loud.png"},
            {"id": 4, "name": "Special Occasion", "image_url": "/static/images/vibes/occassion.png"},
            {"id": 1, "name": "Casual Dining", "image_url": "/static/images/vibes/casual.png"},
            {"id": 2, "name": "Fine Dining", "image_url": "/static/images/vibes/finedining.png"},
        ]


def get_all_cuisines():
    # conn = get_db_connection()
    # cursor = conn.cursor(dictionary=True)
    # cursor.execute("SELECT * FROM cuisine")
    # cuisines = cursor.fetchall()
    # cursor.close()
    # conn.close()
    return [
        {"cuisine_id": 2, "name": "Indian", "image_url": "/static/images/cuisines/indian.png"},
        {"cuisine_id": 1, "name": "Italian", "image_url": "/static/images/cuisines/italian.png"},
        {"cuisine_id": 4, "name": "Lebanese", "image_url": "/static/images/cuisines/lebanese.png"},
        {"cuisine_id": 3, "name": "Japanese", "image_url": "/static/images/cuisines/japanese.png"},
        {"cuisine_id": 5, "name": "Mediterranean", "image_url": "/static/images/cuisines/mediterranean.png"}
    ]


def get_restaurants_by_vibe_and_cuisine(vibe_id, cuisine_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM restaurants WHERE vibe_id = %s AND cuisine_id = %s",
        (vibe_id, cuisine_id)
    )
    restaurants = cursor.fetchall()
    cursor.close()
    conn.close()
    return restaurants


def get_reviews_by_restaurant_id(restaurant_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT review.*, user.user_name AS user_name
        FROM review
        JOIN user ON review.user_id = user.user_id
        WHERE review.restaurant_id = %s
        ORDER BY review.creation_date DESC
    """

    cursor.execute(query, (restaurant_id,))
    reviews = cursor.fetchall()

    cursor.close()
    conn.close()
    return reviews

def find_restaurant(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    sql = "SELECT restaurant_id,name, address, location_id, phone_number, website, price_range, cuisine_id, vibe_id, description, menu_link FROM restaurants WHERE restaurant_id = %s"
    cursor.execute(sql, (id,))

    restaurant = cursor.fetchone()
    connection.close()

    if restaurant:
        return {
            'restaurant_id': restaurant[0],
            'name': restaurant[1],
            'address': restaurant[2],
            'location_id': restaurant[3],
            'phone_number': restaurant[4],
            'website': restaurant[5],
            'price_range': restaurant[6],
            'cuisine_id': restaurant[7],
            'vibe_id': restaurant[8],
            'description':restaurant[9],
            'menu_link': restaurant[10]
        }
    return None


def get_vibe_by_id(vibe_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM vibetype WHERE vibe_id = %s"
    cursor.execute(query, (vibe_id,))

    result = cursor.fetchone()  # Might be None if no match
    cursor.close()

    if result is None:
        print(f"No vibe found with ID: {vibe_id}")
    return result

def save_review(user_id, restaurant_id, overall, ambience, service, location, value, comment):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO review
        (user_id, restaurant_id, Rating, Ambience, Service, Location, Value_for_money, Overall_review, creation_date) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    today = date.today()
    cursor.execute(query, (user_id, restaurant_id, overall, ambience, service, location, value, comment, today))
    conn.commit()
    cursor.close()
    conn.close()




def get_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def get_reviews_by_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM review WHERE user_id = %s ORDER BY creation_date DESC", (user_id,))
    review = cursor.fetchall()
    cursor.close()
    conn.close()
    return review

if __name__ == "__main__":
    main()