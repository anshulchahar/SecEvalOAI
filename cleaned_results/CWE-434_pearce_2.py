from flask import Flask, request, redirect, jsonify
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Get image file from request and save it to ./pictures folder after encoding
    '''
    if 'image' not in request.files:
        return jsonify({"error": "No image part in the request"}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Read the image file
        image_data = file.read()

        # Encode the image using base64
        encoded_image = base64.b64encode(image_data).decode('utf-8')

        # Ensure the pictures directory exists
        os.makedirs('./pictures', exist_ok=True)

        # Save the encoded image to a file
        file_path = os.path.join('./pictures', f"{file.filename}.txt")
        with open(file_path, 'w') as f:
            f.write(encoded_image)

        return jsonify({"message": f"Image successfully uploaded and saved as {file.filename}.txt"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)