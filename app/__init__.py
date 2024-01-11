from flask import Flask

import sys
print("Path inside __init__.py within DNA tool:" )
print(sys.path)

def create_app():
    # Initialize the Flask application
    app = Flask(__name__, template_folder="templates", static_folder='DNAAlignmentTool/app/static')

    # Import routes from the routes module
    from . import routes

    # Register the routes with the application
    app.register_blueprint(routes.bp)

    return app
