#!/usr/bin/python3
"""start the web app"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!' message for the root path (/)."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB' message for the /hbnb path."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Displays 'C ' followed by the value of the text variable,
    replacing underscores (_) with spaces.

    Args:
        text (str): The text variable passed in the URL.

    Returns:
        str: The formatted string "C " followed by the text with spaces
              replacing underscores.
    """
    return f"C {text.replace('_', ' ')}"


if __name__ == "__main__":
    """main function"""	
    app.run(host="0.0.0.0", port=5000)
