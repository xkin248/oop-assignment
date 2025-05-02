import mysql.connector
from mysql.connector import Error

def connect_to_database(host, database, user, password):
    """
    Connect to the MySQL database.
    """
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return None

def insert_visitor(connection):
    """
    Insert visitor information into the database.
    """
    try:
        cursor = connection.cursor()
        name = input("Enter visitor's name: ")
        contact_info = input("Enter visitor's contact info: ")
        visit_date = input("Enter visit date (YYYY-MM-DD): ")
        visited_spots = input("Enter visited spots (comma-separated): ")

        cursor.execute("""
            INSERT INTO Visitors (name, contact_info, visit_date, visited_spots)
            VALUES (%s, %s, %s, %s)
        """, (name, contact_info, visit_date, visited_spots))
        connection.commit()
        print(f"Visitor {name} added successfully.")
    except Error as e:
        print(f"Error while inserting visitor: {e}")

def view_visitors(connection):
    """
    View all visitors in the database.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Visitors")
        rows = cursor.fetchall()
        print("Visitors:")
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error while fetching visitors: {e}")

def delete_visitor(connection):
    """
    Delete a visitor from the database.
    """
    try:
        cursor = connection.cursor()
        visitor_id = input("Enter the ID of the visitor to delete: ")
        cursor.execute("DELETE FROM Visitors WHERE id = %s", (visitor_id,))
        connection.commit()
        print(f"Visitor with ID {visitor_id} deleted successfully.")
    except Error as e:
        print(f"Error while deleting visitor: {e}")

def main():
    """
    Main function to connect to the database and manage visitor information.
    """
    # Replace with your database credentials
    host = "localhost"
    database = "sarawak_tourism"
    user = "visitor"
    password = "your_password"  # Replace with the correct password

    # Connect to the database
    connection = connect_to_database(host, database, user, password)
    if connection:
        while True:
            print("\nVisitor Management System")
            print("1. Add Visitor")
            print("2. View Visitors")
            print("3. Delete Visitor")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                insert_visitor(connection)
            elif choice == "2":
                view_visitors(connection)
            elif choice == "3":
                delete_visitor(connection)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

        # Close the connection
        if connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    main()