from flask import Blueprint, request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from utils.db import query_db

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
        # Check if user exists
        user_exists = query_db(
            "SELECT id FROM dbo.Users WHERE username=? OR email=?",
            (username, email),
            fetch_one=True
        )
        if user_exists:
            flash('Username or email already exists.', 'danger')
            return render_template('register.html')

        # Insert new user
        query_db(
            "INSERT INTO dbo.Users (username, email, password) VALUES (?, ?, ?)",
            (username, email, hashed_password),
            commit=True
        )
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login.login'))
    return render_template('register.html')
