# Napisz i uruchom prostą zgadywankę, która:
#
#     wylosuje poprawną odpowiedź,
#     zapyta użytkownika - "Spróbuj zgadnąć liczbę", wyświetlając formularz
#     po wysłaniu formularza z odpowiedzią, wypisze na ekranie:
#         "za mało!" jeżeli odpowiedź użytkownika jest mniejsza niż liczba i formatkę jeszcze raz,
#         "za dużo!" jeżeli odpowiedź użytkownika jest większa niż liczba i formatkę jeszcze raz,
#         "Gratulacje, udało Ci się!" jeżeli użytkownik trafi.
#
# Wstępna informacja do następnych zadań
#
# https://www.garron.me/en/bits/curl-delete-request.html
#
# http://superuser.com/questions/149329/what-is-the-curl-command-line-syntax-to-do-a-post-request
from flask import Flask, request
import random

app = Flask(__name__)

liczba_losowa = random.randint(10, 56)
@app.route('/', methods=["GET", "POST"])
def zgadywanka():
    if request.method == 'GET':
        return ''' 
    <html> 
        <body>
            <form method = "POST">
            <input type="number"  name = "liczba_wprowadzona" >

            <input type = "submit">
            </form >
        </body>
    </html>
    '''


    #if request.method == 'POST':
    else:
        liczba_wprowadzona = int(request.form["liczba_wprowadzona"])
        if liczba_wprowadzona == liczba_losowa:
            return f"TRAFILES Wylosowana liczba: {liczba_losowa} Wprowadzona: {liczba_wprowadzona}"
        elif liczba_wprowadzona < liczba_losowa:
            return f"NIETRAFILES ZA MALO, Wylosowana liczba: {liczba_losowa} Wprowadzona: {liczba_wprowadzona}"
        elif liczba_wprowadzona > liczba_losowa:
            return f"NIETRAFILES ZA DUZO, Wylosowana liczba: {liczba_losowa} Wprowadzona: {liczba_wprowadzona}"
        #liczba1 = int(liczba1)


    # else:
    #     return f"To nie ta liczba {liczba_wprowadzona}"





if __name__ == '__main__':
    app.run(debug=True, port=5002)