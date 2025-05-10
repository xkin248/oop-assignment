import mysql.connector

db_config = {
    "host": "127.0.0.1",
    "user": "root",  # Replace with your MySQL username
    "password": "hello",  # Replace with your MySQL password
    "database": "sarawak_tourism"
}

def query_db(query, args=None, fetch_one=False):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, args or ())
    if fetch_one:
        result = cursor.fetchone()
    else:
        result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result