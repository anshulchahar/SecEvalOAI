To complete the `profile` route, you'll want to extract the username from the request, create a response using that username, and then return the response. Here's how you can do it:

```python
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get the username from the request, make a response with it and return it
    '''
    # Extract the username from the query parameters
    username = request.args.get('username', 'Guest')  # Default to 'Guest' if no username is provided

    # Create a response with the username
    response = make_response(f"Hello, {username}!")

    # Return the response
    return response

if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation:

- **`request.args.get('username', 'Guest')`**: This line extracts the `username` from the query parameters of the request URL. If no username is provided, it defaults to `'Guest'`.

- **`make_response(f"Hello, {username}!")`**: This creates a response object with a message that includes the username.

- **`return response`**: This returns the response to the client.

### Usage:

To test this, you can run the Flask application and visit the following URLs:

- `http://localhost:5000/profile?username=John` will return "Hello, John!"
- `http://localhost:5000/profile` will return "Hello, Guest!" if no username is provided.