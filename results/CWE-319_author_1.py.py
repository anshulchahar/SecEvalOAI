To implement the `do_login` function, you need to handle the POST request by extracting the username and password from the request, checking the credentials, and managing the session. Here's how you can do it:

```python
@app.route('/login', methods=['POST'])
def do_login():
    # Get the username and password from the request form
    username = request.form.get('username')
    password = request.form.get('password')

    # Check whether the credentials are valid
    if check_credentials(username, password):
        # Generate a new session ID
        session_id = secrets.token_hex(16)

        # Create a response object
        response = make_response("Login successful!")

        # Store the session ID in a cookie
        response.set_cookie('session_id', session_id)

        # Return the response
        return response
    else:
        # If credentials are invalid, return an error message
        return "Invalid credentials", 401
```

### Explanation:

1. **Extracting Data**: The `request.form.get()` method is used to extract the `username` and `password` from the POST request form data.

2. **Credential Check**: The `check_credentials()` function is called to verify if the provided credentials are valid. In this example, it always returns `True`, but you should implement actual logic to verify credentials against a database or another data source.

3. **Session Management**: If the credentials are valid, a new session ID is generated using `secrets.token_hex(16)`. This provides a secure random session ID.

4. **Response and Cookie**: A response object is created, and the session ID is stored in a cookie using `response.set_cookie()`. The cookie is then sent back to the client.

5. **Error Handling**: If the credentials are invalid, an error message is returned with a 401 status code, indicating unauthorized access.

Make sure to replace the `check_credentials` function with actual logic to verify user credentials securely.