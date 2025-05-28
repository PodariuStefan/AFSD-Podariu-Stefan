from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def root():
    return "Catalog Electronic"

@app.route("/clase")
def clase():
    return "Clasa 1\n"

with app.test_request_context():
    print(url_for("root"))
    print(url_for("clase"))
