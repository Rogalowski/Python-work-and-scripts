from flask import Flask, request

app = Flask(__name__)
form_html = """\
    <form action="#" method="POST">
        <p>Imię: <input type="text" name="first_name"></p>
        <p>Nazwisko: <input type="text" name="last_name"></p>
        <input type="submit" value="Wyślij">
    </form>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return form_html
    else:
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        return f"Witaj {first_name} {last_name}"

if __name__ == '__main__':
    app.run(debug=True)