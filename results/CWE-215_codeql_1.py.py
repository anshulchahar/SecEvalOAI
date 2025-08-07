To run the Flask application you've defined, you need to ensure that the script is executed as the main program. Here's how you can modify your script to run the Flask application:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/crash')
def main():
    raise Exception()

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:

1. **`if __name__ == '__main__':`**: This line checks if the script is being run directly (as opposed to being imported as a module in another script). If it is, the Flask application will start.

2. **`app.run(debug=True)`**: This starts the Flask development server. The `debug=True` argument enables debug mode, which provides helpful error messages and automatically reloads the server when code changes are detected.

### Running the Application:

1. Save your script to a file, for example, `app.py`.

2. Open a terminal and navigate to the directory where your `app.py` file is located.

3. Run the script using Python:

   ```bash
   python app.py
   ```

4. The Flask development server should start, and you can access your application by navigating to `http://127.0.0.1:5000/crash` in your web browser. This will trigger the exception you defined in the `/crash` route.

### Note:

- The `debug=True` setting is useful during development but should be turned off in a production environment for security reasons.
- Ensure you have Flask installed in your Python environment. If not, you can install it using pip:

  ```bash
  pip install flask
  ```