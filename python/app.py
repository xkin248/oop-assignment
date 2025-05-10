from flask import Flask
from flask_bcrypt import Bcrypt

# Import blueprints
from routes.home import home_bp
from routes.auth import auth_bp
from routes.register import register_bp
from routes.dashboard import dashboard_bp
from routes.logout import logout_bp
from routes.ui_routes import ui_bp  # Import the new UI routes

app = Flask(__name__)
app.secret_key = 'hello'  # Replace with a secure key
bcrypt = Bcrypt(app)

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(register_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(ui_bp)  # Register the new UI routes

if __name__ == '__main__':
    app.run(debug=True)