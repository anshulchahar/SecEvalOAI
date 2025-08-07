@app.route('/register', methods=['POST'])
def register():
    # Get username and password from the request
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return "Username and password are required", 400

    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Connect to the database
    db = MySQLdb.connect(host="localhost", user="yourusername", passwd="yourpassword", db="yourdatabase")
    cursor = db.cursor()

    try:
        # Check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            return "Username already exists", 409

        # Insert the new user into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        db.commit()

        return "User registered successfully", 201

    except MySQLdb.Error as e:
        db.rollback()
        return f"An error occurred: {e}", 500

    finally:
        cursor.close()
        db.close()