from flask import Flask, request, render_template_string
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

@app.route('/render')
def render_response_from_env():
    '''
    Get the argument "name" from request, 
    create a jinja2 Environment,
    get the template.html from the environment, and render it.
    '''
    # Get the "name" argument from the request
    name = request.args.get('name', 'World')  # Default to 'World' if no name is provided

    # Set up the Jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'))

    # Load the template.html from the environment
    template = env.get_template('template.html')

    # Render the template with the provided name
    rendered_template = template.render(name=name)

    return rendered_template

if __name__ == '__main__':
    app.run(debug=True)