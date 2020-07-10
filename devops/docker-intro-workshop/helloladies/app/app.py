from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world!"


@app.route("/<name>")
def homepage(name):
    return render_template("index.html", username=name)


if __name__ == "__main__":

    app.run(host="0.0.0.0")

