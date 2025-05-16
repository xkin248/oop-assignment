from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from utils.db import query_db

ui_bp = Blueprint('ui', __name__)

@ui_bp.route('/account-settings')
def account_settings():
    return render_template('Account_Setting.html')

@ui_bp.route('/add-appointment', methods=['GET', 'POST'])
def add_appointment():
    if request.method == 'POST':
        # Get form data
        user_id = session.get('user_id')  # Ensure the user is logged in
        appointment_date = request.form.get('appointment_date')
        appointment_time = request.form.get('appointment_time')
        description = request.form.get('description')
        location = request.form.get('location')

        if not user_id:
            flash('You must be logged in to add an appointment.', 'danger')
            return redirect(url_for('auth.login'))

        # Insert the appointment into the database with a default status of "Pending"
        query = """
            INSERT INTO Appointments (user_id, appointment_date, appointment_time, description, location, status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        query_db(query, (user_id, appointment_date, appointment_time, description, location, 'Pending'))
        flash('Appointment added successfully! Redirecting to Today Appointment.', 'success')
        return redirect(url_for('ui.today_appointment'))

    return render_template('Add_New_Appointment.html')

@ui_bp.route('/today-appointment')
def today_appointment():
    user_id = session.get('user_id')  # Ensure the user is logged in

    if not user_id:
        flash('You must be logged in to view your appointments.', 'danger')
        return redirect(url_for('auth.login'))

    # Fetch today's appointments for the logged-in user
    query = """
        SELECT * FROM Appointments
        WHERE user_id = %s AND appointment_date = CURDATE()
        ORDER BY appointment_time ASC
    """
    appointments = query_db(query, (user_id,))
    print("Today's Appointments:", appointments)  # Debug statement

    return render_template('Today_Appointment.html', appointments=appointments)

@ui_bp.route('/history-appointments')
def history_appointments():
    user_id = session.get('user_id')  # Ensure the user is logged in

    if not user_id:
        flash('You must be logged in to view your appointments.', 'danger')
        return redirect(url_for('auth.login'))

    # Fetch all past appointments for the logged-in user
    query = """
        SELECT * FROM Appointments
        WHERE user_id = %s AND appointment_date < CURDATE()
        ORDER BY appointment_date DESC, appointment_time DESC
    """
    appointments = query_db(query, (user_id,))
    print("History Appointments:", appointments)  # Debug statement

    return render_template('AS_HistoryAppointment.html', appointments=appointments)

@ui_bp.route('/payment-services')
def payment_services():
    return render_template('AS_PayAndService.html')

@ui_bp.route('/preferences')
def preferences():
    return render_template('AS_Preferences.html')

@ui_bp.route('/privacy')
def privacy():
    return render_template('AS_Privacy.html')

@ui_bp.route('/security')
def security():
    return render_template('AS_Security.html')

@ui_bp.route('/main-dashboard')
def main_dashboard():
    return render_template('main_dashboard.html')

@ui_bp.route('/profile-create')
def profile_create():
    return render_template('profile_create.html')

@ui_bp.route('/qr-code')
def qr_code():
    return render_template('QR_Code.html')