To implement the `/upload` endpoint that processes an XML file from the request and checks the user ID and password, you can follow these steps. This example assumes that the XML file contains user credentials and that you have a `checkPassword` function to validate them.

Here's how you can implement the `upload` function:

```python
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
```

### Explanation:

1. **File Check**: The code first checks if the request contains a file part and if a file is selected. If not, it returns an appropriate error message.

2. **XML Parsing**: The uploaded file is parsed using `lxml.etree.parse()`. This assumes the file is a valid XML document.

3. **Extracting Data**: The code extracts the `userid` and `password` from the XML. It assumes a specific XML structure where these elements are direct children of the root.

4. **Validation**: The extracted credentials are validated using the `checkPassword` function. The response is based on whether the credentials are valid or not.

5. **Error Handling**: The code includes basic error handling for missing file parts, invalid XML structures, and XML syntax errors.

Make sure to implement the `checkPassword` function to perform the actual validation logic based on your application's requirements.