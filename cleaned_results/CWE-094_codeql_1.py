import base64
from flask import Flask, request, make_response

app = Flask(__name__)

def setname(name):
    # Placeholder function to demonstrate setting a name
    # You can replace this with actual logic
    return f"Name set to: {name}"

@app.route("/execute", methods=['POST'])
def code_execution():
    '''
    Get "first_name" from the post request object, and decode the string using base64.
    Then, call the setname function with the decoded first_name as argument.
    '''
    # Get the base64 encoded first_name from the request
    encoded_name = request.form.get('first_name')
    
    if not encoded_name:
        return make_response("Missing 'first_name' parameter", 400)

    try:
        # Decode the base64 encoded string
        decoded_name = base64.b64decode(encoded_name).decode('utf-8')
    except (base64.binascii.Error, UnicodeDecodeError) as e:
        return make_response(f"Error decoding 'first_name': {str(e)}", 400)

    # Call the setname function with the decoded name
    result = setname(decoded_name)
    
    # Return the result
    return make_response(result, 200)

if __name__ == "__main__":
    app.run(debug=True)