from flask import Flask, request, jsonify, render_template
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# MySQL Database Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # Your MySQL username
    'password': 'hello',  # Your MySQL password
    'database': 'sarawak_tourism'  # Database name
}

# Initialize MySQL Database
def init_db():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            nric VARCHAR(20) NOT NULL UNIQUE
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            title VARCHAR(255) NOT NULL,
            date_time DATETIME NOT NULL,
            location VARCHAR(255) NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

# Function to add a new appointment
@app.route('/add_appointment', methods=['POST'])
def add_appointment():
    try:
        # Extract data from POST request
        name = request.form['name']
        nric = request.form['nric']
        title = request.form['title']
        date_time = request.form['date_time']  # Expected format: YYYY-MM-DD HH:MM:SS
        location = request.form['location']

        # Validate data
        if not all([name, nric, title, date_time, location]):
            return jsonify({"error": "All fields are required"}), 400

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Check if user exists, if not create a new user
        cursor.execute('SELECT id FROM users WHERE nric = %s', (nric,))
        user = cursor.fetchone()

        if user:
            user_id = user[0]
        else:
            cursor.execute('INSERT INTO users (name, nric) VALUES (%s, %s)', (name, nric))
            user_id = cursor.lastrowid

        # Insert the new appointment
        cursor.execute('''
            INSERT INTO appointments (user_id, title, date_time, location)
            VALUES (%s, %s, %s, %s)
        ''', (user_id, title, date_time, location))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message": "Appointment added successfully"}), 201

    except mysql.connector.Error as e:
        return jsonify({"error": str(e)}), 500

# Web page for adding appointments
@app.route('/')
def index():
    return render_template('index.html')  # A simple HTML form to send data

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
