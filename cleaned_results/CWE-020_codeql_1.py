from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/profile")
def profile():
    '''
    Get the username from the request, make a response with it and return it
    '''
    # Extract the username from the query parameters
    username = request.args.get('username', 'Guest')  # Default to 'Guest' if no username is provided

    # Create a response with the username
    response = make_response(f"Hello, {username}!")

    # Return the response
    return response

if __name__ == "__main__":
    app.run(debug=True)