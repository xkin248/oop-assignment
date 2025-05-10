from flask import Blueprint, render_template

ui_bp = Blueprint('ui', __name__)

@ui_bp.route('/account-settings')
def account_settings():
    return render_template('Account_Setting.html')

@ui_bp.route('/add-appointment')
def add_appointment():
    return render_template('Add_New_Appointment.html')

@ui_bp.route('/history-appointments')
def history_appointments():
    return render_template('AS_HistoryAppointment.html')

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