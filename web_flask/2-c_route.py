#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
