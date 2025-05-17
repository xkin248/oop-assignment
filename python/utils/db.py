import mysql.connector
from mysql.connector import Error

config = {
    "user": "Henry@stdb3",
    "password": "Hello123",
    "host": "stdb3.mysql.database.azure.com",
    "port": 3306,
    "database": "sarawk_tourism",
    "ssl_ca": "/workspaces/oop-assignment/python/static/DigiCertGlobalRootCA.crt.pem",
    "ssl_disabled": False
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except Error as e:
        print("Error connecting to MySQL database:", e)
        return None

def query_db(query, args=(), fetch_one=False):
    conn = get_db_connection()
    if not conn:
        return None
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, args)
    rv = cursor.fetchone() if fetch_one else cursor.fetchall()
    cursor.close()
    conn.close()
    return rv
