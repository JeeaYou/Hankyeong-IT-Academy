from flask import Blueprint
from pybo.models import Question
from datetime import datetime
from pybo import db

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

@bp.route('/insertqa')
def insertqa():   # 데이터 추가하기
    for temp in range(10):
        q = Question(subject = '질문{}'.format(temp), content = '내용{}'.format(temp), create_date = datetime.now())
        db.session.add(q)
        print('저장 완료!')
    db.session.commit()   # commit는 for문 안데 들어가지 않는다. 마지막 1번만 쓴다
    return '데이터 입력 완료!'

@bp.route('/get_qa_all')
def get_qa_all():
    result = Question.query.all()   # list형태로 저장됨
    for temp in result:
        print(temp.id)
        print(temp.subject)
        print(temp.content)
        print(temp.create_date)
        print('총 게시글 : {} 개'.format(len(result)))
    return '총 게시글 : {} 개'.format(len(result))

@bp.route('/get_qa_pk/<int:pk>')
def get_qa_pk(pk):
    result = Question.query.get(pk)
    print(result.subject)
    print(result.content)
    print(result.create_date)
    return '가져오기 완료!'

@bp.route('/get_qa_title/<title>')
def get_qa_title(title):
    result = Question.query.filter(Question.subject==title).all()

    contentlist = []
    for temp in result:
        print(temp.id)
        print(temp.subject)
        print(temp.content)
        contentlist.append(temp.content)
        print(temp.create_date)
    return contentlist
