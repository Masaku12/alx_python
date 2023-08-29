# Importing the relevant 
import requests
import sys

# Get the url from command-line argument
url = sys.argv[1]

# Send an HTTP GET request to the intended url
response = requests.get(url)

# Check if the response has the 'X-Request-Id' header
if 'X-Request-Id' in response.headers:
    # Extract the value of the 'X-Requesr-Id' header from the response
    request_id = response.headers['X-Request-Id']
    print(request_id)
else:
    print("X-Request-Id header not found in the response.")