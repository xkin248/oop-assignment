import os
from flask import Flask
from flask_bcrypt import Bcrypt
from sqlalchemy import create_engine, text

# Flask app setup
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'fallback-secret-key')
bcrypt = Bcrypt(app)

# MySQL configuration
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
SSL_CERT = 'DigiCertGlobalRootCA.crt.pem'

# Debug (safe for local dev)
print("🔍 DB_USER:", DB_USER)
print("🔍 DB_HOST:", DB_HOST)
print("🔍 DB_NAME:", DB_NAME)

# Build connection string
if os.path.exists(SSL_CERT):
    connection_string = (
        f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
        f"?ssl_ca={SSL_CERT}"
    )
else:
    connection_string = (
        f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )

# SQLAlchemy engine
engine = create_engine(connection_string)

# Test connection
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("✅ Connected to MySQL:", result.scalar())
except Exception as e:
    print("❌ Database connection failed:", e)
    
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
