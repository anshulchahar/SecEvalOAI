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