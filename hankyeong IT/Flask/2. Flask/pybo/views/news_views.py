from flask import Blueprint

bp = Blueprint('news', __name__, url_prefix='/news')

@bp.route('/login/<id>/<pw>')
def login(id, pw):
    print(id)
    print(pw)
    return 'login'

@bp.route('/top/<int:newsno>')   # top뒤에 newsno라는 변수의 숫자가 들어온다.
def news_top(newsno):
    print(newsno)
    return '화면에 Top뉴스입니다.'

@bp.route('/week')
def news_week():
    print('주간뉴스입니다.')
    return '주간뉴스입니다.'