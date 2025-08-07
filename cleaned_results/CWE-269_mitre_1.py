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