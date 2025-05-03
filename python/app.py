from flask import Flask, request, render_template, jsonify
from Login_function import Login  # Import the Login function

app = Flask(__name__, template_folder="../UI")  # Set the template folder to serve HTML files

# Route to serve the login page
@app.route('/')
def home():
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

if __name__ == '__main__':
    app.run(debug=True, port=5000)