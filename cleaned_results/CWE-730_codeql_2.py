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