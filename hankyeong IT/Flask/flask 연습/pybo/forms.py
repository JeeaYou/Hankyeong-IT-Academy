from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

# wtf 를 사용했을 때 비여있거나 경고창등을 자동으로 처리한다.
class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired()])  # StringField 한줄만 넣는다, DataRequired 무조건 채워진다
    content = TextAreaField('내용', validators=[DataRequired()])  # TextAreaField 여러줄 넣을수 있다, DataRequired 무조건 채워진다

class UserCreateForm(FlaskForm):
    username = StringField('사용자 이름', validators=[DataRequired(), Length(min=6, max=20)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2','비밀번호가 다릅니다.')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    email = EmailField('이메일',validators=[DataRequired(), Email()])
    phone = StringField('전화번호', validators=[DataRequired()])