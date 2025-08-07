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