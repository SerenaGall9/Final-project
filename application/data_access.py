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
        database="projectdb2"
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

def find_restaurant(id):
    connection = get_db_connection()
    cursor = connection.cursor()

    sql = "SELECT name, address, location_id, phone_number, website, cuisine_id, vibe_id, description, menu_link FROM restaurants WHERE restaurant_id = %s"
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
            'description' :restaurant[7],
            'menu_link' : restaurant[8]
        }
    return None


if __name__ == "__main__":
    main()