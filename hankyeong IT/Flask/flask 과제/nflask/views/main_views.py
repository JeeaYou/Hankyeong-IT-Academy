from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/movie')
def movie():
    print('success')
    return render_template('index.html')


