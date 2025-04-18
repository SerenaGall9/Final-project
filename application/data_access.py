# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="persondb"
# )


def main():
    print(mydb)

    cursor = mydb.cursor()

    sql = "INSERT INTO person (firstname, lastname, age) VALUES (%s, %s, %s)"
    val = ("Fred", "Flintstone", 40)
    cursor.execute(sql, val)

    mydb.commit()

    print(cursor.rowcount, "record inserted.")


def get_db_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="persondb"
    )

    return mydb


def add_person(fname, lname, age=25):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO person (firstname, lastname, age) VALUES (%s, %s, %s)"
    val = (fname, lname, age)
    cursor.execute(sql, val)

    conn.commit()


def get_people():
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "Select ID, Firstname, Lastname from person"
    cursor.execute(sql)

    result_set = cursor.fetchall()
    person_list = []
    for person in result_set:
        person_list.append({'ID': person[0], 'Firstname': person[1], 'Lastname': person[2]})
    return person_list


if __name__ == "__main__":
    main()
