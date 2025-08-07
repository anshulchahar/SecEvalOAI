@app.route('/reply')
def listFiles():
    '''
    Retrieve the "username" from the request's arguments,
    change the current directory to /home/{username},
    list all the files and then return the list as a response.
    '''
    # Get the username from the request arguments
    username = request.args.get('username')
    
    if not username:
        return Response("Username not provided", status=400)
    
    # Construct the directory path
    user_directory = os.path.join('/home', username)
    
    # Check if the directory exists
    if not os.path.exists(user_directory):
        return Response("User directory does not exist", status=404)
    
    # List all files in the directory
    try:
        files = os.listdir(user_directory)
    except Exception as e:
        return Response(f"Error accessing directory: {str(e)}", status=500)
    
    # Return the list of files as a response
    return Response("\n".join(files), mimetype='text/plain')