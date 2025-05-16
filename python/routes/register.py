from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.db1 import query_db
from flask_bcrypt import Bcrypt
import mysql.connector

register_bp = Blueprint('register', __name__)
bcrypt = Bcrypt()

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Ensure the form contains the expected keys
        if 'username' not in request.form or 'email' not in request.form or 'password' not in request.form:
            flash('Invalid form submission.', 'danger')
            return redirect(url_for('register.register'))

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
            return redirect(url_for('register.register'))

        # Insert the new user into the database
        query = "INSERT INTO Users (username, email, password) VALUES (%s, %s, %s)"
        try:
            query_db(query, (username, email, hashed_password))
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth.login'))
        except mysql.connector.Error as e:
            flash(f'An error occurred: {e}', 'danger')
            return redirect(url_for('register.register'))

    return render_template('register.html')