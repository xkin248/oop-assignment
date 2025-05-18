from flask import Blueprint, session, flash, redirect, url_for, render_template

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/main-dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'danger')
        return redirect(url_for('login.login'))
    return render_template('main_dashboard.html')
