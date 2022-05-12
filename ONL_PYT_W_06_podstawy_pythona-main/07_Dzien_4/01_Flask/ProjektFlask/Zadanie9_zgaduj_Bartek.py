from random import randint
from flask import Flask, request

app = Flask(__name__)

lucky_number = randint(1, 100)
print(lucky_number)

html_form = """
    <h3>Zgadnij liczbę między 1 a 100:</h3>
    <form method="POST">
        <p>Twój typ: <input type="number" name="players_choice"></p>
        <input type="submit" value="Zgadnij">
    </form>
    """

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return html_form
    else:
       # request.method == "POST"
        return handle_form()

def handle_form():
    try:
        players_choice = int(request.form["players_choice"])
    except (KeyError, ValueError):
        return "Niepoprawne dane"
    else:
        if players_choice == lucky_number:
            return "<h3>Gratulacje! Trafiłeś.</h3>"  
        elif players_choice < lucky_number:
            return "<h3>Za mała</h3>" + html_form
        elif players_choice > lucky_number:
            return "<h3>Za duża</h3>" + html_form

if __name__ == '__main__':
    app.run(debug=True)