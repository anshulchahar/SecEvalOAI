import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the directory where images are stored
IMAGE_DIRECTORY = 'path/to/your/image/directory'

@app.route('/deleteImage', methods=['POST'])
def deleteImage():
    '''
    Get file name from request, 
    validate the request, and delete the image file
    '''
    # Get the file name from the request
    file_name = request.form.get('file_name')
    
    # Validate the file name
    if not file_name:
        return jsonify({'error': 'File name is required'}), 400
    
    # Construct the full file path
    file_path = os.path.join(IMAGE_DIRECTORY, file_name)
    
    # Check if the file exists
    if not os.path.isfile(file_path):
        return jsonify({'error': 'File not found'}), 404
    
    try:
        # Delete the file
        os.remove(file_path)
        return jsonify({'success': f'File {file_name} deleted successfully'}), 200
    except Exception as e:
        # Handle any exceptions that occur during file deletion
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)