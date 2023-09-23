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
    # Render an HTML template with the number
    return render_template('number_template.html', n=n), 200

if __name__ == "__main__":
    # Start the web app on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
