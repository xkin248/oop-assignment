from flask import Blueprint, request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from utils.db import create_connection, close_connection

register_bp = Blueprint('register_bp', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')

        if not username or not email or not password or not confirm_password:
            flash('All fields are required.', 'danger')
            return render_template('register.html')

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return render_template('register.html')

        hashed_password = generate_password_hash(password)
        conn = create_connection()
        if conn:
            cursor = conn.cursor()
            # Check if user exists
            cursor.execute("SELECT id FROM Users WHERE username=%s OR email=%s", (username, email))
            if cursor.fetchone():
                flash('Username or email already exists.', 'danger')
                close_connection(conn)
                return render_template('register.html')
            # Insert new user
            cursor.execute(
                "INSERT INTO Users (username, email, password) VALUES (%s, %s, %s)",
                (username, email, hashed_password)
            )
            conn.commit()
            close_connection(conn)
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login.login'))
        else:
            flash('Database connection error.', 'danger')
    return render_template('register.html')