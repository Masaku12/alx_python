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
    
    response = requests.get(url, headers=headers)
    
    # Check if the response is valid JSON
    try:
        data = response.json()
    except:
        return None
    
    # Check if response contains expected fields
    if "id" in data:
        return data["id"]
    else:
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
        print(f"Your Github User ID is: {user_id}")
    else:
        print("Unable to retrieve Github user ID")
    
    if __name__ == "__main__":
        main()