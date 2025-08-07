The function name `redirect` in your code conflicts with the `redirect` function imported from Flask. It's a good practice to use a different name for your route handler to avoid this conflict. Here's how you can implement the redirection functionality:

```python
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def redirect_user():
    '''
    Redirect the user to the next_url specified in the GET request.
    '''
    next_url = request.args.get('next_url')
    if next_url:
        return redirect(next_url)
    else:
        return "No URL provided for redirection", 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
- **Function Name**: The route handler is renamed to `redirect_user` to avoid conflict with the `redirect` function from Flask.
- **Query Parameter**: The `next_url` is extracted from the query parameters using `request.args.get('next_url')`.
- **Redirection**: If `next_url` is provided, the user is redirected to that URL using Flask's `redirect` function.
- **Error Handling**: If `next_url` is not provided, the server responds with a 400 status code and an error message.

### Running the Application:
- Make sure to run the application in a suitable environment where Flask is installed.
- Access the application in a web browser or via a tool like `curl` or Postman, and provide the `next_url` as a query parameter, e.g., `http://localhost:5000/?next_url=http://example.com`.