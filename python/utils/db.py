import mysql.connector
import os
config = {
  "user": "",
  "password": "",
  "host": "",
  "port": 3306,
  "database": "mysql",
  "ssl_ca": "{path to the .pem file downloaded from Azure}",
  "ssl_disabled": False
}


try:
    # Try to establish a connection
    cnx = mysql.connector.connect(**config)
    
    # Check if the connection is successful
    if cnx.is_connected():
        print("Connection successful!")
        
        # Execute a simple query to test the connection
        cursor = cnx.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print("Query result:", result)
        
    else:
        print("Connection failed.")
        
except mysql.connector.Error as e:
    print("Error connecting to MySQL database:", e)
    
finally:
    # Close the connection
    cnx.close()
