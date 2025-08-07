from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def redirect_user():
    '''
    Redirect the user to the next_url specified in the GET request.
    '''
    next_url = request.args.get('next_url')
    if next_url:
        return redirect(next_url)
    else:
        return "No URL provided for redirection", 400

if __name__ == '__main__':
    app.run(debug=True)