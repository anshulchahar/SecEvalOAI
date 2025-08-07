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