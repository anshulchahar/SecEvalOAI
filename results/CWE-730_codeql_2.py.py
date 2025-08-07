To implement the `/direct` route in your Flask application, you need to extract the `pattern` and `text` from the GET request, compile the regular expression pattern, and then use it to search within the provided text. Here's how you can do it:

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    '''
    Get the regular expression pattern from the GET request (pattern), compile it
    and then use it to search the string within the 'text' in the GET request.
    '''
    # Extract 'pattern' and 'text' from the request arguments
    pattern = request.args.get('pattern')
    text = request.args.get('text')

    # Check if both 'pattern' and 'text' are provided
    if not pattern or not text:
        return jsonify({"error": "Both 'pattern' and 'text' parameters are required"}), 400

    try:
        # Compile the regular expression pattern
        regex = re.compile(pattern)

        # Search for the pattern in the text
        match = regex.search(text)

        # Return the result
        if match:
            return jsonify({"match": match.group()}), 200
        else:
            return jsonify({"match": None}), 200
    except re.error as e:
        # Handle invalid regular expression patterns
        return jsonify({"error": f"Invalid regular expression pattern: {e}"}), 400

if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation:

1. **Import Statements**: Import necessary modules from Flask and the `re` module for regular expressions.

2. **Flask App Initialization**: Create a Flask application instance.

3. **Route Definition**: Define the `/direct` route using the `@app.route` decorator.

4. **Extract Parameters**: Use `request.args.get()` to extract `pattern` and `text` from the query parameters of the GET request.

5. **Validation**: Check if both `pattern` and `text` are provided. If not, return a 400 error with a message.

6. **Compile and Search**: Compile the regular expression pattern and search for it in the provided text.

7. **Return Result**: If a match is found, return the matched string. If no match is found, return `None`. Handle any exceptions related to invalid regular expressions and return an appropriate error message