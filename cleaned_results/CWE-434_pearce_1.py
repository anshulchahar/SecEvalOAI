from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)

# Ensure the uploads directory exists
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/pdf/upload', methods=['GET', 'POST'])
def upload_pdf():
    '''
    Get PDF file from request, save it to ./uploads directory, and redirect to /pdf/view
    '''
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return 'No file part', 400
        file = request.files['file']
        # If the user does not select a file, the browser may submit an empty part without filename
        if file.filename == '':
            return 'No selected file', 400
        # Save the file if it is a PDF
        if file and file.filename.endswith('.pdf'):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            return redirect(url_for('view_pdf'))
    # If GET request, show a simple upload form
    return '''
    <!doctype html>
    <title>Upload PDF</title>
    <h1>Upload PDF</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/pdf/view')
def view_pdf():
    '''
    Placeholder for viewing PDFs
    '''
    return 'PDFs uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)