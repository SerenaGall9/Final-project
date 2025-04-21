import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="projectdb2"
)


def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="projectdb3"
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
    connection = get_db_connection()
    cursor = connection.cursor()

    sql = "SELECT name FROM vibetype WHERE vibe_id = %s"

    cursor.execute(sql, (vibe_id,))
    vibe = cursor.fetchone()
    connection.close()

    if vibe is not None:
        return vibe[0]
    return None

def get_all_vibes():
    return [
        {"id": 1, "name": "Cozy & Intimate", "image_url": "/static/images/vibes/cosy.png"},
        {"id": 2, "name": "Office Eats", "image_url": "/static/images/vibes/officeeats.png"},
        {"id": 3, "name": "Loud & Lively", "image_url": "/static/images/vibes/loud.png"},
        {"id": 4, "name": "Special Occasion", "image_url": "/static/images/vibes/occassion.png"},
        {"id": 5, "name": "Casual Dining", "image_url": "/static/images/vibes/casual.png"},
        {"id": 6, "name": "Fine Dining", "image_url": "/static/images/vibes/finedining.png"},
    ]

def get_all_cuisines():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cuisine")
    cuisines = cursor.fetchall()
    cursor.close()
    conn.close()
    return cuisines


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

def save_review(restaurant_id, overall, ambience, service, location, value, comment):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO reviews 
        (restaurant_id, overall_rating, ambience_rating, service_rating, location_rating, value_rating, comment) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (restaurant_id, overall, ambience, service, location, value, comment))
    conn.commit()
    cursor.close()
    conn.close()


def get_reviews_by_restaurant_id(restaurant_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM reviews WHERE restaurant_id = %s ORDER BY timestamp DESC", (restaurant_id,))
    reviews = cursor.fetchall()
    cursor.close()
    conn.close()
    return reviews

def find_restaurant(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    sql = "SELECT name, address, location_id, phone_number, website, price_range, cuisine_id, vibe_id, description, menu_link FROM restaurants WHERE restaurant_id = %s"
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
            'price_range': restaurant[5],
            'cuisine_id': restaurant[6],
            'vibe_id': restaurant[7],
            'description' :restaurant[8],
            'menu_link' : restaurant[9]
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

if __name__ == "__main__":
    main()