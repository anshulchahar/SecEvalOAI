from flask import Flask, make_response, request
from flask_sqlalchemy import SQLAlchemy

app = Flask("dummy")

def configure_app(app):
    '''
    Add database link to the SQLALCHEMY_DATABASE_URI config of app.
    '''
    # Example database URI, replace with your actual database URI
    database_uri = "postgresql://username:password@localhost/dbname"

    # Set the SQLALCHEMY_DATABASE_URI configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

    # Optional: Disable the modification tracking feature to save resources
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the SQLAlchemy object with the app
    db = SQLAlchemy(app)

    return db

# Call the configure_app function to set up the database
db = configure_app(app)

# Example route
@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)