from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # Get the module version from the request arguments
    version = request.args.get('version', '')

    # Validate the version input to ensure it's safe
    if not version.replace('.', '').isdigit():
        return jsonify({"error": "Invalid version format"}), 400

    # Construct the import statement
    import_statement = f"import urllib{version} as urllib"

    try:
        # Execute the import statement
        exec(import_statement)
        # Assuming you want to return the version of the imported module
        return jsonify({"message": f"Successfully imported urllib version {version}"})
    except ImportError:
        return jsonify({"error": f"urllib version {version} not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)