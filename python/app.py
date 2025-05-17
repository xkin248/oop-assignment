import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
from utils.db import query_db
import mysql.connector

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Home route
@app.route('/')
def home():
    return redirect(url_for('login'))

# Auth routes
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form.get('identifier')  # Can be email or username
        password = request.form.get('password')

        # Check if identifier is an email or username
        if '@' in identifier:
            query = "SELECT * FROM Users WHERE email = %s"
        else:
            query = "SELECT * FROM Users WHERE username = %s"

        user = query_db(query, (identifier,), fetch_one=True)

        if user and bcrypt.check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            flash('Login successful!', 'success')
            return redirect(url_for('main_dashboard'))
        else:
            flash('Invalid email/username or password', 'danger')

    return render_template('Login.html')

# Register routes
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if 'username' not in request.form or 'email' not in request.form or 'password' not in request.form:
            flash('Invalid form submission.', 'danger')
            return redirect(url_for('register'))

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Check if username or email already exists
        existing_user = query_db("SELECT * FROM Users WHERE username = %s OR email = %s", (username, email), fetch_one=True)
        if existing_user:
            if existing_user['username'] == username:
                flash('Username already exists. Please choose a different one.', 'danger')
            elif existing_user['email'] == email:
                flash('Email already exists. Please use a different one.', 'danger')
            return redirect(url_for('register'))

        # Insert the new user into the database
        query = "INSERT INTO Users (username, email, password) VALUES (%s, %s, %s)"
        try:
            query_db(query, (username, email, hashed_password))
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except mysql.connector.Error as e:
            flash(f'An error occurred: {e}', 'danger')
            return redirect(url_for('register'))

    return render_template('register.html')

# Dashboard route
@app.route('/main-dashboard')
def main_dashboard():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'danger')
        return redirect(url_for('login'))
    return render_template('main_dashboard.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

# UI routes
@app.route('/account-settings')
def account_settings():
    return render_template('Account_Setting.html')

@app.route('/add-appointment', methods=['GET', 'POST'])
def add_appointment():
    if request.method == 'POST':
        user_id = session.get('user_id')
        appointment_date = request.form.get('appointment_date')
        appointment_time = request.form.get('appointment_time')
        description = request.form.get('description')
        location = request.form.get('location')

        if not user_id:
            flash('You must be logged in to add an appointment.', 'danger')
            return redirect(url_for('login'))

        query = """
            INSERT INTO Appointments (user_id, appointment_date, appointment_time, description, location, status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        query_db(query, (user_id, appointment_date, appointment_time, description, location, 'Pending'))
        flash('Appointment added successfully! Redirecting to Today Appointment.', 'success')
        return redirect(url_for('today_appointment'))

    return render_template('Add_New_Appointment.html')

@app.route('/today-appointment')
def today_appointment():
    user_id = session.get('user_id')
    if not user_id:
        flash('You must be logged in to view your appointments.', 'danger')
        return redirect(url_for('login'))

    query = """
        SELECT * FROM Appointments
        WHERE user_id = %s AND appointment_date = CURDATE()
        ORDER BY appointment_time ASC
    """
    appointments = query_db(query, (user_id,))
    return render_template('Today_Appointment.html', appointments=appointments)

@app.route('/history-appointments')
def history_appointments():
    user_id = session.get('user_id')
    if not user_id:
        flash('You must be logged in to view your appointments.', 'danger')
        return redirect(url_for('login'))

    query = """
        SELECT * FROM Appointments
        WHERE user_id = %s AND appointment_date < CURDATE()
        ORDER BY appointment_date DESC, appointment_time DESC
    """
    appointments = query_db(query, (user_id,))
    return render_template('AS_HistoryAppointment.html', appointments=appointments)

@app.route('/payment-services')
def payment_services():
    return render_template('AS_PayAndService.html')

@app.route('/preferences')
def preferences():
    return render_template('AS_Preferences.html')

@app.route('/privacy')
def privacy():
    return render_template('AS_Privacy.html')

@app.route('/security')
def security():
    return render_template('AS_Security.html')

@app.route('/profile-create')
def profile_create():
    return render_template('profile_create.html')

@app.route('/qr-code')
def qr_code():
    return render_template('QR_Code.html')

# Azure best practice: Use gunicorn for production, only use Flask's built-in server for local dev
def main():
    app.run(debug=os.environ.get('FLASK_DEBUG', 'False') == 'True')

if __name__ == '__main__':
    main()