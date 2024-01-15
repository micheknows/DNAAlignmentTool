

from flask import Blueprint

dna_tool = Blueprint('dna_tool', __name__,
                    template_folder="dna_app/templates",
                    static_folder='dna_app/static', url_prefix='/dna-tool')


from .dna_app import routes

@dna_tool.route('/test')
def test():
    return "DNA Blueprint Works!"

