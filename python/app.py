import os
from flask import Flask
from flask_bcrypt import Bcrypt
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables from .env (only in local dev)
load_dotenv()

# Flask app setup
app = Flask(__name__)
bcrypt = Bcrypt(app)

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
