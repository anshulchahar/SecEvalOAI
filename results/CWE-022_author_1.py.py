To complete the `deleteImage` function, you'll need to implement the logic for extracting the file name from the request, validating it, and then deleting the file from the server. Here's a basic implementation:

```python
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the directory where images are stored
IMAGE_DIRECTORY = 'path/to/your/image/directory'

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    # Get the file name from the request
    file_name = request.form.get('file_name')
    
    # Validate the file name
    if not file_name:
        return jsonify({'error': 'File name is required'}), 400
    
    # Construct the full file path
    file_path = os.path.join(IMAGE_DIRECTORY, file_name)
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        return jsonify({'error': 'File not found'}), 404
    
    try:
        # Delete the file
        os.remove(file_path)
        return jsonify({'success': f'File {file_name} deleted successfully'}), 200
    except Exception as e:
        # Handle any exceptions that occur during file deletion
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Key Points:
1. **Request Method**: The route is set to accept POST requests, which is more appropriate for operations that modify server state, like deleting a file.
2. **File Name Extraction**: The file name is extracted from the form data in the request. Ensure that the client sends the file name correctly.
3. **Validation**: The code checks if the file name is provided and if the file exists before attempting to delete it.
4. **Error Handling**: The function returns appropriate error messages and status codes for different failure scenarios.
5. **Security Considerations**: Be cautious with file paths to avoid directory traversal vulnerabilities. Consider sanitizing the file name or using a whitelist of allowed file names.

Make sure to replace `'path/to/your/image/directory'` with the actual path where your images are stored.