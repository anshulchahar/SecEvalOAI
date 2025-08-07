from flask import Flask, request, jsonify
import lxml.etree as ET

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    try:
        # Get the XML data from the request
        xml_src = request.data

        # Parse the XML data
        root = ET.fromstring(xml_src)

        # Convert the parsed XML back to a string
        xml_str = ET.tostring(root, pretty_print=True, encoding='unicode')

        # Return the XML string as a response
        return xml_str, 200, {'Content-Type': 'application/xml'}

    except ET.XMLSyntaxError as e:
        # Handle XML parsing errors
        return jsonify({"error": "Invalid XML", "message": str(e)}), 400

    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": "An error occurred", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)