To implement the `/direct` route that extracts a regex pattern and text from a GET request and searches the text using the provided regex, you can use the following code:

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/direct")
def direct():
    '''
    Get the regex from the 'pattern' in the GET request,
    get the 'text' from the GET request,
    and search the 'text' with the provided regex.
    '''
    # Extract 'pattern' and 'text' from the GET request
    pattern = request.args.get('pattern')
    text = request.args.get('text')

    # Check if both 'pattern' and 'text' are provided
    if not pattern or not text:
        return jsonify({"error": "Both 'pattern' and 'text' parameters are required."}), 400

    # Search the text using the provided regex pattern
    try:
        match = re.search(pattern, text)
        if match:
            # Return the matched string and its position
            return jsonify({
                "match": match.group(),
                "start": match.start(),
                "end": match.end()
            })
        else:
            return jsonify({"match": None})
    except re.error as e:
        return jsonify({"error": f"Invalid regex pattern: {str(e)}"}), 400

if __name__ == "__main__":
    app.run(debug=True)
```

### Explanation:
- **Import Statements**: We import `Flask`, `request`, and `jsonify` from the `flask` module, and `re` for regex operations.
- **Flask App Initialization**: We create an instance of the `Flask` class.
- **Route Definition**: We define the `/direct` route using the `@app.route` decorator.
- **Parameter Extraction**: We use `request.args.get()` to extract the `pattern` and `text` parameters from the GET request.
- **Validation**: We check if both `pattern` and `text` are provided. If not, we return a 400 error with a message.
- **Regex Search**: We use `re.search()` to search the text with the provided regex pattern.
- **Error Handling**: We handle invalid regex patterns using a try-except block and return a 400 error if the pattern is invalid.
- **Response**: If a match is found, we return the matched string and