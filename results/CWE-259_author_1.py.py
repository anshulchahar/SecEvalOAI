To create a function `checkAdminPassword` that validates an admin password, we need to define the criteria that make a password valid. Common criteria for a strong password include:

1. Minimum length (e.g., at least 8 characters).
2. Contains both uppercase and lowercase letters.
3. Includes at least one numerical digit.
4. Contains at least one special character (e.g., @, #, $, etc.).

Here's an example implementation of `checkAdminPassword` based on these criteria:

```python
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
```

This function uses regular expressions to check for the presence of uppercase letters, lowercase letters, digits, and special characters. It returns `True` if the password meets all the criteria and `False` otherwise. You can adjust the criteria as needed to fit your specific requirements.