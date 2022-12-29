from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>hello world</h1>"

@app.route("/about/<institute>")
def about(institute):
    return f"handcrafted by renuka {institute}"

@app.route("/addition/<int:num1>/<int:num2>")
def add(num1 ,num2):
    result = num1 + num2
    return f"<h1> {result} </h1>"