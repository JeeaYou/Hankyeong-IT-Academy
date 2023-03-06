# url생성
# route 기능 구현

# route/주소를 쉽게 관리하기 위해 blueprint 생성
from flask import Blueprint, render_template, request, jsonify
from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():

    question_list = Question.query.order_by(Question.create_date.desc())
    print('sucess')
    return render_template('question/question_list.html', question_list = question_list, id = '홍길동') # Jinja2 기능

@bp.route('/test')
def test():
    return render_template('index.html')

@bp.route('/chatbot', methods=['POST'])
def chatbot():
    result = request.get_json()
    print('영화 제목: {}'.format(result['queryResult']['parameters']['Movie_Name']))
    r = jsonify(
        fulfillment_text="영화내용은 다음과 같습니다.",
        fulfillment_messages=[
            {
                "payload": {
                    "richContent": [
                        [
                            {
                                "type": "image",
                                "rawUrl": "https://cdn.sisamagazine.co.kr/news/photo/202205/444486_449427_2817.jpg",
                                "accessibilityText": "아바타 이미지"
                            }
                        ]
                    ]
                }
            }
        ]
    )
    return r

