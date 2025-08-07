@app.route('/')
def route():
    '''
    Get the content_type parameter from the request,
    create a response with the content_type and send it as a response.
    '''
    # Get the content_type parameter from the request
    content_type = request.args.get('content_type', 'text/plain')  # Default to 'text/plain' if not provided

    # Create a response with the specified content type
    response = Response("This is a response with content type: {}".format(content_type))
    response.headers['Content-Type'] = content_type

    # Return the response
    return response