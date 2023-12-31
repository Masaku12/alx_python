#!/usr/bin/env python3

import requests
import sys

def get_user_id(username, token):
    """
    Retrieves the Github user id for a given username using the Github API and a personal access token
    
    Args:
        username: The Github username, which is a string
        token: The personal access token with requisite permissions, also a string
        
    Returns:
        int: The Github user ID
    """
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"token {token}"}
    
    # Check if the response is valid JSON
    try:
        # Send a GET request to Github API
        response = requests.get(url, headers=headers)
        response.raise_for_status() # check for successful request status
        data = response.json()
        
        if "id" in data:
            return data["id"]
        else:
            return None
    except requests.exceptions.RequestException as e:
        # Handle request exceptions
        print(f"An error occured: {e}")
        return None
    except ValueError:
        # Handle JSON parsing error
        return None
    
def main():
    """
    Main function that reads Github username and personal access token as cmd line args
    It will also display their user ID or 'None' if not found
    """
    if len(sys.argv) != 3:
        print("Usage: my_github.py <GitHub_username> <personal_access_token>")
        sys.exit(1)
    
    username = sys.argv[1]
    token = sys.argv[2]
    
    user_id = get_user_id(username, token)
    if user_id is not None:
        print(user_id)
    else:
        print("None")
    
if __name__ == "__main__":
    main()
