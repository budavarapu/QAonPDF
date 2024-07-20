from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config.from_object('config.Config')

    # Register blueprints
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app

