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
    headers = {"Authorization": f"Bearer {token}"}
    
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
    Main function that prompts the user to enter their Github username and personal access token
    It will also display their user ID
    """
    username = input("Enter your Github Username: ")
    token = input("Enter your personal access token: ")
    
    user_id = get_user_id(username, token)
    if user_id is not None:
        print(user_id)
    else:
        print("None")
    
if __name__ == "__main__":
    main()