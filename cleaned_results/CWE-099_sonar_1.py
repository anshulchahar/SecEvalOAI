@app.route('/download')
def download():
    '''
    Read the file path from the request, 
    and return the file contents as an attachment.
    '''
    # Get the file path from the request arguments
    file_path = request.args.get('file_path')
    
    if not file_path:
        return "File path is required", 400

    try:
        # Send the file as an attachment
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError:
        return "File not found", 404
    except Exception as e:
        return str(e), 500