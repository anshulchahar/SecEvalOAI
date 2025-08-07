To complete the `getFileData` function, you'll need to implement the logic for extracting the filename from the request, validating it, and then reading and returning the file's content. Here's a basic implementation:

```python
import os
from flask import Flask, request, abort, jsonify

app = Flask(__name__)

# Define a directory where files are stored
FILE_DIRECTORY = '/path/to/your/files'  # Change this to your actual directory

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    # Get the filename from the request arguments
    filename = request.args.get('filename')

    # Validate the filename
    if not filename:
        return jsonify({"error": "Filename is required"}), 400

    # Prevent directory traversal attacks
    if '..' in filename or filename.startswith('/'):
        return jsonify({"error": "Invalid filename"}), 400

    # Construct the full file path
    file_path = os.path.join(FILE_DIRECTORY, filename)

    # Check if the file exists
    if not os.path.isfile(file_path):
        return jsonify({"error": "File not found"}), 404

    # Read and return the file content
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data, 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

### Key Points:

1. **Filename Extraction**: The filename is extracted from the request's query parameters using `request.args.get('filename')`.

2. **Validation**:
   - Ensure the filename is provided.
   - Prevent directory traversal attacks by checking for `..` or leading slashes in the filename.

3. **File Path Construction**: The full path to the file is constructed using `os.path.join`.

4. **File Existence Check**: Verify that the file exists using `os.path.isfile`.

5. **File Reading**: If the file exists, read its content and return it. Handle any exceptions that might occur during file operations.

6. **Error Handling**: Return appropriate error messages and status codes for different failure scenarios.

Make sure to replace `'/path/to/your/files'` with the actual directory path where your files are stored.