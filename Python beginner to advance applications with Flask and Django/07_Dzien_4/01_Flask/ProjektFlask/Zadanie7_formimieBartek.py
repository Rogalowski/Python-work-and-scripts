from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/formularz", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        # return html_form()
        return render_template("form.html")
    elif request.method == "POST":
        return handle_form()

# def html_form():
#     with open("templates/form.html") as file:
#         return file.read()

# @app.route("/formularz", methods=["GET", "POST"])
# def form():
#     if request.method == "GET":
#         return html_form()
#     elif request.method == "POST":
#         return handle_form()
#
#
# def html_form():
#     return """\
#     <form method="POST">
#         <p>
#             Imię: <input type="text" name="first_name">
#         </p>
#         <input type="submit" value="Wyślij">
#     </form>
#     """

def handle_form():
    first_name = request.form["first_name"]
    return f"Witaj, {first_name}"

# @app.route("/show_form")
# def show_form():
#     return """\
# <form action="/handle_form" method="POST">
#     <p>
#         Imię: <input type="text" name="first_name">
#     </p>
#     <input type="submit" value="Wyślij">
# </form>
# """
#
#
# @app.route("/handle_form", methods=["POST"])
# def handle_form():
#     first_name = request.form["first_name"]
#     return f"Witaj, {first_name}"

if __name__ == '__main__':
    app.run(debug=True)