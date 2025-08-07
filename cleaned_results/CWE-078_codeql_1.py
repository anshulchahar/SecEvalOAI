import os
import shlex
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/command", methods=['POST'])
def executeCommand():
    '''
    Receive a command from a post request, 
    validate it, and execute it.
    '''
    # Get the command from the request
    command = request.json.get('command')

    # Validate the command
    if not command:
        return jsonify({'error': 'No command provided'}), 400

    # Define a list of allowed commands for security
    allowed_commands = ['ls', 'echo', 'date']  # Example allowed commands

    # Split the command into parts
    command_parts = shlex.split(command)

    # Check if the command is in the allowed list
    if command_parts[0] not in allowed_commands:
        return jsonify({'error': 'Command not allowed'}), 403

    try:
        # Execute the command safely
        result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return jsonify({'output': result.stdout}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e), 'output': e.output}), 500

if __name__ == "__main__":
    app.run(debug=True)