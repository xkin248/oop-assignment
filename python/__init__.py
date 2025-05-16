from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hello'  # Change in production!

    # Register blueprints
    from python.routes.auth import auth_bp
    from python.routes.home import home_bp
    from python.routes.dashboard import dashboard_bp
    from python.routes.logout import logout_bp
    from python.routes.register import register_bp
    from python.routes.ui_routes import ui_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(logout_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(ui_bp)

    return app