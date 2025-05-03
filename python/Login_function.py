import mysql.connector
from mysql.connector import Error

def Login(email, password):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='your_host',       # Replace with your database host
            user='your_username',   # Replace with your MySQL username
            password='your_password', # Replace with your MySQL password
            database='your_database' # Replace with your database name
        )
        
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            
            # Query to find the user with the provided email and password
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))  # Use parameterized query to prevent SQL injection
            
            # Fetch user data
            user = cursor.fetchone()
            
            if user:
                print("Login successful!")
                return True  # Return True for successful login
            else:
                print("Invalid email or password.")
                return False  # Return False for invalid credentials

    except Error as e:
        print(f"Error while connecting to MySQL {e}")
        return False
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
email = input("Enter your email: ")
password = input("Enter your password: ")
Login(email, password)
