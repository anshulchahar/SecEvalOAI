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