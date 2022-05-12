# Napisz i uruchom prosty kalkulator, który:
#
#     wyświetli formatkę z dwoma polami na wprowadzenie liczb i listę wybieraną operacji (+, -, *, /)
#     po wciśnięciu guzika "wyślij" policzy wynik i wyświetli go na ekranie

from flask import Flask
from flask import  request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def kalkulator():

    if request.method == 'GET':
       return  ''' 
    <html> 
        <body>
            <form method = "POST">
            <input type="number" name = "liczba1">
            
            <select name="rodzaj">
		        <option  value = "mnozenie">*</option>
		        <option  value = "dzielenie">/</option>
		        <option  value = "dodawanie">+</option>
		        <option  value = "odejmowanie">-</option>
	        </select>
	        
            <input type="number" name = "liczba2">
            <input type = "submit">
            </form >
        </body>
    </html>
    '''
    else:
    #if request.method == 'POST':
        liczba1 = int(request.form["liczba1"])
        liczba2 = int(request.form["liczba2"])


        rodzaj = request.form["rodzaj"]
       # return f"Wynik: {liczba1}*{liczba2}"
        if rodzaj == "mnozenie":
           return f"Wynik: {liczba1 * liczba2}"
        elif rodzaj == "dzielenie":
           return f"Wynik: {liczba1 / liczba2}"
        elif rodzaj == "odejmowanie":
           return f"Wynik: {liczba1 - liczba2}"
        elif rodzaj == "dodawanie":
           return f"Wynik: {liczba1 + liczba2}"
        else:
           return f"Zly parametr matematyczny"

if __name__ == '__main__':
    app.run(debug=True, port="5002")



