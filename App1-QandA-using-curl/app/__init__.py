import os
import logging
from flask import Flask
from .database import init_db

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def create_app():
    app = Flask(__name__)
    
    # Load configuration from environment variables or defaults
    app.config.from_mapping(
        OPENAI_API_KEY=os.getenv('OPENAI_API_KEY'),
        SLACK_TOKEN=os.getenv('SLACK_TOKEN')
    )

    logger.info("Creating the Flask application and loading configuration.")

    # Initialize the database
    init_db()

    # Register routes
    from .routes import api
    app.register_blueprint(api)

    logger.info("Flask application created and routes registered.")

    return app
