# url생성
# route 기능 구현

# route/주소를 쉽게 관리하기 위해 blueprint 생성
from flask import Blueprint
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def hello_pybo():
    print('실행됬음')
    return 'Hello , Pybo!'
