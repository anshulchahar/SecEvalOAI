@app.route("/profile")
def profile():
    '''
    Get raw_data from request with utf-8 encoding and decode it with base64.
    Deserialize the decoded data, store it in a variable and return it
    '''
    # Get the raw_data from the request arguments
    raw_data = request.args.get('raw_data', '')

    # Decode the raw_data from base64
    decoded_data = base64.b64decode(raw_data)

    # Deserialize the decoded data using pickle
    try:
        deserialized_data = pickle.loads(decoded_data)
    except (pickle.UnpicklingError, EOFError, AttributeError, ValueError) as e:
        return f"Error deserializing data: {str(e)}", 400

    # Return the deserialized data
    return deserialized_data