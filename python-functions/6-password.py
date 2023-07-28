def validate_password(password):
    if len(password) < 8:
        return False
    
    # Check for the presence of at least one of the expected outcomes in the password
    contains_uppercase = False
    contains_lowercase = False
    contains_digit = False
    
    for char in password:
        if char.isupper():
            contains_uppercase = True
        elif char.islower():
            contains_lowercase = True
        elif char.isdigit():
            contains_digit = True
            
    if not (contains_uppercase and contains_lowercase and contains_digit):
        return False
    
    # Checking for space character in the password
    if ' ' in password:
        return False
    
    # if all checks have been met
    return True