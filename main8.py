from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/manager")
def manager():
    url = url_for("emp", name="renu")
    print(url)

    return "hello manager"

@app.route("/employee/<name>")
def emp(name):
    return f"<h1> employee:good morning {name} </h1>"

@app.route("/client/<client>")
def cli(client):
    return f"<h1> client:good morning {client} </h1>"

@app.route("/user/<name>")   # redirct the url from one function to another fuuction
def greeting_everyone(name):
    if name == "employee":
        emp_url = url_for("emp", name="renu")
        return redirect(emp_url)
    elif name == "client":
        cli_url = url_for("cli", client="mayur")
        return redirect(cli_url)


    return f"hello {name}"
