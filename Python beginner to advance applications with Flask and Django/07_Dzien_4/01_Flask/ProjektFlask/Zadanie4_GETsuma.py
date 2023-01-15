from flask import Flask

app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello():
    liczba1 = 2
    liczba2 = 2
    licz = liczba1 + liczba2
    return f"{licz}"



if __name__ == '__main__':
    app.run(debug=True, port=5002)


# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/licz/<int:a>/<int:b>")
# def home(a, b):
#     # total = int(a) + int(b)
#     total = a + b
#     # return str(total)
#     return f"{total}"
#
# if __name__ == '__main__':
#     app.run(debug=True)