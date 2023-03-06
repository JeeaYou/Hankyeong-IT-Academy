from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)   # config파일을 flask에 등록하기

    db.init_app(app)
    migrate.init_app(app,db)   # 데이터베이스를 집어넣기

    # flask db init ------ db를 초기화 한다.(migrations 폴더에 파일이 생성된다)
    # migrations폴더가 생성되지 않을 경우 config파일이 잘못됬다
    # db와 migrate 설정이 안된경우

    from .import models

    from .views import main_views, news_views, question_views, auth_views  # blueprint로 묶은 주소를 추가해야한다.
    app.register_blueprint(main_views.bp)    # main_views의 blueprint를 flask에 등록한다
    app.register_blueprint(news_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(question_views.bp)

    return app

    # Flask db migrate 테이블이 추가/또는 바뀌였을때
