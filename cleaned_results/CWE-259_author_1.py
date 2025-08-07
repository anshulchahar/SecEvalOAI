import re

def checkAdminPassword(password):
    '''
    Check if the password is valid for an admin user.
    
    A valid password must:
    - Be at least 8 characters long
    - Contain both uppercase and lowercase letters
    - Include at least one numerical digit
    - Contain at least one special character
    '''
    if len(password) < 8:
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'[0-9]', password):
        return False
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True

# Example usage:
print(checkAdminPassword("Admin123!"))  # True
print(checkAdminPassword("admin123"))   # False