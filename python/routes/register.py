from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from utils.db import query_db
import mysql.connector

register_bp = Blueprint('register', __name__)
bcrypt = Bcrypt()

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        query = "INSERT INTO Users (username, password) VALUES (%s, %s)"
        try:
            query_db(query, (username, hashed_password))
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth.login'))
        except mysql.connector.IntegrityError:
            flash('Username already exists. Please choose a different one.', 'danger')
    return render_template('register.html')