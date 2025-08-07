To implement the `/download` route in your Flask application, you need to extract the file name from the request, construct the file path, and then use `send_file` to send the file as an attachment to the client. Here's how you can do it:

```python
from flask import request, send_file, Flask, abort
import os

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Get the file name from the request and parse the name to get the file path
    Send the file to the client as an attachment.
    '''
    # Get the file name from the request arguments
    file_name = request.args.get('file_name')

    # Check if the file name is provided
    if not file_name:
        abort(400, description="File name is required")

    # Construct the file path (assuming files are stored in a directory named 'files')
    file_path = os.path.join('files', file_name)

    # Check if the file exists
    if not os.path.exists(file_path):
        abort(404, description="File not found")

    # Send the file as an attachment
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
```

### Key Points:
1. **Request Argument**: The file name is expected to be passed as a query parameter in the URL, e.g., `/download?file_name=example.txt`.
2. **File Path Construction**: The file path is constructed by joining a directory (e.g., `files`) with the file name. Ensure that the directory exists and contains the files you want to serve.
3. **Error Handling**: 
   - If the file name is not provided, a `400 Bad Request` error is returned.
   - If the file does not exist, a `404 Not Found` error is returned.
4. **Security Considerations**: Be cautious with file paths to prevent directory traversal attacks. You might want to sanitize the file name or use a whitelist of allowed files.

Make sure to replace `'files'` with the actual directory where your files are stored. Also, ensure that the Flask application has the necessary permissions to read the files from this directory.