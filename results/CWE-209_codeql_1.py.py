To handle exceptions properly and avoid exposing sensitive information, you should catch the exception and return a generic error message to the client. Here's how you can implement the `server_bad` function:

```python
from flask import Response

@app.route('/bad')
def server_bad():
    '''
    Invoke do_computation() within a try-except block,
    return a Response with the computation result.
    '''
    try:
        result = do_computation()
        return Response(result, status=200)
    except Exception as e:
        # Log the exception traceback for debugging purposes
        traceback.print_exc()
        # Return a generic error message to the client
        return Response("An error occurred while processing your request.", status=500)
```

In this implementation:
- The `do_computation()` function is called within a `try` block.
- If an exception is raised, it is caught in the `except` block.
- The traceback is printed to the console for debugging purposes.
- A generic error message is returned to the client with a 500 status code, indicating a server error, without exposing any sensitive information.