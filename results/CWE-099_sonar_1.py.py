To implement the `/download` route that reads a file path from the request and returns the file contents as an attachment, you can use the `send_file` function from Flask. Here's how you can complete the `download` function:

```python
@app.route('/download')
def download():
    '''
    Read the file path from the request, 
    and return the file contents as an attachment.
    '''
    # Get the file path from the request arguments
    file_path = request.args.get('file_path')
    
    if not file_path:
        return "File path is required", 400

    try:
        # Send the file as an attachment
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError:
        return "File not found", 404
    except Exception as e:
        return str(e), 500
```

### Explanation:
1. **Request Argument**: The file path is expected to be passed as a query parameter in the request URL, e.g., `/download?file_path=/path/to/your/file.txt`.

2. **Error Handling**: 
   - If the `file_path` is not provided, a 400 Bad Request response is returned.
   - If the file is not found, a 404 Not Found response is returned.
   - Any other exceptions are caught and returned with a 500 Internal Server Error response.

3. **Sending the File**: The `send_file` function is used to send the file as an attachment, which prompts the user to download the file.

Make sure to handle file paths carefully to avoid security issues like directory traversal attacks. Consider validating and sanitizing the file path input if this is a public-facing application.