To implement the `dispatchCommand` function as described, you'll need to define the `loginUser`, `sendFile`, and `listFiles` functions, as well as handle authentication. Below is an example of how you might implement this:

```python
def loginUser(user, args):
    # Implement login logic here
    print(f"Logging in user: {user} with args: {args}")
    # Return True if login is successful, otherwise False
    return True

def sendFile(user, args):
    # Implement file retrieval logic here
    print(f"Sending file to user: {user} with args: {args}")

def listFiles(user, args):
    # Implement file listing logic here
    print(f"Listing files for user: {user} with args: {args}")

def authenticate(user):
    # Implement authentication logic here
    # For simplicity, let's assume all users are authenticated
    print(f"Authenticating user: {user}")
    return True

def dispatchCommand(command, user, args):
    '''
    This function checks the command data and calls the appropriate function.
    When command is 'login', it calls loginUser()
    When command is 'retrieve_file', it calls sendFile()
    When command is 'list_files', it calls listFiles()
    It does appropriate authentication before calling the function
    '''
    if command == 'login':
        if loginUser(user, args):
            print("Login successful")
        else:
            print("Login failed")
    else:
        if authenticate(user):
            if command == 'retrieve_file':
                sendFile(user, args)
            elif command == 'list_files':
                listFiles(user, args)
            else:
                print(f"Unknown command: {command}")
        else:
            print("Authentication failed")

# Example usage
dispatchCommand('login', 'user1', {'password': 'secret'})
dispatchCommand('retrieve_file', 'user1', {'filename': 'example.txt'})
dispatchCommand('list_files', 'user1', {})
```

### Explanation:
- **`loginUser`**: Simulates a login process. It should return `True` if the login is successful.
- **`sendFile`**: Simulates sending a file to the user.
- **`listFiles`**: Simulates listing files for the user.
- **`authenticate`**: Simulates user authentication. In a real-world scenario, this would involve checking user credentials or tokens.
- **`dispatchCommand`**: