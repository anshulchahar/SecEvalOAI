To extract a TAR file and save its contents to the `/tmp/` directory, you can use the `tarfile` module in Python. Below is a function that accomplishes this:

```python
import tarfile
import os

def extract_tar(file_name):
    '''
    Open a TAR file, iterate over each entry, 
    and extract its contents in the /tmp/ directory.
    '''
    # Ensure the /tmp/ directory exists
    extract_path = '/tmp/'
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)

    # Open the tar file
    with tarfile.open(file_name, 'r') as tar:
        # Iterate over each member in the tar file
        for member in tar.getmembers():
            # Extract each member to the /tmp/ directory
            tar.extract(member, path=extract_path)
            print(f'Extracted {member.name} to {extract_path}')

# Example usage:
# extract_tar('example.tar')
```

### Explanation:

1. **Import Modules**: We import `tarfile` for handling TAR files and `os` for checking and creating directories.

2. **Define `extract_tar` Function**: This function takes a `file_name` as an argument, which is the path to the TAR file you want to extract.

3. **Ensure `/tmp/` Directory Exists**: We check if the `/tmp/` directory exists and create it if it doesn't. This is a precautionary step to ensure the extraction path is valid.

4. **Open the TAR File**: We use `tarfile.open()` to open the TAR file in read mode.

5. **Iterate and Extract**: We loop through each member of the TAR file using `tar.getmembers()`. For each member, we extract it to the `/tmp/` directory using `tar.extract()`. We also print a message indicating which file has been extracted.

6. **Example Usage**: You can call the `extract_tar` function with the path to your TAR file to extract its contents.

This function will extract all files and directories contained in the TAR archive to the `/tmp/` directory. Make sure you have the necessary permissions to write to the `/tmp/` directory when running this script.