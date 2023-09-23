"""
A simple Flask web app that displays Hello HBNB
"""

from flask import Flask, render_template

# Create a Flask web application
app = Flask(__name__)

# Define a route for the home page
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the home page

    Returns:
        a str: Hello HBNB!
    """
    return "Hello HBNB!"

# Define a route for the /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the hbnb page

    Returns:
        a str: HBNB
    """
    return "HBNB"

# Define a route that accepts a dynamic parameter text
@app.route('/c/<text>', strict_slashes=False)
def custom_text(text):
    """
    Route handler for custom_text page

    Args:
        a str: The text provided as a param

    Returns:
        a str: "C " 
    """
    # Replace underscores with spaces in the text param
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"

# Define a route that accepts a dynamic param 'text'
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_text(text="is cool"):
    """
    Route handler for the /python/<text> page

    Args:
        text: a str

    Returns:
        a str: "Python " followed by value of text
    """
    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"

# Define a route that accepts an int param 'n'
@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    Route handler for the /number/<n> page

    Args:
        n (int): The int parameter

    Returns:
        str: "<n> is a num" if n is an int
    """
    return f"{n} is a number"

# Define a route that accepts an int param & renders an HTML template
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route handler for the /number_template/<int:n> page

    Args:
        n (int): The int parameter

    Returns:
        HTML page with an H1 tag with the "Number: n"
    """
    if isinstance(n, int):
        template = render_template("5-number.html", n=n)
        response = app.response_class(response=template, status=200, mimetype='text/html')

    # Set response status to 1
    response.status_code = 1

    return response

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route handler for /number_odd_or_even/<int:n> page

    Args:
        n (int): The integer parameter

    Returns:
        HTML page with an H1 tag with "Number: n is even|odd"
    """
    if isinstance(n, int):
        odd_or_even = "even" if n % 2 == 0 else "odd"
        template = render_template("6-number_odd_or_even.html", n=n, odd_or_even=odd_or_even)
        response = app.response_class(response=template, status=200, mimetype='text/html')
        return response


if __name__ == "__main__":
    # Start the web app on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
