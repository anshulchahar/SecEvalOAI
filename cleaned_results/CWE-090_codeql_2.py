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