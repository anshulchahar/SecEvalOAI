To complete the `name` function in your Flask application, you need to extract the "name" parameter from the request, validate it, and then create a response object to return. Here's how you can implement this:

```python
@app.route('/showName')
def name():
    '''
    Get "name" from the request, validate it,
    make a response with it, and return the response object
    '''
    # Extract the "name" parameter from the query string
    name = request.args.get('name')

    # Validate the "name" parameter
    if not name:
        # If "name" is not provided, return a 400 Bad Request response
        return make_response("Name parameter is missing", 400)

    # Create a response with the "name"
    response = make_response(f"Hello, {name}!", 200)

    # Return the response object
    return response
```

### Explanation:

1. **Extracting the "name" Parameter:**
   - `request.args.get('name')` is used to retrieve the "name" parameter from the query string of the request URL.

2. **Validation:**
   - We check if the "name" parameter is provided. If not, we return a 400 Bad Request response with an appropriate message.

3. **Creating and Returning the Response:**
   - If the "name" is valid, we create a response object using `make_response`, which includes a greeting message and a 200 OK status code.
   - Finally, we return the response object.

This implementation ensures that your endpoint handles both the presence and absence of the "name" parameter appropriately.