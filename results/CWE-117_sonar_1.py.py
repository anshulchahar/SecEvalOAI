To log the "input" from a GET request as an error using Flask, you can access the query parameter from the request object and then use the application's logger to log it. Here's how you can implement the `log` function:

```python
from flask import request, current_app, Flask

app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Get the "input" from the GET request and log it as an error.
    '''
    # Retrieve the "input" parameter from the query string
    input_value = request.args.get('input', '')

    # Log the input value as an error
    current_app.logger.error(f"Logged input: {input_value}")

    return "Input logged as error.", 200

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:
- **`request.args.get('input', '')`**: This retrieves the value of the "input" query parameter from the URL. If the parameter is not provided, it defaults to an empty string.
- **`current_app.logger.error(...)`**: This logs the retrieved input value as an error using Flask's built-in logging system.
- **`return "Input logged as error.", 200`**: This returns a simple response to the client indicating that the input has been logged.

### Usage:
To test this, you can run the Flask application and make a GET request to the `/log` endpoint with an "input" query parameter, like so:

```
http://localhost:5000/log?input=TestError
```

This will log "TestError" as an error in the application's log.