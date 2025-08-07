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