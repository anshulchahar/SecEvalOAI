To implement the `viewName` function as described, you need to read the HTML template file, replace the placeholder with the provided name parameter, and return the modified content as a response. Here's how you can do it:

```python
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/view', methods=['GET'])
def viewName():
    '''
    Get the param "name" from the request.
    Open the "templates/xss_shared.html" file and replace  "{{name}}" with the "name" param.
    return the html file as a response.
    '''
    # Get the 'name' parameter from the request
    name = request.args.get('name', '')

    # Open the HTML template file
    try:
        with open('templates/xss_shared.html', 'r') as file:
            html_content = file.read()
    except FileNotFoundError:
        return "Template file not found", 404

    # Replace the placeholder with the actual name
    html_content = html_content.replace('{{name}}', name)

    # Return the modified HTML content as a response
    response = make_response(html_content)
    response.headers['Content-Type'] = 'text/html'
    return response

if __name__ == '__main__':
    app.run(debug=True)
```

### Key Points:

1. **Reading the Parameter**: The `request.args.get('name', '')` retrieves the `name` parameter from the query string. If the parameter is not provided, it defaults to an empty string.

2. **File Handling**: The HTML template is read from the file `templates/xss_shared.html`. If the file does not exist, a 404 error is returned.

3. **String Replacement**: The placeholder `{{name}}` in the HTML content is replaced with the value of the `name` parameter.

4. **Response Construction**: The modified HTML content is returned as a response with the `Content-Type` set to `text/html`.

5. **Security Consideration**: This implementation directly injects user input into HTML, which can lead to XSS (Cross-Site Scripting) vulnerabilities. In a real-world application, you should sanitize user input to prevent such vulnerabilities. Consider using templating engines like Jinja2, which Flask uses by default, to automatically escape user input.