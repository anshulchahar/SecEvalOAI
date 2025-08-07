To implement the `redirectToTarget` function, you'll need to extract the target URL from the request, validate it using a regular expression, and then redirect to it if it's valid. Here's how you can do it:

```python
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
```

### Explanation:

1. **Extracting the Target URL**: The `request.args.get('target', '')` line extracts the `target` parameter from the query string. If it's not present, it defaults to an empty string.

2. **Regular Expression for URL Validation**: The `url_pattern` is a regular expression designed to match valid URLs. It checks for optional `http://` or `https://`, a valid domain, and an optional path.

3. **Validation and Redirection**: The `re.match(url_pattern, target_url)` checks if the extracted URL matches the pattern. If it does, the `redirect(target_url)` function is called to redirect the user. If not, an error message is returned with a 400 status code indicating a bad request.

4. **Running the App**: The `if __name__ == '__main__':` block ensures that the Flask app runs when the script is executed directly. The `debug=True` argument enables debug mode, which is helpful during development.