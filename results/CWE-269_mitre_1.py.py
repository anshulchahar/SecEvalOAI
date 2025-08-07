To implement the `makeNewUserDir` function, you'll need to follow the steps outlined in the docstring. Here's a possible implementation:

```python
def makeNewUserDir(username):
    # Check if the username is invalid
    if invalidUsername(username):
        return False

    # Temporarily raise privileges
    raisePrivileges()

    try:
        # Define the path for the new user directory
        user_dir = os.path.join('/home', username)

        # Create the new user directory
        os.makedirs(user_dir, exist_ok=False)

        # If the directory was successfully created, return True
        return True
    except Exception as e:
        # Handle any exceptions (e.g., directory already exists, permission issues)
        print(f"Error creating directory for user {username}: {e}")
        return False
    finally:
        # Lower privileges back to normal
        lowerPrivileges()
```

### Explanation:

1. **Check for Invalid Username**: The function first checks if the username is invalid by calling `invalidUsername(username)`. If the username is invalid, it returns `False`.

2. **Raise Privileges**: The function then raises privileges by calling `raisePrivileges()`. This is necessary to ensure the program has the necessary permissions to create directories in `/home`.

3. **Create User Directory**: The function constructs the path for the new user directory using `os.path.join('/home', username)`. It then attempts to create this directory using `os.makedirs()`. The `exist_ok=False` parameter ensures that an exception is raised if the directory already exists.

4. **Exception Handling**: If an exception occurs during directory creation (e.g., if the directory already exists or there are permission issues), the function prints an error message and returns `False`.

5. **Lower Privileges**: Finally, the function ensures that privileges are lowered back to normal by calling `lowerPrivileges()`, regardless of whether the directory creation was successful or not.

6. **Return Value**: The function returns `True` if the directory was successfully created, and `False` otherwise.

This implementation assumes that `invalidUsername`, `raisePrivileges`, and `lowerPrivileges` are defined elsewhere in your code.