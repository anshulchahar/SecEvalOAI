import time

def currentTime():
    '''
    Print the current processor time in seconds.
    '''
    processor_time = time.process_time()
    print(f"Current processor time: {processor_time} seconds")

# Example usage
currentTime()