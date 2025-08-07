@app.post("/upload")
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    try:
        # Read XML data from the request
        xml_data = request.data

        # Parse the XML data
        root = ET.fromstring(xml_data)

        # For demonstration, let's convert the XML to a dictionary
        def xml_to_dict(element):
            return {
                element.tag: {
                    "attributes": element.attrib,
                    "text": element.text,
                    "children": [xml_to_dict(child) for child in element]
                }
            }

        # Convert the root element to a dictionary
        xml_dict = xml_to_dict(root)

        # Return the parsed XML as a JSON response
        return xml_dict, 200

    except ET.ParseError as e:
        return {"error": "Invalid XML", "message": str(e)}, 400