from flask import Blueprint, session, flash, redirect, url_for, render_template, request

logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('login.login'))

@logout_bp.route('/logout-confirm')
def logout_confirm():
    return render_template('LogOut.html')
