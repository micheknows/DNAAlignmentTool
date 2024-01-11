from flask import Flask
import app.routes as routes

app = Flask(__name__, template_folder="app/templates", static_folder='app/static')

app.register_blueprint(routes.dna_tool_bp)


if __name__ == '__main__':
    app.run()
