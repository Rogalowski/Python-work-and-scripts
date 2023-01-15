## Zadanie 3
Przy użyciu biblioteki **requests**, napisz prosty program, który połączy się z dowolną stroną i ściągnie HTML 
strony głównej.

**Podpowiedź:** zajrzyj do http://docs.python-requests.org/en/master/


import requests

r = requests.get('https://www.x-kom.pl')

#print(r.content)
#print(r.status_code)
print(r.text)




DEKORATORYDEKORATORYDEKORATORYDEKORATORYDEKORATORYDEKORATORYDEKORATORYDEKORATORYDEKORATORYDEKORATORYDEKORATORYDEKORATORYDEKORATORYDEKORATORYDEKORATORYDEKORATORYDEKORATORY

#https://docs.python.org/3/library/doctest.html

import time
def timed(function):
    def wrapper(a, b):
        t1 = time.time()
        result = function(a, b)
        t2 = time.time()
        print("Funkcja wykonywała się przez", t2 - t1)
        return result
    return wrapper
# Dekoratory wbudowane w Pythona:
# @property
# @classmethod
# @staticmethod
# Własny dekorator, krtóry sam zdefiniowałem:
# @timed
@timed
def div(a, b):
    return a / b
@timed
def add(a, b):
    return a + b
# div = timed(div)
# add = timed(add)
print(div(3, 4))
print(add(3, 4))


#https://docs.python.org/3/library/doctest.html

def upper(function):
    def wrapper(arg):
        result = function(arg)
        return result.upper()
    return wrapper
@upper
def greet(name):
    return f"Hello, {name}"
print(greet("Bartek"))







AKTUALNY CZAS

from datetime import datetime
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    now = format(datetime.now().time(), "%H:%M:%S")
    return f"Teraz jest godzina {now}"
if __name__ == '__main__':
    app.run(debug=True)


DATA DATA

from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    today = format(datetime.today(), "%Y-%m-%d")
    return f"Dziaj jest {today}"

if __name__ == '__main__':
    app.run(debug=True)









DODANIE IMIENiA  I NAZWISKA TEMPLATE:



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



#TEMPLATKA form.html def html_form():#     with open("templates/form.html") as file:  return file.read()
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Formularz</title>
</head>
<body>
  <form method="POST">
    <p>Imię: <input type="text" name="first_name"></p>
    <input type="submit" value="Wyślij">
  </form>
</body>
</html>




LOTEKLOTEKLOTEKLOTEKLOTEKLOTEKLOTEKLOTEKLOTEKLOTEKLOTEKLOTEKLOTEKLOTEKLOTEKLOTEKLOTEKLOTEKLOTEKLOTEKLOTEK

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








## Zadanie 2

Napisz aplikację Flaska, która poprosi użytkownika o wpisanie kodu pocztowego (na akcji GET "/"), 
a potem (na akcji POST "/") wyświetli informację:

* `Kod poprawny`, jeżeli kod jest w poprawnym polskim formacie (00-001).
* `Kod niepoprawny`, w przeciwnym wypadku

Kod wysyłaj jako parametr `code`.

**Wskazówka: możesz rozbić podany ciąg znaków po myślniku i sprawdzić czy obie części spełniają warunki.**

**Wskazówka: Pamiętaj o wyświetleniu guzika do wysłania formularza!**


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







#ZADANIE6
2001
Warsztat: Salon gier (*)

Zaimplementuj grę 2001. Poniżej znajdziesz zasady.
2001 – Zasady Gry

    Każdy z graczy zaczyna z liczbą punktów równą 0.
    W swojej turze, gracz rzuca 2 kośćmi do gry (standardowe kości sześciościenne).
    Wyrzucona liczba oczek jest dodawana do sumarycznej liczby punktów.
    Począwszy od drugiej tury:
        jeśli gracz wyrzuci 7, dzieli swoją liczbę punktów przez tę wartość odrzucając część ułamkową,
        jeśli wyrzuci 11, mnoży aktualną liczbę punktów przez tę wartość.
    Wygrywa gracz, który jako pierwszy uzyska 2001 punktów.

Implementacja

    Zaimplementuj grę w wersji dla dwóch graczy.
    Niech będzie to aplikacja konsolowa.
    Niech drugim graczem będzie komputer.
    Po każdej turze wyświetl aktualną liczbę punktów.
    Rzut gracza, powinien odbywać się po naciśnięciu przez użytkownika klawisza enter. Rzut komputera następuje automatycznie, po rzucie gracza. Zakończ program w momencie, gdy gracz, lub komputer osiągnie więcej niż 2001 punktów.

Modyfikacja 1

Zauważyłeś pewno, że gra w obecnej wersji jest mało interaktywna i sprowadza się tylko i wyłącznie, do klikania klawisza enter. Spróbujmy uczynić ją trochę bardziej interaktywną.

    Przed każdym rzutem, daj graczowi wybór.
    Niech wybierze 2 kości z zestawu: D3, D4, D6, D8, D10, D12, D20, D100.
    Kości mogą się powtarzać, gracz może też użyć 2 różnych kości.
    Niech wybór kości odbywa się za pomocą wprowadzenia odpowiedniego łańcucha znaków przez gracza (po jednym na każdą z kości).
    Możesz wykorzystać kod z zadania Kostka do gry.
    Wybór kości przez komputer niech będzie losowy.

Reszta zasad pozostaje bez zmian.
Modyfikacja 2

Spróbuj teraz przenieść swoją grę na serwer przy użyciu Flaska. Aby przechowywać informację między turami, wykorzystaj ukryte pola formularza. Nie jest to najlepsze rozwiązanie (może być podatne na oszukiwanie), ale na tę chwilę się tym nie przejmujemy. Wybór kości przed rzutem, powinien odbywać się za pomocą formularza.




from flask import Flask, request

app = Flask(__name__)

html_start = """
    <!DOCTYPE html>
    <html lang="en"> 

    <head>
    <meta charset="UTF-8">
    <title>Guess The Number</title>
    </head>

        <body>
        <h3>Lets Start The Game</h3>
        
            <form  action = "" method = "POST">
            Mini: <input type="text" name="min" value="{}"><br>
            Maxi: <input type="hidden" name = "max" value="{}"> <br>
            Counter: <input type="text" name = "counter" value="{}"> <br>
            <input type="submit" value="OK">
            </form >
            
        </body>
    </html>
    """

HTML_GAME = """
    <!DOCTYPE html>
    <html lang="en"> 

    <head>
    <meta charset="UTF-8">
    <title>Guess The Number</title>
    </head>

        <body>
            <p> Here: {guess} </p>
            <h3>GAME to guess Imagine number 1 - 1000 </h3>
            <p> Turn number: {counter}</p>
            <form  action = "" method = "POST">
            Mini: <input type="text"  name = "min" value="{min}"> <br>
            Maxi: <input type="text"  name = "max" value="{max}"> <br>
            Guess:<input type="text" name = "guess" value="{guess}"> <br>
            Counter: <input type="text" name = "counter" value="{counter}"> <br>

            <br>

            <input type="submit" name="answer" value="Too Big">
            <input type="submit" name="answer" value="Too Small">
            <input type="submit" name="answer" value="Correct">
            </form >
        </body>
    </html>
    """
html_win = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess The Number</title>
  
</head>
<body>
<h1>Hurra! I guess! Your number is {guess} in {counter} turns!</h1>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "GET":
        return html_start.format(0, 1000, 1)  # STAN POCZATKOWY

    if request.method == "POST":

        mini = int(request.form.get("min"))
        maxi = int(request.form.get("max"))
        guess = int(request.form.get("guess", 500))

        counter = int(request.form.get("counter", 1))
        answer = request.form.get("answer")



        if answer == "Too Big":
            maxi = guess
            counter += 1

        elif answer == "Too Small":
            mini = guess
            counter += 1
        elif answer == "Correct":
            return html_win.format(guess=guess, counter=counter)


        guess = (maxi - mini) // 2 + mini
        return HTML_GAME.format(guess=guess, min=mini, max=maxi, counter=counter)


if __name__ == '__main__':
    app.run()













FLASK I BAZY DANYCH  
FLASK I BAZY DANYCH
FLASK I BAZY DANYCH
FLASK I BAZY DANYCH  
FLASK I BAZY DANYCH
FLASK I BAZY DANYCH









## Zadanie 1 &ndash; zadania rozwiązywane z wykładowcą

Napisz funkcję `execute_sql` uruchamiającą dowolny kod sql. Funkcja powinna przyjąć dwa parametry:
* nazwę bazy danych.
* zapytanie SQL.

Funkcja powinna wykonać podany w parametrze kod sql na podanej bazie.
Funkcja powinna zwrócić listę wyników (w przypadku zapytań typu **SELECT**), lub `None`.

Rozwiązanie umieść w pliku **sql_utils.py**.
import psycopg2
from psycopg2.extras import RealDictCursor


USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"
PORT = 5431

def execute_sql(sql_code, db):
    """
    Run given sql code with psycopg2.

    :param str sql_code: sql code to run
    :param str db: name of db,

    :rtype: list
    :return: data from psycobg2 cursor as a list (can be None) if nothing to fetch.
    """
    conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=db)
    conn.autocommit = True
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(sql_code)
            for row in cursor:
                print(row)
    finally:
        conn.close()


execute_sql("""
SELECT cinemas.name AS cinema, movies.name AS title, address, datetime, rating  FROM cinemas
INNER JOIN screening ON cinemas.id=screening.cinema_id
INNER JOIN movies ON movies.id=screening.movie_id;
""", "cinemas_db")




## Zadanie 2 &ndash; zadania rozwiązywane z wykładowcą

Używając Flaska, napisz program, który wyświetli na stronie wszystkie produkty znajdujące się w bazie danych o nazwie
 `exercises_db`.

**Podpowiedź:** Program powinien uruchamiać zapytanie SQL, które wyciągnie wszystkie wpisy z odpowiedniej tabeli,
po czym wyświetli je na ekranie. Możesz wykorzystać kod napisany w poprzednim zadaniu.

Rozwiązanie umieść w pliku **sql_utils.py**.





import flask
import psycopg2


USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"
PORT = 5431

def execute_sql(sql_code, db):
    result = []
    conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=db)
    conn.autocommit = True
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql_code)

            for row in cursor:
                result.append(str(row))
    finally:
        conn.close()

    return result


app = flask.Flask(__name__)


@app.route("/")
def list_products():
    result = execute_sql("""SELECT * FROM movies""", "cinemas_db")
    return "<br>\n".join(result)

app.run(port=8080)




## Zadanie 3

1. W pliku **form.html** jest formularz służący do tworzenia nowych wpisów w tablicach.
Przeanalizuj HTML i użyj tego kodu w dalszej części zadania.
2. Używając Flaska napisz program, który:
  * po wejściu metodą **GET** wyświetli formularz zawierający następujące pola:
    * `name` - nazwa filmu,
    * `description` - opis filmu,
    * `rating` - ocena filmu,
  * po wejściu metodą **POST** sprawdzi, czy formularz został wypełniony poprawnie:
    * jeśli tak, to zapisze film do bazy danych,
    * jeśli nie, zwróci odpowiedni komunikat.

Program udostępnij pod adresem `add_movie`.  
Możesz wykorzystać fukcje utworzone w poprzednich zadaniach.


## Zadanie 4

Używając Flaska, napisz stronę, która:
* będzie dostępna pod adresem `movies`,
* pobierze z bazy danych wszystkie filmy
* wyświetli je na stronie w formie listy.    


## Zadanie 5 (*)

Używając Flaska, napisz stronę, która:
* będzie dostępna pod adresem `movie/<movie_id>`, gdzie `movie_id`, to liczba określająca **id** filmu,
* pobierze z bazy informacje na temat filmu o podanym ID,
* wyświetli je na stronie.    

## Zadanie 6 (*)

Używając Flaska, napisz stronę, która usunie wybrany film o podanym **id**. Id powinno być przekazane w adresie strony.
Strona powinna wyświetać informacje o usunięciu wpisu z tabeli.


## Zadanie 7 (*)

Używając Flaska, napisz stronę, do której przekażesz id filmu metodą GET. Strona powinna:

- wyciągnąć dane filmu z bazy danych; w razie podania błędnego identyfikatora filmu,
powinna wyświetlić komunikat „nie ma takiego filmu.”
- wyświetlić formularz, w którym będą następujące pola:
  - id filmu (pole ukryte, niemożliwe do edycji),
  - tytuł filmu,
  - opis filmu.

Każde z tych pól, pownno być wypełnione danymi wyciągnietymi z bazy danych.

Po wysłaniu formularza (metodą POST), program powinien:

- wyciagnąć dane filmu z bazy danych,
- wygenerować odpowiednie zapytanie, które **zmieni** dane filmu w bazie,
- wykonać to zapytanie,
- gdy wszystko zakończy się poprawnie, wyświetlić komunikat „zmieniono dane filmu”,
- w przypadku błędu, wyświetlić komunikat „ups... coś poszło źle!”.


Najpierw przetestuj zapytania SQL w konsoli lub panelu administracyjnym,
dopiero potem napisz kod Pythona.

**Uwaga: Jeśli w poleceniu widnieje „napisz stronę”, oznacza to, że należy
napisać program w Pythonie, używając Flaska, który będzie się komunikował z
użytkownikiem za pomocą stron WWW i protokołu HTTP.**



import flask
from flask import request, render_template
import psycopg2
from markupsafe import escape


USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"
PORT = 5431
DB = "cinemas_db"

SQL_INSERT_MOVIE = """INSERT INTO movies (name, description, rating) VALUES (%s, %s, %s);"""
SQL_SELECT_MOVIES = """SELECT * FROM movies;"""
SQL_SELECT_MOVIE = """SELECT * FROM movies WHERE id = %s or id = %s;""" #or id=%s
#SQL_SELECT_MOVIES = """SELECT * FROM movies ORDER BY rating DESC, name ASC;"""


def add_movies_database(name, desc, rating):
    conn = psycopg2.connect(user=USER, password=PASSWORD, port=PORT, host=HOST, database=DB)
    #conn.autocommit = True
    try:
        with conn.cursor() as cursor:
            cursor.execute(SQL_INSERT_MOVIE, (name, desc, rating))
        conn.commit()


    finally:
        conn.close()
        print("Bye")

def view_movies_from_database():
    conn = psycopg2.connect(user=USER, password=PASSWORD, port=PORT, host=HOST, database=DB)
    conn.autocommit = True
    try:
        with conn.cursor() as cursor:

            cursor.execute(SQL_SELECT_MOVIES)

            result = []

            for row in cursor:
                #print(str(row))
                result.append(str(row))
            return "<h3>AKTUALNA BIBLIOTEKA FILMOW: </h3>" + "<br>\n".join(result)
    finally:
        conn.close()


def view_movie_id(id):
    conn = psycopg2.connect(user=USER, password=PASSWORD, port=PORT, host=HOST, database=DB)
    conn.autocommit = True
    try:
        with conn.cursor() as cursor:

#FIRST METHOD TO GET MOVIE ID
            #cursor.execute("SELECT * FROM movies WHERE id = '"+ str(id) +"'  or id = '" + str(id) +"';") # PODATNY NA SQL INJECTION
            cursor.execute("SELECT * FROM movies WHERE id = %s  or id = %s;", (id, id)) #SQL PREVENT id OR id INJECTION
            #cursor.execute(SQL_SELECT_MOVIES)

            result = []
            for row in cursor:
                print(row[0])
                result.append(str(row))
                return f"<h3>Film o id  {id}: </h3>" + "<br>\n".join(result)

# SECOND METHOD TO GET MOVIE ID
                #if row[0] == id:
                #    result.append(str(row))
                #    return f"<h3>Film o id  {id}: </h3>" + "<br>\n".join(result)





                #break


    finally:
        conn.close()


app = flask.Flask(__name__)



@app.route("/add_movie", methods=["GET", "POST"])
def movies():
    if request.method == 'GET':
        return view_movies_from_database() + "<h3>DODAJ NOWY FILM DO BIBLIOTEKI</h3>" + render_template("form.html")

    if request.method == 'POST':
        name = str(request.form["name"])
        desc = str(request.form["desc"])
        rating = int(request.form["rating"])

        print(request.form)
        add_movies_database(request.form['name'], request.form['desc'], request.form['rating'])
        return f"""
        DODANO DO BAZY DANYCH: <br> 
        Nazwa Filmu: {name} <br>
        Opis: {desc} <br>
        Ocena: {rating}
        """ + render_template("form.html") + view_movies_from_database()

@app.route("/movies", methods=["GET", "POST"])
def view_movies():
    if request.method == 'GET':
        return view_movies_from_database()

@app.route("/movie/<int:id>", methods=["GET", "POST"])
def view_movie_from_id(id):
    page_id = id
    return f'{view_movie_id(page_id)}'



if __name__ == '__main__':
    app.run(debug=True, port="5002")








 

# Python i bazy danych &ndash; praca domowa &ndash; Dzień 2

Połącz tabele relacjami:
1. autorów i książki (relacja jeden do wielu); dla uproszczenia przyjmij, że książka może mieć tylko jednego autora;
wystarczy, że przeedytujesz odpowiednie tabele,
2. książki i kategorie (relacja wiele do wielu); jedna ksiązka może mieć wiele kategorii, jedna kategoria może należeć
do wielu ksiązek; dodaj odpowiednią tabelę pośrednią,
3. klientów i książki (relacja wiele do wielu); W tabeli pośredniej, dodaj pola:
    * loan_date: date (data wypożyczenia)
    * return_date: date (data zwrotu, domyślnie Null)


Używając **Flaska** Napisz aplikację, do zarządzania naszą biblioteką. W aplikacji powinny być następujące strony:
1. `books` - lista wszystkich książek,
2. `add_book` - strona, która:
    * po wejściu metodą **GET** wyświetli formularz dodania książki, 
    * po wejściu metodą **POST** doda książkę do bazy danych,
3. `book_details/<id>` - strona wyświetlająca szczegółowe dane książki,       
4. `delete_book/<id>` - strona umożliwiająca usunięcie książki o podanym id  
5. `clients` - lista wszystkich klientów,
6. `add_client` - strona, która:
    * po wejściu metodą **GET** wyświetli formularz dodania klienta, 
    * po wejściu metodą **POST** doda klienta do bazy danych,  
7. `delete_client/<id>` - strona umożliwiająca usunięcie klienta o podanym id
8. `client_details/<id>` - strona wyświetlająca szczegółowe dane klienta, 
w tym wszystkie wypożyczone przez niego ksiązki
9. loan - strona umożliwiająca wypożyczenie książki:
  * po wejściu metodą **GET** powinna wyświetlić formularz z listą klientów i ksiązek
  * po wejściu metodą **POST** powinna dodać wypożyczenie do bazy danych      


(*) Aplikacje możesz rozwinąć według własnego uznania dodając inne przydatne funkcjonalności. np.:
    * zarządzanie kategoriami,
    * stronę zwrotu książki,
    * blokadę wypożyczeń (mechanizm pozwalający wypożyczyc tylko jedną książkę przez jednego klienta w danym czasie)
    * możliwość oceniania książek,
    * możliwość komentowania książek.
    
----

### Zadanie: poćwicz SQL (*)

W repozytorium z zadaniami domowymi znajdziesz zrzut bazy danych **football.sql**. 
Jest to baza danych z wynikami Ligi Okręgowej Warszawa II w sezonie 2016/17 (wyniki na dzień 14 listopada 2016 roku).

Utwórz na serwerze bazę danych i zaimportuj plik SQL. Jeśli nie wiesz, jak to zrobić, poszukaj w Google,
używając słów kluczowych: *PostgreSQL, import, dump*.

Przyjrzyj się strukturze i danym. Znajdują się tam dwie tabele: **Teams** i **Games**. 
Pierwsza z nich to lista klubów piłkarskich i punkty zdobyte do dnia eksportu bazy danych. 
Druga tabela to wyniki gier. Pola `team_home` i `team_away` to klucze obce do tabeli **Teams**

Napisz zapytania, które:

1. Wyciągną klub, który jest liderem tabeli,
2. Wyciągną tabelę, posortowaną według liczby zdobytych punktów,
3. Wyciągną wszystkie mecze, które Naprzód Brwinów grał u siebie,
4. Wyciągną wszystkie mecze, które Naprzód Brwinów grał na wyjeździe,
5. Wyciągną wszystkie mecze (u siebie i na wyjeździe) klubu Naprzód Brwinów. 
6. Zsumują wszystkie gole zdobyte przez klub Naprzód Brwinów u siebie i na wyjeździe 
(zrób dwa zapytania: osobno u siebie, osobno na wyjeździe).

W podpunktach 3 - 5 wynik ma zawierać kolejno: 

* nazwę klubu gospodarzy,
* nazwę klubu gości,
* liczbę goli strzelonych przez gospodarzy,
* liczbę goli strzelonych przez gości.  