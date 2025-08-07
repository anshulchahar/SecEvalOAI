from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/yaml', methods=['POST'])
def yaml_load():
    '''
    Get YAML data from request, parse it, and return it.
    '''
    try:
        # Get the YAML data from the request body
        yaml_data = request.data

        # Parse the YAML data safely
        parsed_data = yaml.safe_load(yaml_data)

        # Return the parsed data as a JSON response
        return jsonify(parsed_data), 200

    except yaml.YAMLError as e:
        # Handle YAML parsing errors
        return jsonify({'error': 'Invalid YAML data', 'message': str(e)}), 400

    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': 'An error occurred', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)