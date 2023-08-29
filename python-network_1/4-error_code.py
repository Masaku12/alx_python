import requests
import sys

# GET the URL from cmd line arguments
url = sys.argv[1]

# Send an HTTP request to the specified URL
response = requests.get(url)

# Display the body of the response
print(response.text)

# Check if the HTTP status code is >= to 400
if response.status_code >= 400:
    print("Error code:", response.status_code)