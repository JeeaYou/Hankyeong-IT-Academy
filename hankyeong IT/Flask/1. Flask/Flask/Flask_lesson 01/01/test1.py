from operator import methodcaller
import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def hello_world():
    return render_template("form.html")

@app.route("/first")
def firts():
    return render_template("form1.html")

@app.route("/login")
def login():
    return "<p>로그인 정보를 입력하세요.</p>"

#GET 방식, POST 방식 합친 경우
@app.route("/login_process", methods = ["GET", "POST"])
def login_process():
    if request.method == "GET":
    #GET 방식
        #print(request.args)
        username = request.args['username']
        pwd = request.args['pwd']
        if username == 'aaa'and pwd == '1111':
            return username +"로그인되었습니다."
        else:
            return "다시 정확한 정보로 로그인하세요."
    elif request.method == "POST": 
    #POST 방식
        username = request.form['username']
        pwd = request.form['pwd']
        if username == 'aaa'and pwd == '1111':
            return username +"로그인되었습니다."
        else:
            return "다시 정확한 정보로 로그인하세요."

@app.route("/user/<username>")
def user(username):
    return username + "님 안녕하세요."  

@app.route("/namelist/<username>")
def namelist(username):
    user = [username, 'aaa', 11]
    return render_template("user.html", title="user", user=user)

@app.route("/<username>")
def exe1(username):
    user = [username, len(username)]
    return render_template("exe1.html",title="user", user=user)

@app.route("/gugudan", methods=["GET", "POST"])
def gugudan():
    if request.method == "GET":
        return render_template("/gugudan.html")

    elif request.method == "POST":
        dan = request.form['dan']
        return render_template("/gugudan.html", dan = dan)
    
@app.route("/file_server")
def file_server():
    return "<p>파일을 업로드하세요.</p>"
    
if __name__ == "__main__":
    app.run( debug = True)
# host = '192.168.4.239', port = "5100",
