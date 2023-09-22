"""
A simple Flask web app that displays Hello HBNB
"""

from flask import Flask

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

if __name__ == "__main__":
    # Start the web app on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
