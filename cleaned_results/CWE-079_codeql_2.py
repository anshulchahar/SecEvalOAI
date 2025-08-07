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