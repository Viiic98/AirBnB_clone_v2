#!/usr/bin/python3
""" Using routes to return """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ Function returning a string in an app """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function returning a string in an app """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_variable(text):
    """ Function returning a string in an app using a variable """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def p_variable(text="is cool"):
    """ Function returning a string in an app using a variable
        with default value
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def n_variable(n):
    """ Function returning a string in an app using a variable
        to return if n is an integer
    """
    if type(n) is int:
        return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_int(n):
    """ Return a html page """
    if type(n) is int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    """ Return a html page """
    if type(n) is int:
        return render_template('6-number_odd_or_even.html', n=n)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
