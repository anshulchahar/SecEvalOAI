from flask import Flask

app = Flask(__name__)

@app.route('/crash')
def main():
    raise Exception()

if __name__ == '__main__':
    app.run(debug=True)