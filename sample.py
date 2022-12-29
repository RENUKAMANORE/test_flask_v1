from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

@app.route("/hello")
def about():
    return render_template("hello.html")

