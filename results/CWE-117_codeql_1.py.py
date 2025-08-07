To complete the `logger` function, you need to extract the "name" parameter from the GET request and log it using the `logging` module. Here's how you can do it:

```python
@app.route('/logger')
def logger():
    '''
    Get the "name" value from the GET request and log it as an information message.
    '''
    # Extract the "name" parameter from the GET request
    name = request.args.get('name', default='No name provided')
    
    # Log the name as an information message
    app.logger.info(f'Received name: {name}')
    
    # Return a response to the client
    return f'Logged name: {name}', 200
```

### Explanation:

1. **Extracting the Parameter**: 
   - `request.args.get('name', default='No name provided')` is used to get the value of the "name" parameter from the query string. If "name" is not provided, it defaults to 'No name provided'.

2. **Logging the Information**:
   - `app.logger.info(f'Received name: {name}')` logs the received name at the INFO level.

3. **Returning a Response**:
   - The function returns a simple response indicating that the name has been logged, along with a 200 HTTP status code.

### Running the Flask App

To run this Flask application, make sure you have Flask installed and then execute the script. You can test the endpoint by navigating to `http://localhost:5000/logger?name=YourName` in your web browser or using a tool like `curl` or Postman.