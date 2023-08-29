# Importing the requests package to make HTTP requests
import requests

# The url being fetched
url = "https://alu-intranet.hbtn.io/status"

# sending an HTTP GET request to the intended URL
response = requests.get(url)

# Displaying the body response in the required format
print("Body response:")

# Displaying the type of the content in the response
print("\t- type:", type(response.text))

# Displaying the actual content of the response
print("\t- content:", response.text)