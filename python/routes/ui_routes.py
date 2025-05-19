from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from utils.db import query_db

ui_bp = Blueprint('ui', __name__)

@ui_bp.route('/new-appointment', methods=['GET', 'POST'])
def new_appointment():
    if request.method == 'POST':
        user_id = session.get('user_id')  # Get logged-in user's ID
        title = request.form.get('title')
        appointment_date = request.form.get('appointment_date')
        appointment_time = request.form.get('appointment_time')r
        description = request.form.get('description')
        location = request.form.get('location')

        if not user_id:
            flash('You must be logged in to add an appointment.', 'danger')
            return redirect(url_for('login.login'))

        if not title:
            flash('Title is required to add an appointment.', 'danger')
            return redirect(url_for('ui.add_new_appointment'))

        # Insert into database
        query = """
            INSERT INTO Appointments (user_id, title, appointment_date, appointment_time, location, description, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        query_db(
            query,
            (user_id, title, appointment_date, appointment_time, location, description, 'Pending'),
            commit=True
        )
        flash('Appointment added successfully! Redirecting to Appointment List.', 'success')
        return redirect(url_for('ui.list'))

    return render_template('Add_New_Appointment.html')

@ui_bp.route('/appointment-list')
def history_appointments():
    user_id = session.get('user_id')  # Ensure the user is logged in

    if not user_id:
        flash('You must be logged in to view your appointments.', 'danger')
        return redirect(url_for('login.login'))

    # Fetch all past appointments for the logged-in user
    query = """
        SELECT * FROM Appointments
        WHERE user_id = ? AND appointment_date < CAST(GETDATE() AS DATE)
        ORDER BY appointment_date DESC, appointment_time DESC
    """
    appointments = query_db(query, (user_id,))
    print("Appointments List:", appointments)  # Debug statement

    return render_template('list.html', appointments=appointments)

@ui_bp.route('/main-dashboard')
def main_dashboard():
    return render_template('main_dashboard.html')

@ui_bp.route('/profile-create')
def profile_create():
    return render_template('profile_create.html')

@ui_bp.route('/logout-confirm')
def logout_confirm():
    return render_template('LogOut.html')