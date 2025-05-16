from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from utils.db1 import query_db
from flask_bcrypt import Bcrypt

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

@auth_bp.route('/login', methods=['GET', 'POST'])
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
            flash('Login successful!', 'success')  # Flash success message
            return redirect(url_for('ui.main_dashboard'))  # Redirect to main dashboard
        else:
            flash('Invalid email/username or password', 'danger')  # Flash error message

    return render_template('Login.html')