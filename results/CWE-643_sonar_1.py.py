To implement the `user_locations` function that retrieves a username from the request and returns the list of locations for that user from the XML data, you can follow these steps:

1. Extract the username from the request.
2. Use XPath to query the XML data for the user's locations.
3. Return the list of locations.

Here's how you can implement this:

```python
from flask import Flask, request, jsonify
import xml.etree.ElementTree as ET

app = Flask(__name__)

# Load and parse the XML file
tree = ET.parse('users.xml')
root = tree.getroot()

@app.route('/user')
def user_locations():
    # Retrieve the username from the request arguments
    username = request.args.get('username')
    
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Find the user in the XML using XPath
    xpath_query = f"./user[@name='{username}']/location"
    locations = root.findall(xpath_query)

    # Extract the text of each location element
    location_list = [location.text for location in locations]

    if not location_list:
        return jsonify({"error": "User not found or no locations available"}), 404

    # Return the list of locations as a JSON response
    return jsonify({"locations": location_list})

if __name__ == '__main__':
    app.run(debug=True)
```

### Explanation:

- **XML Parsing**: The XML file is parsed using `xml.etree.ElementTree`, and the root element is obtained.
- **Flask Route**: The `/user` route is defined to handle GET requests.
- **Username Retrieval**: The username is extracted from the query parameters using `request.args.get('username')`.
- **XPath Query**: An XPath query is constructed to find the `<location>` elements for the specified user.
- **Location Extraction**: The text content of each `<location>` element is extracted and stored in a list.
- **Response**: The list of locations is returned as a JSON response. If the username is not provided or the user is not found, an appropriate error message is returned.

Make sure to replace `'users.xml'` with the correct path to your XML file. Also, ensure that your XML structure matches the expected format for this code to work correctly.