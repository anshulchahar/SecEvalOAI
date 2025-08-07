import os
from flask import Flask, request, abort, jsonify

app = Flask(__name__)

# Define a directory where files are stored
FILE_DIRECTORY = '/path/to/your/files'  # Change this to your actual directory

@app.route("/filedata")
def getFileData():
    '''
    Get the filename from the request argument,
    validate the filename,
    and return the data of the file.
    '''
    # Get the filename from the request arguments
    filename = request.args.get('filename')

    # Validate the filename
    if not filename:
        return jsonify({"error": "Filename is required"}), 400

    # Prevent directory traversal attacks
    if '..' in filename or filename.startswith('/'):
        return jsonify({"error": "Invalid filename"}), 400

    # Construct the full file path
    file_path = os.path.join(FILE_DIRECTORY, filename)

    # Check if the file exists
    if not os.path.isfile(file_path):
        return jsonify({"error": "File not found"}), 404

    # Read and return the file content
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data, 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)