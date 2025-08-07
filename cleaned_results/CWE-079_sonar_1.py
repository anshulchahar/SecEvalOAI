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