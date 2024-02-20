#!/usr/bin/python3
""" Starts a Flask Web Application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns a msg when '/' is called """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Returns a msg when '/hbnb' is called """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """ Displays a msg when '/c' is called """
    return "C " + text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
