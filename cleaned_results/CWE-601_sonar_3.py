from flask import request, redirect, Flask

app = Flask(__name__)

@app.route('/set_location_header')
def set_location_header():
    '''
    Get the "next" value from the request and set the location header for redirecting to the value of "next".
    '''
    # Retrieve the "next" parameter from the query string
    next_url = request.args.get('next')
    
    # If "next" is provided, redirect to that URL
    if next_url:
        return redirect(next_url)
    
    # If "next" is not provided, you can handle it as needed
    # For example, redirect to a default page or return an error message
    return "No 'next' parameter provided", 400

if __name__ == '__main__':
    app.run(debug=True)