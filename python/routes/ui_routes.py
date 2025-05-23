from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from utils.db import query_db
from routes.demo import Appointment, OnlineAppointment

ui_bp = Blueprint('ui', __name__)

@ui_bp.route('/new-appointment', methods=['GET', 'POST'])
def new_appointment():
    if request.method == 'POST':
        user_id = session.get('user_id')  # Get logged-in user's ID
        title = request.form.get('title')
        appointment_date = request.form.get('appointment_date')
        appointment_time = request.form.get('appointment_time')
        description = request.form.get('description')
        location = request.form.get('location')

        if not user_id:
            flash('You must be logged in to add an appointment.', 'danger')
            return redirect(url_for('login.login'))

        if not title:
            flash('Title is required to add an appointment.', 'danger')
            return redirect(url_for('ui.new_appointment'))

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
        return redirect(url_for('ui.list_appointment'))

    return render_template('Add_New_Appointment.html')

@ui_bp.route('/appointment-list')
def list_appointment():
    user_id = session.get('user_id')  # Ensure the user is logged in

    if not user_id:
        flash('You must be logged in to view your appointments.', 'danger')
        return redirect(url_for('login.login'))

    # Fetch all appointments for all users, both past and future
    query = """
        SELECT * FROM dbo.Appointments
        WHERE user_id = ?
        ORDER BY appointment_date DESC, appointment_time DESC
    """
    appointments = query_db(query, (user_id,))
    print("Appointments List:", appointments)  # Debug statement

    return render_template('list.html', appointments=appointments)

@ui_bp.route('/main-dashboard')
def main_dashboard():
    return render_template('main_dashboard.html')

@ui_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login.login'))

@ui_bp.route('/oop-demo')
def oop_demo():
    try:
        appt1 = Appointment("Dentist Visit", "2025-05-21", "10:00", "Clinic", "Routine checkup")
        appt2 = OnlineAppointment("Team Meeting", "2025-05-22", "14:00", "Home", "Monthly sync", "https://meet.link")
        appointments = [appt1, appt2]
        details = [a.get_details() for a in appointments]
        return "<br>".join(details)
    except Exception as e:
        return f"Error: {e}"