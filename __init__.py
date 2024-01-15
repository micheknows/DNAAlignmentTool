

from flask import Blueprint, render_template

dna_tool = Blueprint('dna_tool', __name__,
                    template_folder="templates",
                    static_folder='static', url_prefix='/dna_tool')

from . import routes


@dna_tool.route('/test')
def dna_index2():
    return "hiya"

