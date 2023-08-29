import requests
import sys

# Get the URL and email address from cmd line args
url = sys.argv[1]
email = sys.argv[2]

# Data being sent in the POST request
data = {'email': email}

# Send an HTTP POST request to the specified url with an email parameter
response = requests.post(url, data=data)

# Display the body of the response
print(response.text)