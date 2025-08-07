To implement the `/normal` route as described, you need to handle the LDAP connection and query safely. However, it's important to note that directly using user input in LDAP queries can lead to LDAP injection vulnerabilities. Always sanitize and validate user inputs before using them in queries.

Here's an example implementation with basic error handling and input validation:

```python
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
```

### Key Points:

1. **Input Validation and Sanitization**: Ensure that inputs are validated and sanitized to prevent LDAP injection attacks. The example uses `ldap.filter.escape_filter_chars()` to escape special characters in the LDAP filter.

2. **Error Handling**: Proper error handling is implemented to catch and return LDAP errors.

3. **Anonymous Bind**: This example uses an anonymous bind (`simple_bind_s()` without credentials), which may not be suitable for all LDAP servers. You might need to provide credentials depending on your LDAP server's configuration.

4. **Security Considerations**: Always consider additional security measures such as using secure connections (