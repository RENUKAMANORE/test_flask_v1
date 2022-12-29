from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> hello world!! </p1>"

@app.route("/details")
def get_details():
    return "<p> renuka python developer </p1>"

@app.route("/mydetails", methods=["GET","POST"])
def details():
    return "<h1> access both get an post method </h1>"
