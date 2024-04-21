#!/usr/bin/python3
"""Start flash web app HBNB"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!' message for the root path"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB' message for the /hbnb path"""
    return "HBNB"


if __name__ == "__main__":
    """main function"""
    app.run(host="0.0.0.0", port=5000)
