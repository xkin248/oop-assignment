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
        print("MySQL 连接错误:", e)
        return None

def query_db(query, args=(), fetch_one=False, commit=False):
    """SELECT / INSERT / UPDATE"""
    conn = get_db_connection()
    if not conn:
        return None
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, args)
    if commit:                 # 对于写操作提交
        conn.commit()
        rv = cursor.lastrowid   # 返回插入行 id
    else:                      # 读操作返回记录
        rv = cursor.fetchone() if fetch_one else cursor.fetchall()
    cursor.close()
    conn.close()
    return rv
