import mysql.connector
import os

def get_db_connection():
    conn = mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "stdb3.mysql.database.azure.com"),
        user=os.environ.get("MYSQL_USER", "Henry@stdb3"),
        password=os.environ.get("MYSQL_PASSWORD", "Hello123"),
        database=os.environ.get("MYSQL_DATABASE", "sarwak_tourism"),
        port=int(os.environ.get("MYSQL_PORT", "3306")),
        ssl_disabled=False
    )
    return conn

def query_db(query, args=(), fetch_one=False, commit=False):
    conn = get_db_connection()
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
