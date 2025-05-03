import mysql.connector
from mysql.connector import Error

def create_user_profile(full_name, gender, passport_no, phone_number, reason_for_visit):
    """
    Save user profile information to the database.

    Parameters:
        full_name (str): Full name of the user.
        gender (str): Gender of the user.
        passport_no (str): Passport number of the user.
        phone_number (str): Phone number of the user.
        reason_for_visit (str): Reason for the user's visit.
    """
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host
            database='sarawak_tourism',  # Replace with your database name
            user='root',  # Replace with your MySQL username
            password='hello'  # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()

            # Define the SQL query to insert user profile data
            query = """
            INSERT INTO user_profiles (full_name, gender, passport_no, phone_number, reason_for_visit)
            VALUES (%s, %s, %s, %s, %s)
            """
            
            # Execute the query with user data
            cursor.execute(query, (full_name, gender, passport_no, phone_number, reason_for_visit))
            
            # Commit the transaction
            connection.commit()
            print("User profile has been successfully saved.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")

# Example usage
if __name__ == "__main__":
    # Sample data
    full_name = "John Doe"
    gender = "Male"
    passport_no = "A1234567"
    phone_number = "+1234567890"
    reason_for_visit = "Business"

    # Create profile
    create_user_profile(full_name, gender, passport_no, phone_number, reason_for_visit)
