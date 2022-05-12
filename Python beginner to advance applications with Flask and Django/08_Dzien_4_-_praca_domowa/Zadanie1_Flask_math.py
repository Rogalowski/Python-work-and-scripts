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
            <p>Podaj Liczbę n, która obliczy poniżej: </p>
            Liczba n: <input type="number" name = "n">



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
        n = int(request.form["n"])

        potega2 = 2**n
        potegan = n**n
        silnian = math.factorial(n)

        return f"""{html_form} \n \
              Potęga 2 ** n = {potega2} \
              <p> Potega n ** n = {potegan}\n </p>\
               <p>Silnia n =      {silnian}\n</p>"""


if __name__ == '__main__':
    app.run(debug=True, port="5002")



