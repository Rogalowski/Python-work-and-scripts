from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Cześć Jacek!'

@app.route('/about')
def about():
    return 'Strona about!'


if __name__ == '__main__':
    app.run(host="localhost", port=5001)
