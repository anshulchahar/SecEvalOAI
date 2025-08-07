import subprocess

def executeCommand():
    '''
    Read a command from a user input, validate it, and execute it
    '''
    # Define a whitelist of allowed commands
    allowed_commands = {
        'list': 'ls',
        'current_directory': 'pwd',
        'who_am_i': 'whoami'
    }

    # Read command from user input
    user_input = input("Enter a command (list, current_directory, who_am_i): ").strip()

    # Validate the command
    if user_input in allowed_commands:
        command = allowed_commands[user_input]
        try:
            # Execute the command
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid command. Please enter a valid command.")

# Example usage
executeCommand()