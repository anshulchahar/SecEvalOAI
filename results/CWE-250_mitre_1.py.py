To implement the `makeNewUserDir` function, you'll need to use the `os` module to create a directory and handle exceptions appropriately. Here's how you can do it:

```python
import os

def raisePrivileges():
    # Placeholder for privilege escalation logic
    print("Privileges raised.")

def lowerPrivileges():
    # Placeholder for privilege de-escalation logic
    print("Privileges lowered.")

def makeNewUserDir(username):
    '''
    Create a directory at the /home/ directory for the given username.
    Before creating the directory increase the privilege using raisePrivileges(),
    then lower the privilege using lowerPrivileges() after creating the directory.
    Handle the exception if the directory already exists.
    '''
    # Define the path for the new user directory
    user_dir = os.path.join('/home', username)
    
    try:
        # Raise privileges before creating the directory
        raisePrivileges()
        
        # Attempt to create the directory
        os.makedirs(user_dir)
        print(f"Directory created: {user_dir}")
    
    except FileExistsError:
        # Handle the case where the directory already exists
        print(f"Directory already exists: {user_dir}")
    
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An error occurred: {e}")
    
    finally:
        # Lower privileges after attempting to create the directory
        lowerPrivileges()

# Example usage
makeNewUserDir('newuser')
```

### Explanation:

1. **Privilege Management**: The `raisePrivileges` and `lowerPrivileges` functions are placeholders where you would implement the logic to change the process's privileges. This might involve using system-specific calls or libraries, depending on your environment.

2. **Directory Creation**: The `os.makedirs` function is used to create the directory. It will raise a `FileExistsError` if the directory already exists, which is caught and handled in the `except` block.

3. **Exception Handling**: The function handles `FileExistsError` specifically to inform the user if the directory already exists. A general `Exception` catch is also included to handle any other unexpected errors.

4. **Finally Block**: The `finally` block ensures that `lowerPrivileges` is called regardless of whether an exception occurred, maintaining the correct privilege level after the operation.