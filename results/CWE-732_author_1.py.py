To create a binary file named `test.bim` and make it executable, you can follow these steps in Python. This example will create a simple binary file and then change its permissions to make it executable:

```python
import os

def createExecutableFile(data):
    # Define the filename
    filename = 'test.bim'
    
    # Write the binary data to the file
    with open(filename, 'wb') as file:
        file.write(data)
    
    # Change the file permissions to make it executable
    # 0o755 gives read, write, and execute permissions to the owner,
    # and read and execute permissions to group and others
    os.chmod(filename, 0o755)

# Example binary data
binary_data = b'\x7fELF...'  # Replace with actual binary content

# Create the executable file
createExecutableFile(binary_data)
```

### Explanation:

1. **Writing Binary Data**: The function `createExecutableFile` takes `data` as an argument, which should be a bytes object representing the binary content you want to write to the file. The file is opened in binary write mode (`'wb'`), and the data is written to it.

2. **Changing File Permissions**: The `os.chmod` function is used to change the file permissions. The mode `0o755` is commonly used for executable files, allowing the owner to read, write, and execute the file, while others can read and execute it.

3. **Binary Data**: Replace `b'\x7fELF...'` with the actual binary content you want to include in the file. This example uses a placeholder, but you should provide the real binary data.

Make sure you have the necessary permissions to create and modify files in the directory where you run this script.