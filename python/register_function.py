import mysql.connector
from mysql.connector import Error
import hashlib

def register(name, email, password, confirm_password):
    """
    Register a new user in the database.
    """
    if not name or not email or not password or not confirm_password:
        return "All fields are required."
    if password != confirm_password:
        return "Passwords do not match."

    try:
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host
            database='sarawak_tourism',  # Replace with your database name
            user='root',  # Replace with your MySQL username
            password='hello'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Hash the password
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            # Insert the user into the database
            cursor.execute("""
                INSERT INTO users (name, email, password)
                VALUES (%s, %s, %s)
            """, (name, email, hashed_password))
            connection.commit()
            return "Registration successful!"
    except Error as e:
        return f"Error while connecting to the database: {e}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()