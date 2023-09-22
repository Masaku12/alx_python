from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route for the home page
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

if __name__ == "__main__":
    # Start the web app on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
