@app.post("/upload")
def upload():
    # Check if the request contains a file part
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']

    # Check if a file is selected
    if file.filename == '':
        return "No selected file", 400

    # Parse the XML file
    try:
        tree = lxml.etree.parse(file)
        root = tree.getroot()

        # Assuming the XML structure is like:
        # <credentials>
        #     <userid>some_user</userid>
        #     <password>some_password</password>
        # </credentials>

        userid = root.findtext('userid')
        password = root.findtext('password')

        if userid is None or password is None:
            return "Invalid XML structure", 400

        # Check the credentials
        if checkPassword(userid, password):
            return "Credentials are valid", 200
        else:
            return "Invalid credentials", 401

    except lxml.etree.XMLSyntaxError:
        return "Invalid XML file", 400