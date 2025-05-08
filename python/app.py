from flask import Flask, request, render_template, jsonify
from Login_function import Login  # Import the Login function
from register_function import register  # Import the register function

app = Flask(__name__, template_folder="../UI")  # Set the template folder to serve HTML files

# Route to serve the registration form
@app.route('/')
def home():
    return render_template('register.html')

# Route to handle registration
@app.route('/register', methods=['POST'])
def handle_register():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirmPassword')

    # Call the register function
    result = register(name, email, password, confirm_password)

    # Return the result as a JSON response
    return jsonify({'message': result})

# Route to serve the login page
@app.route('/login')
def login_page():
    return render_template('Login.html')

# Route to handle login
@app.route('/login', methods=['POST'])
def login():
    # Get login data from the request
    email = request.json.get('email')
    password = request.json.get('password')

    # Validate inputs
    if not email or not password:
        return jsonify({"success": False, "message": "Email and password are required."}), 400

    # Call the Login function
    result = Login(email, password)

    if result["success"]:
        return jsonify({"success": True, "message": "Login successful!", "user": result["user"]})
    else:
        return jsonify({"success": False, "message": result["message"]}), 401

# Route to serve the main dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('main_dashboard.html')

# Route to serve the profile creation page
@app.route('/profile')
def profile():
    return render_template('profile_create.html')

# Route to serve the visitor detail page
@app.route('/visitor-detail')
def visitor_detail():
    return render_template('Visitor_Detail.html')

# Route to serve the QR code page
@app.route('/qr-code')
def qr_code():
    return render_template('QR_Code.html')

# Route to serve the QR code scanner page
@app.route('/scan-qr')
def scan_qr():
    return render_template('Scan_QR.html')

# Route to serve the add new appointment page
@app.route('/add-appointment')
def add_appointment():
    return render_template('Add_New_Appointment.html')

# Route to serve today's appointments page
@app.route('/today-appointments')
def today_appointments():
    return render_template('Today_Appointment.html')

# Route to serve the logout confirmation page
@app.route('/logout')
def logout():
    return render_template('LogOut.html')

# Route to serve the preferences page
@app.route('/preferences')
def preferences():
    return render_template('AS_Preferences.html')

# Route to serve the privacy settings page
@app.route('/privacy')
def privacy():
    return render_template('AS_Privacy.html')

# Route to serve the security settings page
@app.route('/security')
def security():
    return render_template('AS_Security.html')

# Route to serve the pay and service page
@app.route('/pay-and-service')
def pay_and_service():
    return render_template('AS_PayAndService.html')

# Route to serve the account settings page
@app.route('/account-settings')
def account_settings():
    return render_template('Account_Setting.html')

# Route to serve the history appointment page
@app.route('/history-appointments')
def history_appointments():
    return render_template('AS_HistoryAppointment.html')

# Route to serve the main page
@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)