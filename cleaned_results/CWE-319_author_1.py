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