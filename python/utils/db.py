import mysql.connector
import os

def get_db_connection():
    # Path to the Azure CA certificate (update this path as needed)
    ssl_ca = os.environ.get("MYSQL_SSL_CA", "/path/to/BaltimoreCyberTrustRoot.crt.pem")
    conn = mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "stdb3.mysql.database.azure.com"),
        user=os.environ.get("MYSQL_USER", "Henry@stdb3"),
        password=os.environ.get("MYSQL_PASSWORD", "Hello123"),
        database=os.environ.get("MYSQL_DATABASE", "stdb3"),
        port=int(os.environ.get("MYSQL_PORT", "3306")),
        ssl_ca=ssl_ca,
        ssl_verify_cert=True
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
