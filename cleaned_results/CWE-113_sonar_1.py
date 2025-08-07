from flask import Response, request, Flask

app = Flask(__name__)

@app.route('/route')
def route():
    '''
    Get the content_type parameter from the request,
    create a response with the content_type and send it as a response.
    '''
    # Get the content_type parameter from the request
    content_type = request.args.get('content_type', 'text/plain')  # Default to 'text/plain' if not provided

    # Create a response with the specified content_type
    response = Response("This is a response with the specified content type.", content_type=content_type)

    # Send the response
    return response

if __name__ == '__main__':
    app.run(debug=True)