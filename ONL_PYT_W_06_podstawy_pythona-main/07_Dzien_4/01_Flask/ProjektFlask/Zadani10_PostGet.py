from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return "Wysłałeś żądanie metodą GET"
    elif request.method == "POST":
        return "Wysłałeś żądanie metodą POST"
    else:
        return f"Wysłałeś żądanie metodą: {request.method}"

if __name__ == '__main__':
    app.run(debug=True)