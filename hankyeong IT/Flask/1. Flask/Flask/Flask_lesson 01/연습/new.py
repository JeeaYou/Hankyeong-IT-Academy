from operator import methodcaller
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET",'POST'])
def hello_world():
    return render_template("file.html")


@app.route("/sql", methods = ["GET", "POST"])
def sql_def():
    return render_template("sql.html")

@app.route("/image", methods = ["GET", "POST"])
def image_def():
    return render_template("image.html")

@app.route("/flask", methods = ["GET", "POST"])
def flask_def():
    return render_template("flask.html")

if __name__ == "__main__":
    app.run( debug = True)