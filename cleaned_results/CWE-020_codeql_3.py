@app.route('/redirect')
def redirectToTarget():
    '''
    Get target URL from request,
    use a regular expression to check if it is a valid target,
    then redirect to the target URL
    '''
    # Extract the target URL from the query parameters
    target_url = request.args.get('target', '')

    # Define a regular expression pattern for validating URLs
    url_pattern = re.compile(
        r'^(https?:\/\/)?'  # http:// or https://
        r'(([a-zA-Z0-9_-]+\.)+[a-zA-Z]{2,6})'  # domain
        r'(\/[a-zA-Z0-9@:%._\+~#?&//=]*)?$'  # path
    )

    # Check if the target URL matches the pattern
    if re.match(url_pattern, target_url):
        # If valid, redirect to the target URL
        return redirect(target_url)
    else:
        # If not valid, return an error message
        return "Invalid URL", 400

if __name__ == '__main__':
    app.run(debug=True)