from flask import Blueprint,render_template

bp = Blueprint('shaderinfo', __name__, url_prefix='/shaderinfo')

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/testcode')
def testcode():
    return render_template('testcode.html')