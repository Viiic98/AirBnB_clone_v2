#!/usr/bin/python3
""" Using routes to return something """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ Function returning a string in an app """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function returning a string in an app """
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
