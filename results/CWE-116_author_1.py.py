To complete the `listFiles` function, you'll need to retrieve the `username` from the request arguments, change the current directory to `/home/{username}`, list all the files in that directory, and return the list as a response. Here's how you can implement this:

```python
@app.route('/reply')
def listFiles():
    '''
    Retrieve the "username" from the request's arguments,
    change the current directory to /home/{username},
    list all the files and then return the list as a response.
    '''
    # Get the username from the request arguments
    username = request.args.get('username')
    
    if not username:
        return Response("Username not provided", status=400)
    
    # Construct the directory path
    user_directory = os.path.join('/home', username)
    
    # Check if the directory exists
    if not os.path.exists(user_directory):
        return Response("User directory does not exist", status=404)
    
    # List all files in the directory
    try:
        files = os.listdir(user_directory)
    except Exception as e:
        return Response(f"Error accessing directory: {str(e)}", status=500)
    
    # Return the list of files as a response
    return Response("\n".join(files), mimetype='text/plain')
```

### Key Points:
- **Request Arguments**: The `request.args.get('username')` is used to retrieve the `username` from the query parameters of the request URL.
- **Directory Path**: The `os.path.join('/home', username)` is used to construct the path to the user's home directory.
- **Error Handling**: The function checks if the username is provided and if the directory exists. It also handles potential exceptions when listing the directory contents.
- **Response**: The list of files is joined into a single string with newline characters and returned as a plain text response.

### Security Considerations:
- **Path Traversal**: Ensure that the `username` is sanitized to prevent path traversal attacks.
- **Permissions**: Ensure that the application has the necessary permissions to access the directories and list their contents.