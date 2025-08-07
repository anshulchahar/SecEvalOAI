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