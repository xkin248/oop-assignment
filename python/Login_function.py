import mysql.connector
from mysql.connector import Error

def Login(email, password):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host
            database='sarawak_tourism',  # Replace with your database name
            user='root',  # Replace with your MySQL username
            password='hello'  # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            
            # Query to find the user with the provided email and password
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))  # Use parameterized query to prevent SQL injection
            
            # Fetch user data
            user = cursor.fetchone()
            
            if user:
                return {"success": True, "user": user}  # Return user data for successful login
            else:
                return {"success": False, "message": "Invalid email or password."}

    except Error as e:
        return {"success": False, "message": f"Error while connecting to MySQL: {e}"}
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
email = input("Enter your email: ")
password = input("Enter your password: ")
result = Login(email, password)
if result["success"]:
    print("Login successful!")
    print("User data:", result["user"])
else:
    print(result["message"])
