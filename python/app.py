import os
from flask_bcrypt import Bcrypt
from flask import Flask, render_template, session, redirect, url_for, flash
from routes.models import db
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
# Flask app setup
def create_app():
    app = Flask(__name__)

    MYSQL_USER = os.environ.get('MYSQL_USER')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
    MYSQL_HOST = os.environ.get('MYSQL_HOST')
    MYSQL_PORT = os.environ.get('MYSQL_PORT', 3306)
    MYSQL_DB = os.environ.get('MYSQL_DB')
    MYSQL_SSL_CA = os.environ.get('MYSQL_SSL_CA')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key')

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
        f"?ssl_ca={MYSQL_SSL_CA}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = SECRET_KEY

    db.init_app(app)
    return app

app = create_app()
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
