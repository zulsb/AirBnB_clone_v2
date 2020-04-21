#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """Module to display text"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """Module to display text2"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Module to display custom text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_r(text="is cool"):
    """Module to display custom text2"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def text_if_int(n):
    """Module to display text only if int"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_if_int(n):
    """Module to display html page only if int"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
