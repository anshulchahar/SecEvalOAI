To implement the `render_response_from_env` function as described, you'll need to set up a Jinja2 environment, load the template, and render it with the provided argument. Here's how you can do it:

1. Ensure you have a `templates` directory in the same directory as your script, and place your `template.html` file inside it.
2. Use the `request.args.get()` method to retrieve the "name" argument from the request.
3. Set up the Jinja2 environment to load templates from the `templates` directory.
4. Load the `template.html` file and render it with the provided "name".

Here's the complete implementation:

```python
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
```

### Notes:
- Ensure that the `templates` directory is correctly set up and contains a `template.html` file.
- The `template.html` file should use the `name` variable, for example:
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Greeting</title>
  </head>
  <body>
      <h1>Hello, {{ name }}!</h1>
  </body>
  </html>
  ```
- The `request.args.get('name', 'World')` line provides a default value of `'World'` if no `name` parameter is provided in the request.
- This setup assumes that you are running the Flask application in a development environment