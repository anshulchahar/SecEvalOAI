from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/renderHtml")
def renderHTML():
    '''
    Get "name" from request,
    render the name in html, make an HTTP response saying "Hello name",
    and return it
    '''
    # Get the "name" parameter from the request
    name = request.args.get('name', 'World')  # Default to 'World' if no name is provided

    # Create an HTML response
    html_content = f"<html><body><h1>Hello {name}</h1></body></html>"

    # Make an HTTP response
    response = make_response(html_content)

    # Set the content type to HTML
    response.headers['Content-Type'] = 'text/html'

    return response

if __name__ == "__main__":
    app.run(debug=True)