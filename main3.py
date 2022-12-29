import json
from flask import Flask, request

app = Flask(__name__)

class MyDB:
    foo = []

@app.get("/data")
def get_data():
    return f"<h1> {MyDB.foo} </h1>"

@app.post("/data")
def post_data():
    data_ = json.loads(request.data)
    for value_ in data_.values():
        MyDB.foo.append(value_)
    return f"<h1> {MyDB.foo} </h1>"




