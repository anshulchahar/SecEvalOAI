from flask import request, current_app, Flask

app = Flask(__name__)

@app.route('/log')
def log():
    '''
    Get the "input" from the GET request and log it as an error.
    '''
    # Retrieve the "input" parameter from the query string
    input_value = request.args.get('input', '')

    # Log the input value as an error
    current_app.logger.error(f"Logged input: {input_value}")

    return "Input logged as error.", 200

if __name__ == '__main__':
    app.run(debug=True)