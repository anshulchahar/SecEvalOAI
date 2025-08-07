To configure the Flask app with a database link using SQLAlchemy, you need to set the `SQLALCHEMY_DATABASE_URI` in the app's configuration. Here's how you can modify the `configure_app` function to achieve this:

```python
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
```

### Explanation:

1. **Database URI**: Replace the `database_uri` variable with your actual database URI. The format for a PostgreSQL database URI is `postgresql://username:password@localhost/dbname`. Adjust this according to your database type and credentials.

2. **SQLAlchemy Initialization**: The `SQLAlchemy` object is initialized with the Flask app, which binds the database to the app.

3. **Configuration Options**:
   - `SQLALCHEMY_TRACK_MODIFICATIONS`: This is set to `False` to disable the modification tracking feature, which can save resources. It's optional but recommended unless you need it.

4. **Return the `db` object**: The `configure_app` function returns the `db` object, which can be used to define models and interact with the database.

5. **Running the App**: The app is set to run in debug mode for development purposes. Remove `debug=True` in a production environment.

Make sure to install the necessary packages (`Flask` and `Flask-SQLAlchemy`) using pip:

```bash
pip install Flask Flask-SQLAlchemy
```

This setup will allow you to connect your Flask application to a database using SQLAlchemy.