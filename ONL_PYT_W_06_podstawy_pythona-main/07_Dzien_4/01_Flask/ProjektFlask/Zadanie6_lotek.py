# from flask import Flask
# import random
#
# app = Flask(__name__)
#
#
# @app.route('/', methods=["GET"])
# def hello():
#     dystrybutor = []
#     for i in range(0, 49):
#         dystrybutor.append(i)
#         #print("xx", dystrybutor[22])
# # return f"{dystrybutor[0:5]}"
#     wylosowany = [5, 5]
#     for i in range(0, 5):
#         #if wylosowany != wylosowany:
#            wylosowany = random.choice(dystrybutor[0:49])
#            # print(f"{wylosowany}")
#     return f"{wylosowany[:3]}"

# if __name__ == '__main__':
#     app.run(debug=True, port=5002)


import random
from flask import Flask

app = Flask(__name__)


@app.route("/lotek")
def home():
    random_numbers = random.sample(range(1, 50), 6)
    return ", ".join([str(x) for x in random_numbers])


# numbers = list(range(1, 50))
# random.shuffle(numbers)
# return ", ".join([str(x) for x in numbers[:6]])

# random_numbers = []
# while len(random_numbers) < 6:
#     draw = random.randint(1, 49)
#     if draw in random_numbers:
#         continue
#     random_numbers.append(draw)
# return ", ".join([str(x) for x in random_numbers])

if __name__ == '__main__':
    app.run(debug=True)
