#!/usr/bin/python3
"""Script that starts a Flask web application."""
from flask import Flask, render_template
from models import storage
from models.state import State

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


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def o_or_e(n):
    """Module to display html page only if int odd or even"""
    o_or_e = "even" if (n % 2 == 0) else "odd"
    return render_template("6-number_odd_or_even.html", n=n, o_or_e=o_or_e)


@app.teardown_appcontext
def tear_down(self):
    """Module to remove current SQLAlchemy and close session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states_html():
    """Module to display html page where you look for ordered
    places to insert in html in the UL tag"""
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


@app.route('/states_list', strict_slashes=False)
def html_states_cities():
    """Module to display html page where you look for ordered
    places and cities to insert in html in the LI tag"""
    states = storage.all("State").values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
