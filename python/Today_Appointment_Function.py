from flask import Flask, render_template
import mysql.connector
from datetime import date

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'hello',
    'database': 'sarawak_tourism'
}

@app.route('/today-appointment')
def today_appointment():
    try:
        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        # Get today's date
        today = date.today()

        # Query to fetch today's appointments
        query = """
        SELECT title, appointment_time, location, name, nric
        FROM appointments
        WHERE DATE(appointment_time) = %s
        """
        cursor.execute(query, (today,))
        appointments = cursor.fetchall()

        # Close the connection
        cursor.close()
        connection.close()

        # Render the template with appointment data
        return render_template('Today_Appointment.html', appointments=appointments)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "An error occurred while fetching appointments."

if __name__ == '__main__':
    app.run(debug=True)
