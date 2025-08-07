To achieve the task of writing a Unicode string to a temporary file and returning its path, you can use Python's `tempfile` module. Here's how you can implement the `write_results` function:

```python
import tempfile

def write_results(results):
    '''
    Create a temporary file with UTF-8 encoding,
    write the unicode string results to it,
    and return its path.
    '''
    # Create a NamedTemporaryFile with delete=False so it persists after closing
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as temp_file:
        # Write the results to the file
        temp_file.write(results)
        # Return the path of the temporary file
        return temp_file.name
```

### Explanation:
- **`tempfile.NamedTemporaryFile`**: This function creates a temporary file that can be accessed by name. The `delete=False` parameter ensures that the file is not deleted when it is closed, allowing you to return its path.
- **`mode='w'` and `encoding='utf-8'`**: These parameters specify that the file should be opened in write mode with UTF-8 encoding, which is suitable for Unicode strings.
- **`temp_file.write(results)`**: This line writes the provided Unicode string to the temporary file.
- **`return temp_file.name`**: This returns the path to the temporary file, allowing the caller to access it later.

This function will create a temporary file, write the provided Unicode string to it, and return the file's path, which can be used to access the file's contents.