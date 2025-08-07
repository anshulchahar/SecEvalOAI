from flask import request, redirect, Flask

app = Flask(__name__)

@app.route('/flask_redirect')
def flask_redirect():
    '''
    Get the url from the request and redirect to it
    '''
    # Get the 'url' parameter from the query string
    target_url = request.args.get('url')
    
    # Check if the 'url' parameter is provided
    if target_url:
        return redirect(target_url)
    else:
        # Handle the case where 'url' parameter is missing
        return "No URL provided to redirect to.", 400

if __name__ == '__main__':
    app.run(debug=True)