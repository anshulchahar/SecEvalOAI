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