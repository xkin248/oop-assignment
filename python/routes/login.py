from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from .models import db, User
from flask_bcrypt import Bcrypt

login_bp = Blueprint('login', __name__)
bcrypt = Bcrypt()

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form.get('identifier')
        password = request.form.get('password')
        if not identifier or not password:
            flash('Username/email and password are required.', 'danger')
            return redirect(url_for('login.login'))

        user = User.query.filter((User.username == identifier) | (User.email == identifier)).first()
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('templates.main_dashboard'))
        else:
            flash('Invalid email/username or password.', 'danger')
            
    return render_template('Login.html')