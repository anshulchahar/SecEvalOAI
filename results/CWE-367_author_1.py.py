To implement the `readFile` function, you can use Python's built-in `os.path` module to check if the file exists and then use a `with` statement to open and read the file. Here's a complete implementation:

```python
import os

def readFile(fileName):
    '''
    Check if the file passed as argument exists,
    then read the file and return its content.
    '''
    # Check if the file exists
    if not os.path.isfile(fileName):
        return "File does not exist."

    # Read the file and return its content
    try:
        with open(fileName, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        return f"An error occurred while reading the file: {e}"

# Example usage:
# content = readFile('example.txt')
# print(content)
```

### Explanation:
- **os.path.isfile(fileName)**: This checks if the specified path is an existing regular file.
- **with open(fileName, 'r') as file**: This opens the file in read mode. The `with` statement ensures that the file is properly closed after its suite finishes, even if an exception is raised.
- **file.read()**: This reads the entire content of the file.
- **Exception handling**: The `try-except` block catches any exceptions that might occur while opening or reading the file, such as permission errors or encoding issues, and returns an appropriate error message.