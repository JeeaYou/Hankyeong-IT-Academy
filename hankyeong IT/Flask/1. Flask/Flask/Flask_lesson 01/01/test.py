#1. mysql, web framework 사용을 위해 라이브러리 가져오기
import pymysql
from flask import Flask , render_template , request, redirect , url_for
#2. db 에 접속
db = pymysql.connect(host='localhost',
                     port = 3306, 
                     user='root',
                     password = 'mamawoaini1992!',
                     database = 'new_data',
                     charset = 'utf8'   
                    )

app = Flask(__name__)

@app.route("/", methods=["GET"]) 
def hello_world():
    return render_template('form.html', title="처음")

@app.route("/first")
def first():
    return render_template("form1.html")

@app.route("/login")
def login():
    return "<p>로그인 정보를 입력하세요.</p>"


@app.route("/user/<userid>", methods = ["GET", "POST"])
def user(userid):
    #3. 커서 가져오기
    cur = db.cursor() 
    if request.method == "GET":   
        data = [userid]
        #4. 원하는 sql 문 적기
        sql = "select username from user where userid = %s; "
        #5. 커서가 전달받은 sql 문을 실행
        res = cur.execute(sql,data)
        if res == 1:
            username = cur.fetchone()
            user = [userid, username[0]]
            return render_template("info.html", user=user)
        else:
            user = [userid, username]
            return render_template("info.html",user=user)
    elif request.method == "POST":
        telno = request.form['telno']
        data = [telno, userid]
        #4. 원하는 sql 문 적기
        sql = "update user set telno = %s where userid = %s; "
        #5. 커서가 전달받은 sql 문을 실행
        res = cur.execute(sql,data) 
        if res == 1:
            db.commit()
            return "수정성공"
        else:
            return "수정실패"

@app.route("/namelist/<username>")
def namelist(username):
    user = [username, 'aaa', 11]
    return render_template("user.html", title="user", user=user)

@app.route("/<username>")
def exe1(username):
    user = [username, len(username)]
    return render_template("exe1.html", title="user", user=user)

@app.route("/fileserver")
def file_server():
    return "<p>파일을 업로드하세요.</p>"

@app.route("/gugudan", methods=["GET","POST"])
def gugudan():
    if request.method == "GET":
        return render_template("gugudan.html")
        
    elif request.method == "POST": 
        dan = request.form['dan']
        return render_template("gugudan.html", dan = dan)

if __name__ == "__main__":
    app.run( debug = True)
    # host = "192.168.44.11", port = "5100",