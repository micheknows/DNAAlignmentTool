

from flask import Blueprint

dna_tool = Blueprint('dna_tool', __name__,
                    template_folder="app/templates",
                    static_folder='app/static', url_prefix='/dna-tool')
print(dna_tool)

from .dna_app import routes

@dna_tool.route('/test')
def test():
    return "DNA Blueprint Works!"

