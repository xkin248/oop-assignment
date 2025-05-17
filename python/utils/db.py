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

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='stdb3.mysql.database.azure.com',
            user='Henry@stdb3',
            password='Hello123',
            database='sarawak_tourism',
            ssl_ca='/workspaces/oop-assignment/python/static/DigiCertGlobalRootCA.crt.pem'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def close_connection(connection):
    if connection and connection.is_connected():
        connection.close()

def get_db_connection():
    try:
        conn = mysql.connector.connect(**config)
        return conn
    except Error as e:
        print("MySQL connection error:", e)
        return None

def query_db(query, args=(), fetch_one=False, commit=False):
    """SELECT / INSERT / UPDATE"""
    conn = get_db_connection()
    if not conn:
        return None
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, args)
    if commit:                 
        conn.commit()
        rv = cursor.lastrowid   
    else:                      
        rv = cursor.fetchone() if fetch_one else cursor.fetchall()
    cursor.close()
    conn.close()
    return rv
