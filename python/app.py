import os
from flask import Flask
from flask_bcrypt import Bcrypt
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import mysql.connector

# Load environment variables from .env (only in local dev)
load_dotenv()

# Flask app setup
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'fallback-secret-key')  # <-- Add this line
bcrypt = Bcrypt(app)

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
            database=os.environ['MYSQL_DATABASE'],
            ssl_ca=os.environ.get('MYSQL_SSL_CA')  # Optional, if using SSL
        )
        if connection.is_connected():
            return connection
    except Exception as e:
        print(f"Error: {e}")
        return None
    
# Register routes
from routes.home import home_bp
from routes.login import login_bp  
from routes.register import register_bp
from routes.dashboard import dashboard_bp
from routes.logout import logout_bp
from routes.ui_routes import ui_bp

app.register_blueprint(home_bp)
app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(ui_bp)

# Run server
if __name__ == '__main__':
    app.run(debug=True)
