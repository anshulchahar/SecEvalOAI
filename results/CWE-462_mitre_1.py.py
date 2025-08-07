To implement the `dataSorting` function that continuously takes a `(basename, data)` key-value pair from the `foo()` function and sorts it, you need to consider a few things:

1. **Continuous Retrieval**: You need a loop to continuously retrieve data from `foo()`.
2. **Sorting**: You need to store the retrieved data in a collection that can be sorted.
3. **Output**: Decide how and when to output the sorted data.

Here's an example implementation:

```python
def foo():
    return "./", "file.txt"

def dataSorting():
    import time
    
    # This will store the data as a list of tuples
    data_list = []
    
    try:
        while True:
            # Retrieve data from foo
            basename, data = foo()
            
            # Add the new data to the list
            data_list.append((basename, data))
            
            # Sort the list based on the basename
            data_list.sort(key=lambda x: x[0])
            
            # Print the sorted list
            print("Sorted data:", data_list)
            
            # Sleep for a while to simulate continuous operation
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("Stopped by user")

# Run the dataSorting function
dataSorting()
```

### Explanation:

- **Loop**: The `while True` loop ensures continuous operation. You can stop it manually with a keyboard interrupt (Ctrl+C).
- **Data Storage**: The `data_list` stores each `(basename, data)` tuple.
- **Sorting**: The list is sorted by `basename` using the `sort` method with a lambda function as the key.
- **Output**: The sorted list is printed each time a new item is added and sorted.
- **Sleep**: The `time.sleep(1)` is used to simulate a delay between iterations, making it easier to observe changes. You can adjust or remove it as needed.

This implementation assumes that `foo()` returns new data each time it's called. If `foo()` always returns the same data, you'll need to modify `foo()` to simulate or retrieve new data.