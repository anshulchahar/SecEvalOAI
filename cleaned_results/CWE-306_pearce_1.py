@app.route('/settings')
@ensure_logged_in
def settings():
    return '''
    <html>
    <h1>Settings Page</h1>
    <p>Welcome to the settings page, {username}!</p>
    </html>
    '''.format(username=session['username'])