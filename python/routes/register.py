from flask import Flask, render_template, request, redirect, flash
from utils.db import query_db

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        gender = request.form['gender']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']

        # Basic validation
        if password != confirm_password:
            flash('Passwords do not match.')
            return render_template('register.html')

        # Insert into DB
        insert_query = """
            INSERT INTO users (username, gender, email, password)
            VALUES (?, ?, ?, ?)
        """
        result = query_db(insert_query, (username, gender, email, password), commit=True)
        if result:
            flash('Registration successful! Please log in.')
            return redirect('/')
        else:
            flash('Registration failed. Email or username may already exist.')
            return render_template('register.html')

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
