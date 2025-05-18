from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from utils.db import query_db

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form.get('identifier')
        password = request.form.get('password')
        if not identifier or not password:
            flash('Username/email and password are required.', 'danger')
            return redirect(url_for('login.login'))

        user = query_db(
            "SELECT * FROM dbo.Users WHERE username=%s OR email=%s",
            (identifier, identifier),
            fetch_one=True
        )
        print("Queried user:", user)  # Debug line

        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            flash('Login successful!', 'success')
            return redirect(url_for('ui.main_dashboard'))
        else:
            flash('Invalid email/username or password.', 'danger')
    return render_template('Login.html')
