from flask import Blueprint, render_template, request, url_for, flash
from pybo.forms import QuestionForm, UserCreateForm
from .. import db  # ..은 상위
from ..models import User
from pybo.models import Question
from datetime import datetime
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup', methods=('GET','POST'))
def signup():
    form = UserCreateForm()
    print('------------1')
    if request.method == 'POST' and form.validate_on_submit():
        print('------------2')
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            user = User(username=form.username.data, password=generate_password_hash(form.password1.data),
            email=form.email.data, phone=form.phone.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재한 데이터입니다')

    return render_template('auth/signup.html',form=form)
