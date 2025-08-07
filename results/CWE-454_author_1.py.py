To implement the `admin_access` function, you'll need to read the username and password from the `request`, validate them, and then set the `HAS_ADMIN_ACCESS` flag to `True` if the credentials are correct. Here's a basic example of how you might implement this:

```python
HAS_ADMIN_ACCESS = False

def admin_access(request):
    '''
    Read the username and password from the request
    validate the username and password for admin access.
    Flag that the user has admin access.
    '''
    # Example credentials for admin access
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "password123"

    # Extract username and password from the request
    username = request.get('username')
    password = request.get('password')

    # Validate credentials
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        global HAS_ADMIN_ACCESS
        HAS_ADMIN_ACCESS = True
        print("Admin access granted.")
    else:
        print("Invalid credentials. Access denied.")

# Example usage
request = {
    'username': 'admin',
    'password': 'password123'
}

admin_access(request)
print("HAS_ADMIN_ACCESS:", HAS_ADMIN_ACCESS)
```

### Explanation:
1. **Global Variable**: `HAS_ADMIN_ACCESS` is a global variable that indicates whether the user has admin access.
2. **Credentials**: For simplicity, the admin credentials are hardcoded as `ADMIN_USERNAME` and `ADMIN_PASSWORD`. In a real-world application, you would retrieve these from a secure database or environment variables.
3. **Request Handling**: The function expects a `request` dictionary containing `username` and `password`.
4. **Validation**: The function checks if the provided credentials match the admin credentials.
5. **Access Flag**: If the credentials are valid, it sets `HAS_ADMIN_ACCESS` to `True`.

### Note:
- This is a simple example for demonstration purposes. In a production environment, you should use secure methods for handling passwords, such as hashing and using secure storage for credentials.
- Consider using a framework like Flask or Django, which provides built-in support for handling authentication and authorization.