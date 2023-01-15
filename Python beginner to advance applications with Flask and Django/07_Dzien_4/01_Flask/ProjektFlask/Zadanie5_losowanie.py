# from flask import Flask
# import random
#
# app = Flask(__name__)
#
#
# @app.route('/', methods=["GET"])
# def hello():
#     liczba1 = random.randint(1, 10)
#     liczba2 = random.randint(1, 10)
#     liczba3 = random.randint(1, 10)
#     return f"{liczba1, liczba2, liczba3}"
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True, port=5002)


from random import randint
from flask import Flask

app = Flask(__name__)

@app.route("/losuj")
def home():
    digits = [str(randint(0, 9)) for _ in range(3)]
    return ", ".join(digits)

if __name__ == '__main__':
    app.run(debug=True)