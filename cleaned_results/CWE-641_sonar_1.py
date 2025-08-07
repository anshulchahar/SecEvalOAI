from flask import request, send_file, Flask, abort
import os

app = Flask(__name__)

@app.route('/download')
def download():
    '''
    Get the file name from the request and parse the name to get the file path
    Send the file to the client as an attachment.
    '''
    # Get the file name from the request arguments
    file_name = request.args.get('file_name')

    # Check if the file name is provided
    if not file_name:
        abort(400, description="File name is required")

    # Construct the file path (assuming files are stored in a directory named 'files')
    file_path = os.path.join('files', file_name)

    # Check if the file exists
    if not os.path.exists(file_path):
        abort(404, description="File not found")

    # Send the file as an attachment
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)