To complete the `renderHTML` function, you need to extract the "name" parameter from the request, create an HTML response that includes the name, and return it. Here's how you can implement this:

```python
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/renderHtml")
def renderHTML():
    '''
    Get "name" from request,
    render the name in html, make an HTTP response saying "Hello name",
    and return it
    '''
    # Get the "name" parameter from the request
    name = request.args.get('name', 'World')  # Default to 'World' if no name is provided

    # Create an HTML response
    html_content = f"<html><body><h1>Hello {name}</h1></body></html>"

    # Make an HTTP response
    response = make_response(html_content)

    # Set the content type to HTML
    response.headers['Content-Type'] = 'text/html'

    return response

if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation:

1. **Request Parameter**: The `request.args.get('name', 'World')` line retrieves the "name" parameter from the query string. If the parameter is not provided, it defaults to "World".

2. **HTML Content**: The `html_content` variable contains a simple HTML structure that includes the name.

3. **Response Creation**: The `make_response` function is used to create an HTTP response with the HTML content.

4. **Content-Type Header**: The `response.headers['Content-Type'] = 'text/html'` line ensures that the response is treated as HTML by the client.

5. **Running the App**: The `app.run(debug=True)` line starts the Flask application in debug mode, which is useful for development.