To kill a process using its process ID in Python, you can use the `os.kill` function along with the `signal` module to send a termination signal to the process. Here's how you can implement the `killProcess` function:

```python
import os
import signal

def killProcess(processID):
    '''
    Kill the process with the given processID.
    
    Parameters:
    processID (int): The ID of the process to be killed.
    '''
    try:
        # Send the SIGTERM signal to the process
        os.kill(processID, signal.SIGTERM)
        print(f"Process {processID} has been terminated.")
    except ProcessLookupError:
        print(f"No process found with ID {processID}.")
    except PermissionError:
        print(f"Permission denied to kill process {processID}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# killProcess(12345)
```

### Explanation:
- **`os.kill(processID, signal.SIGTERM)`**: This line sends the `SIGTERM` signal to the process with the specified `processID`. `SIGTERM` is a termination signal that requests a process to stop running. It allows the process to perform cleanup operations before exiting.
- **Exception Handling**: The function includes exception handling to manage different scenarios:
  - **`ProcessLookupError`**: Raised if no process with the specified ID is found.
  - **`PermissionError`**: Raised if the current user does not have permission to terminate the specified process.
  - **General Exception**: Catches any other exceptions that might occur and prints an error message.

### Important Notes:
- Make sure you have the necessary permissions to terminate the process. You might need to run your script with elevated privileges (e.g., using `sudo` on Unix-like systems) if you're trying to kill a process owned by another user.
- Be cautious when terminating processes, especially critical system processes, as it might lead to system instability.