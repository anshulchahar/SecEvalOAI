@app.route("/full_ssrf")
def full_ssrf():
    '''
    Get the subdomain from the request and use it as the url, make a request to the url, and return the response
    '''
    # Get the 'url' parameter from the query string
    url = request.args.get('url')
    
    if not url:
        return "No URL provided", 400

    try:
        # Make a request to the provided URL
        response = requests.get(url)
        
        # Return the response content
        return response.content, response.status_code
    except requests.exceptions.RequestException as e:
        # Handle exceptions and return an error message
        return f"An error occurred: {str(e)}", 500