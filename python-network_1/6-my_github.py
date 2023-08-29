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
    url = 'https://api.github.com/users/{}'.format(username)
    response = requests.get(url, auth=(username, token))
    
    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print('None')
    
if __name__ == "__main__":
    # Get GitHub username and personal access token using cmd line args
    username = sys.argv[1]
    token = sys.argv[2]
    
    # Retrieve and print the user ID
    user_id = get_user_id(username, token)
    if user_id is not None:
        print(user_id)
    else:
        print('None')