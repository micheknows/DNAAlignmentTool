from flask import Flask

def create_app():
    # Initialize the Flask application
    app = Flask(__name__)

    # Import routes from the routes module
    from . import routes

    # Register the routes with the application
    app.register_blueprint(routes.bp)

    return app
