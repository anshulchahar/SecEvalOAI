To implement the `/normal` route that performs an LDAP search based on the domain component (dc) and username provided in the request, you need to handle the LDAP connection and search appropriately. Below is an example of how you might implement this functionality using the `ldap3` library:

```python
from flask import request, Flask, jsonify
from ldap3 import Server, Connection, ALL, SUBTREE

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the domain component and username from the request arguments
    dc = request.args.get('dc')
    username = request.args.get('username')

    if not dc or not username:
        return jsonify({"error": "Missing 'dc' or 'username' parameter"}), 400

    # Construct the LDAP server and connection
    server = Server('localhost', get_info=ALL)
    conn = Connection(server, auto_bind=True)

    # Construct the search base and search filter
    search_base = f"dc={dc}"
    search_filter = f"(uid={username})"

    # Perform the search
    conn.search(search_base, search_filter, search_scope=SUBTREE, attributes=['*'])

    # Check if any entries were found
    if not conn.entries:
        return jsonify({"error": "User not found"}), 404

    # Return the found user(s) as JSON
    users = [entry.entry_to_json() for entry in conn.entries]
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)
```

### Key Points:

1. **Input Validation**: The code checks if both `dc` and `username` are provided in the request. If not, it returns a 400 error with a message indicating the missing parameter.

2. **LDAP Connection**: The `ldap3` library is used to establish a connection to the LDAP server running on `localhost`. The `auto_bind=True` parameter automatically binds the connection.

3. **LDAP Search**: The search is performed using the `search` method, specifying the search base and filter. The search scope is set to `SUBTREE` to search through all levels of the directory.

4. **Response**: If no entries are found, a 404 error is returned. Otherwise, the found entries are converted to JSON and returned in the response.

5. **Security Considerations**: This example assumes a local LDAP server without authentication. In a production environment, you should handle authentication securely