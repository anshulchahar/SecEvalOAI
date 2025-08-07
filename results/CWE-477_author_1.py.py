To print the current processor time in seconds, you can use the `time` module in Python. Specifically, you can use the `time.process_time()` function, which returns the processor time in seconds as a floating-point number. Here's how you can implement the `currentTime` function:

```python
import time

def currentTime():
    '''
    Print the current processor time in seconds.
    '''
    processor_time = time.process_time()
    print(f"Current processor time: {processor_time} seconds")

# Example usage
currentTime()
```

This function will print the amount of CPU time used by the current process since it started. Note that this is different from wall-clock time, as it only accounts for the time the CPU has spent executing the process, not the actual elapsed time.