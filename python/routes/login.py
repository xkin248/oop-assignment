from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from utils.db import create_connection, close_connection

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form.get('identifier')
        password = request.form.get('password')
        if not identifier or not password:
            flash('Username/email and password are required.', 'danger')
            return redirect(url_for('login.login'))

        conn = create_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                "SELECT * FROM Users WHERE username=%s OR email=%s",
                (identifier, identifier)
            )
            user = cursor.fetchone()
            close_connection(conn)
            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                flash('Login successful!', 'success')
                return redirect(url_for('ui.main_dashboard'))
            else:
                flash('Invalid email/username or password.', 'danger')
        else:
            flash('Database connection error.', 'danger')
    return render_template('login.html')