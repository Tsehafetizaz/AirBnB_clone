#!/usr/bin/python3
"""start web application"""
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


@app.route("/python/<text:text>", strict_slashes=False)
def python_route(text="is cool"):
    """Displays 'Python ' followed by the value of the text variable,
    replacing underscores (_) with spaces.

    Args:
        text (str, optional): text variable passed URL. Defaults to "is cool".

    Returns:
        str: The formatted string "Python " followed by the text with spaces
              replacing underscores.
    """
    # Wrap the long line within parentheses for continuation
    return (f"Python {text.replace('_', ' ')}")  # Remove trailing whitespace


if __name__ == "__main__":
    """main fucntion"""
    app.run(host="0.0.0.0", port=5000)
