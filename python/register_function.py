import mysql.connector
from mysql.connector import Error
import re
import hashlib

def register(name, email, password, confirm_password):
    # Validate inputs
    if not name.strip():
        return "Name cannot be empty."
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "Invalid email format."
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if password != confirm_password:
        return "Passwords do not match."

    # Hash the password for security
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        # Establish a database connection
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host
            database='your_database',  # Replace with your database name
            user='your_username',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Check if the email is already registered
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            if cursor.fetchone():
                return "Email is already registered."

            # Insert the user information into the database
            insert_query = """
                INSERT INTO users (name, email, password)
                VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (name, email, hashed_password))
            connection.commit()

            return "Registration successful!"

    except Error as e:
        return f"Error while connecting to the database: {e}"

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
if __name__ == "__main__":
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    result = register(name, email, password, confirm_password)
    print(result)
