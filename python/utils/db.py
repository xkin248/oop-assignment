import mysql.connector
import os

def get_db_connection():
    conn = mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "sarawaktourismdb.mysql.database.azure.com"),
        user=os.environ.get("MYSQL_USER", "Henry@sarawaktourismdb"),
        password=os.environ.get("MYSQL_PASSWORD", "Mesopro123"),
        database=os.environ.get("MYSQL_DATABASE", "sarawaktourismdb"),
        port=int(os.environ.get("MYSQL_PORT", "3306")),
        ssl_ca=os.environ.get("MYSQL_SSL_CA", "DigiCertGlobalRootCA.crt.pem"),
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