# Napisz i uruchom prosty kalkulator, który:
#
#     wyświetli formatkę z dwoma polami na wprowadzenie liczb i listę wybieraną operacji (+, -, *, /)
#     po wciśnięciu guzika "wyślij" policzy wynik i wyświetli go na ekranie
import math
from flask import Flask
from flask import request


app = Flask(__name__)

html_form = ''' 
    <html> 
        <body>
            <form method = "POST">
            <h3>Podaj kod pocztowy </h3>
            
            Kod: <input type="code" name = "code" autofocus minlength="6" maxlength="6" placeholder="Podaj kod w postaci: 12-345" >
 
            <input type = "submit"  >
            </form >
        </body>
    </html>
    '''

@app.route('/', methods=["GET", "POST"])
def kalkulator():
    if request.method == 'GET':

        return html_form
    else:
        # if request.method == 'POST':
        code = request.form["code"]
        for i in range(1, 6, 2):
            if code[i].isdigit() and code[2] is "-":
                return f"""{html_form} \n \
               <p><b>KOD POPRAWNY</b> {code}\n</p>"""
            else:
                return f"""{html_form} \n \
               <p><b>KOD NIE POPRAWNY</b> {code}\n</p>"""

#pattern="[0-9]{2}-[0-9]{3}" # wyrazenie regularne



if __name__ == '__main__':
    app.run(debug=True, port="5002")



