from flask import request, Flask, jsonify
import ldap

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Validate inputs
    if not dc or not username:
        return jsonify({"error": "Missing dc or username parameter"}), 400

    # Sanitize inputs (basic example, consider more robust validation)
    if any(char in dc for char in ";()&|") or any(char in username for char in ";()&|"):
        return jsonify({"error": "Invalid characters in input"}), 400

    # Create an LDAP query
    search_filter = f"(uid={ldap.filter.escape_filter_chars(username)})"
    search_base = f"dc={ldap.filter.escape_filter_chars(dc)},dc=com"

    try:
        # Establish an LDAP connection on localhost
        ldap_connection = ldap.initialize("ldap://localhost")
        ldap_connection.simple_bind_s()  # Anonymous bind

        # Search for the user in the LDAP
        result = ldap_connection.search_s(search_base, ldap.SCOPE_SUBTREE, search_filter)

        # Close the connection
        ldap_connection.unbind_s()

        # Return the result
        return jsonify(result)

    except ldap.LDAPError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)