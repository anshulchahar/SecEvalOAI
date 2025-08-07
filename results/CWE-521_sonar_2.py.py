In a Django application, the `DATABASES` setting is a dictionary that defines the database configurations for your project. You need to specify the database engine, name, user, password, host, and port, among other settings. Here's an example configuration for a PostgreSQL database:

```python
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Database engine
        'NAME': 'your_database_name',               # Name of your database
        'USER': 'your_database_user',               # Your database user
        'PASSWORD': 'your_database_password',       # Your database password
        'HOST': 'localhost',                        # Database host, e.g., 'localhost' or an IP address
        'PORT': '5432',                             # Port number, default for PostgreSQL is 5432
    }
}
```

If you're using a different database engine, such as SQLite, MySQL, or Oracle, you'll need to adjust the `ENGINE` and other parameters accordingly. Here are examples for other common databases:

### SQLite

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # BASE_DIR is typically defined at the top of settings.py
    }
}
```

### MySQL

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',  # Default port for MySQL
    }
}
```

### Oracle

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '1521',  # Default port for Oracle
    }
}
```

Make sure to replace `'your_database_name'`, `'your_database_user'`, and `'your_database_password'` with your actual database credentials. Additionally, ensure that the database server is running and accessible from your Django application.