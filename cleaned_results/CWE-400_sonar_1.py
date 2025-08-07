import re
from flask import request, Flask, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['GET'])
def upload():
    '''
    Get the username and a file attachment from the HTTP GET request.
    Then, search the username in the filename of the attachment.
    '''
    # Get the username from the query parameters
    username = request.args.get('username')
    
    # Get the file from the request
    file = request.files.get('file')
    
    # Check if both username and file are provided
    if not username or not file:
        return jsonify({'error': 'Username and file are required'}), 400
    
    # Get the filename
    filename = file.filename
    
    # Search for the username in the filename
    if re.search(username, filename):
        return jsonify({'message': 'Username found in filename'}), 200
    else:
        return jsonify({'message': 'Username not found in filename'}), 404

if __name__ == '__main__':
    app.run(debug=True)