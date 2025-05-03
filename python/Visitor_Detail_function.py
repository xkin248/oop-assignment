import mysql.connector
from mysql.connector import Error

def fetch_visitor_details():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',  # Update with your database host
            user='your_username',  # Update with your MySQL username
            password='your_password',  # Update with your MySQL password
            database='your_database'  # Update with your database name
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            
            # Query to fetch visitor details
            query = "SELECT * FROM visitors"  # Replace 'visitors' with your table name
            cursor.execute(query)
            records = cursor.fetchall()
            
            # Generate HTML content
            html_content = """
            <html>
            <head>
                <title>Visitor Details</title>
            </head>
            <body>
                <h1>Visitor Details</h1>
                <table border="1">
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Phone</th>
                        <th>Address</th>
                    </tr>
            """
            
            for row in records:
                html_content += f"""
                <tr>
                    <td>{row['id']}</td>
                    <td>{row['name']}</td>
                    <td>{row['email']}</td>
                    <td>{row['phone']}</td>
                    <td>{row['address']}</td>
                </tr>
                """
            
            html_content += """
                </table>
            </body>
            </html>
            """
            
            # Write HTML content to a file
            with open('Visitor_Detail.html', 'w') as file:
                file.write(html_content)
            
            print("Visitor details have been written to 'Visitor_Detail.html' successfully.")
    
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def update_visitor_details(visitor_id, name=None, email=None, phone=None, address=None):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',  # Update with your database host
            user='your_username',  # Update with your MySQL username
            password='your_password',  # Update with your MySQL password
            database='your_database'  # Update with your database name
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Build the UPDATE query dynamically
            update_fields = []
            if name:
                update_fields.append(f"name = '{name}'")
            if email:
                update_fields.append(f"email = '{email}'")
            if phone:
                update_fields.append(f"phone = '{phone}'")
            if address:
                update_fields.append(f"address = '{address}'")
            
            if update_fields:
                query = f"UPDATE visitors SET {', '.join(update_fields)} WHERE id = {visitor_id}"
                cursor.execute(query)
                connection.commit()
                print(f"Visitor ID {visitor_id} details have been updated successfully.")
            else:
                print("No fields to update.")

    except Error as e:
        print("Error while connecting to MySQL or updating data", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example Usage
fetch_visitor_details()
update_visitor_details(visitor_id=1, name="Jane Doe", email="jane.doe@example.com", phone="9876543210", address="456 Another St")
