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