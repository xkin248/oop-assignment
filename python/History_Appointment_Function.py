from flask import Flask, render_template, session, g
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection
def get_db_connection():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="hello",
            database="sarawak_tourism"
        )
    return g.db

# Fetch history appointments
@app.route('/history_appointments')
def history_appointments():
    # Ensure the user is logged in
    if 'user_id' not in session:
        return "Please log in to view your appointments", 401

    user_id = session['user_id']
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    # Query to fetch appointment data for the current user
    query = """
    SELECT title, date_time, location, name, nric
    FROM appointments
    WHERE user_id = %s
    ORDER BY date_time DESC
    """
    cursor.execute(query, (user_id,))
    appointments = cursor.fetchall()

    cursor.close()
    return render_template('AS_HistoryAppointment.html', appointments=appointments)

# Close database connection after each request
@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)
