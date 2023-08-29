import requests
import sys

# Get the letter from cmd line args or set it to an empty str
letter = sys.argv[1] if len(sys.argv) > 1 else ""

#URL for the POST request
url = "http://0.0.0.0:5000/search_user"

# Data being sent in the POST request
data = {'q': letter}

# Send an HTTP POST request to the specified URL with the letter parameter
response = requests.post(url, data=data)

try:
    # Try to parse the response as JSON
    json_data = response.json()
    
    # Check if the JSON is not empty
    if json_data:
        print("[{}] {}".format(json_data['id'], json_data['name']))
    else:
        print("No result")
        
except ValueError:
    # Handle invalid JSON format
    print("Not a valid JSON")