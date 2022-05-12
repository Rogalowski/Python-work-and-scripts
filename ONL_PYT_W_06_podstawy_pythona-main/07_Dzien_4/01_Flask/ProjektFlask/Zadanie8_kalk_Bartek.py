
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return html_form()
    elif request.method == "POST":
        return handle_form()

def html_form():
    return """\
    <form method="POST">
        <p>Liczba 1: <input type="number" name="a"></p>
        <p>Liczba 2: <input type="number" name="b"></p>
        <p>
            Działanie:
            <select name="operation">
                <option value="add">+</option>
                <option value="subtract">-</option>
                <option value="multiply">*</option>
                <option value="divide">/</option>
            </select>
        </p>
        <input type="submit" value="Wyślij">
    </form>
    """

def handle_form():
    try:
        a = int(request.form["a"])
        b = int(request.form["b"])
        operation = request.form["operation"]

        operations = {
            "add": lambda a, b: a + b,
            "subtract": lambda a, b: a - b,
            "multiply": lambda a, b: a * b,
            "divide": lambda a, b: a / b,
        }

        function = operations[operation]

    except (KeyError, ValueError):
        return "Błędne dane wejściowe"
    else:
        return str(function(a, b))

        # if operation == "add":
        #     return str(a + b)
        # elif operation == "subtract":
        #     return str(a - b)
        # elif operation == "multiply":
        #     return str(a * b)
        # elif operation == "divide":
        #     return str(a / b)
        # else:
        #     return f"Nieznana operacja: {operation}"

if __name__ == '__main__':
    app.run(debug=True)