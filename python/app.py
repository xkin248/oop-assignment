import os
from flask import Flask
from flask_bcrypt import Bcrypt

# Flask app setup
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'fallback-secret-key')
bcrypt = Bcrypt(app)

# Register routes
from routes.home import home_bp
from routes.auth import auth_bp
from routes.register import register_bp
from routes.dashboard import dashboard_bp
from routes.logout import logout_bp
from routes.ui_routes import ui_bp

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(register_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(ui_bp)

# Azure best practice: Use gunicorn for production, only use Flask's built-in server for local dev
def main():
    app.run(debug=os.environ.get('FLASK_DEBUG', 'False') == 'True')

if __name__ == '__main__':
    main()
