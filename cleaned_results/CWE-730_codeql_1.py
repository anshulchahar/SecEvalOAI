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