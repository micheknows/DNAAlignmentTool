from flask import Flask
import dna_tool2.routes as routes

app = Flask(__name__, template_folder="templates", static_folder='DNAAlignmentTool/static')

app.register_blueprint(routes.dna_tool_bp)


if __name__ == '__main__':
    app.run()
