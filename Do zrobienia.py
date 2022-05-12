 
# Zadanie 1
#
# Napisz obiektowo program, który będzie obsługiwał skanowanie produktów w sklepie.
#
# Stwórz klasę Product. Klasa ta ma posiadać podane atrybuty:
#
#     _id – numer identyfikacyjny produktu; zazwyczaj tego typu atrybuty powinny być nadawane automatycznie i to klasa powinna dbać o unikalność tej danej, ale o tym, jak zapewnić tutaj spójność, dowiemy się w dalszej części tego modułu,
#     name – string. Jest to nazwa danego produktu,
#     description – string. Jest to opis danego produktu,
#     price – float. Jest to cena za jeden produkt. Powinna być większa od 0.01,
#     quantity – liczba całkowita większa od zera.
#
# Klasa powinna mieć też nastepujące metody:
#
#     __init__ - powinien przyjmować nazwę, opis, cenę i ilość produtku.
#     atrybut id powiniem mieć możliwość wyłącznie odczytu (najlepiej użyć do tego @property).
#     metodę get_total_sum() która będzie zwracała łączną kwotę za dany produkt (wyliczaną jako ilość * cena produktu.
#
# Generowanie unikalnego id dla produktu:
# Uwaga! Aby zrozumieć dalszą część zadania, zajrzyj do jutrzejszych prezentacji.
#
# W dalszej części programu będziemy chcieli identyfikować nasze produkty po ich id. Dlatego musimy zagwarantować że każdy z stworzonych produktów będzie miał unikalny numer identyfikacyjny. W tym celu w klasie Product powinniśmy zdefiniować dodatkowy atrybutnext_id.
#
# Utwórz kilka produktów, dbając o to, by nie nadawać tego samego id kolejnym obiektom.
#
# Zmienna ta będzie trzymała id ktore zostanie nadane następnemu stworzonemu produktowi. Nastepnie w metodzie __init__ musimy wykonać następujące czynności:
#
#     własnie tworzonemu produktowi przypisać id trzymane w zmiennej next_id,
#     zwiększyć wartość next_id o jeden.
#
# # w __init__
#
# self.id = self.next_id
#
# Product.next_id += 1
#
# Dzieki temu żaden z naszych produktów nie będzie miał takiego samego id.
#
# Dla chętnych: Bardziej eleganckim rozwiązaniem, będzie użycie licznika z itertools, lub wbudowanej funkcji id(). Więcej na ten temat możesz przeczytać w tym wątku na stack overflow: https://stackoverflow.com/questions/1045344/how-do-you-create-an-incremental-id-in-a-python-class
#

class Product:
    def __init__(self, id, name, description, price, quantity):
        self._id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @property
    def id(self):
        return self._id

    def get_total_sum(self):
        return self.quantity * self.price
        
        
        
        
        
        
        
        
        
        
        
        
ZAdanie 5 exam


## Zadanie 5. (5pkt)

Napisz w Pythonie klasę `EBook`. Klasa powinna spełniać następujące właściwości:
1. Dziedziczyć po klasie `Book` (zajrzyj do modułu `exam_lib`).
2. Mieć dodatkowe atrybuty: `size` (rozmiar w MB) i `registration_code` (kod do rejestracji).
    Kod rejestracyjny nie powinien być dostępny na zewnątrz (pamiętaj o konwencji nazw).
3. Mieć metodę `__init__`, która przyjmuje następujące dane: tytuł, autor, liczba stron, rozmiar i kod rejestracyjny.
    Tytuł, autor i liczba stron mają być przekazywane do metody `__init__` klasy nadrzędnej.
    Metoda `__init__` ma sprawdzać, czy podany kod rejestracyjny jest prawidłowy. Jeżeli jest  &ndash; to go nastawiać,
    jeżeli nie  &ndash; to kod ma być nastawiony na `None`.
    Kod jest poprawny, jeśli jest ciągiem znaków (`str`) składającym się z 16 cyfr.
4. Mieć metodę statyczną `check_code`. Powinna ona przyjmować jeden parametr (kod rejestracyjny)
    i zwracać wartość logiczną. `True`, jeśli kod jest poprawny, `False`, jeśli nie.
    Kod jest poprawny, jeśli jest ciągiem znaków (`str`) składającym się z 16 cyfr.
5. Mieć getter (`property`) i setter dla atrybutu `registration_code`.
    * getter powinien po prostu zwrócić wartość kodu rejestracyjnego.
    * setter powinien ustawić numer rejestracyjny tylko w przypadku, gdy numer ten jest prawidłowy.

Rozwiązanie zapisz w pliku `answer5.py`.       
      



## Zadanie 5 (5pkt)
Napisz w Pythonie klasę `VIPUser`. Klasa ma spełniać następujące właściwości:

1. Dziedziczyć po klasie `User` (zajrzyj do modułu **exam_lib**) oraz mieć dodatkowy atrybut: ```_vip_card_number```.
    Atrybut ten nie powinien być dostępny na zewnątrz klasy (pamiętaj o odpowiedniej konwencji nazw).

2. Mieć metodę `__init__`, która przyjmuje następujące dane:
    * imię,
    * nazwisko,
    * mail,
    * numer karty VIP.
    Imię, nazwisko i mail mają być przekazywane do odpowiedniej metody klasy nadrzędnej.
  Metoda ta ma sprawdzać, czy podany numer jest prawidłowy.
    * Jeżeli jest  &ndash; to go nastawiać.
    * Jeżeli nie  &ndash; to numer ma być nastawiony na ```None```.

3. Mieć metodę statyczną ```_check_card(new_number)``` &ndash; numer jest prawidłowy, jeżeli:
    * jest większy niż 999,
    * podzielny przez 2.
    Metoda ma zwracać wartość logiczną. Metoda nie powinna być dostępna z zewnątrz klasy.

4. Mieć metodę statyczną ```use_vip_card()``` &ndash; ciało metody może zostać puste (lub zwrócić wartość `None`).
5. Mieć setter i getter (`@property`) dla atrybutu ```_vip_card_number```.
    * Setter ma nastawiać zmienną `_vip_card_number` (jeżeli podany nowy numer spełnia założenia).
    * Getter (property) ma po prostu zwrócić wartość atrybutu.

Rozwiązanie zadania umieść w pliku `answer5.py`.


#xam_lib.py:
class User:
    def __init__(self, mail, name, surname):
        self.mail = mail
        self.name = name
        self.surname = surname

    def say_hello(self):
        return "User %(name)s %(surname)s says hello." % {
            "name": self.name,
            "surname": self.surname
        }
















FLASK

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














    ![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709387-2b7ac180-571f-11eb-9b94-517aa6d501c9.png)



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
SQL_SELECT_MOVIE = """SELECT * FROM movies WHERE;""" #or id=%s
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

            cursor.execute(SQL_SELECT_MOVIE, (id))

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

            cursor.execute(SQL_SELECT_MOVIES)

            result = []


            result.append(str(id))
        return "<h3>Film o id  {id}: </h3>" + "<br>\n".join(result)
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
def view_movie_id(id):
    return f'{view_movie_id(id)}'


if __name__ == '__main__':
    app.run(debug=True, port="5002")







 
# Warsztat &ndash; Konfiguracja bazy danych

Zanim przygotujemy skrypt, który utworzy nam bazę danych, musimy przygotować nasz projekt.
W tym celu:
* stwórz folder pod aplikację,
* utwórz repozytorium na `githubie`,
* stwórz plik `.gitignore` i dodaj do niego podstawowe dane (podpowiedź: możesz znaleźć gotowy plik dla pythona w sieci)

**Pamiętaj, o robieniu backapów bazy danych i częstym tworzeniu commitów.** 

Na początek zajmijmy się skonfigurowaniem naszej bazy danych.
Napisz w tym celu skrypt pythona: `create_db.py`, w którym:

1. Utworzysz bazę danych. Jeśli baza już istnieje, skrypt ma poinformować o tym użytkownika, nie przerywając swojego
    działania (Podpowiedź: możesz przechwycić błąd: `DuplicateDatabase`). 
2. Stworzysz tabelę trzymającą dane użytkownika (`users`). Powinna posiadać następujące kolumny:
    * `id` &ndash; klucz główny (najlepiej typu serial),
    * `username` &ndash; ciąg znaków (varchar(255)),
    * `hashed_password` &ndash; ciąg znaków (varchar(80)).
    Jeżeli istnieje już taka tabela, skrypt powinien poinformować o tym użytkownika, nie przerywając swojego działania
    (Podpowiedź: możesz przechwycić błąd: `DuplicateTable`).
3. Stworzysz tabelę przechowującą komunikaty (`messages`). Powinna posiadać następujące kolumny:
    * `id` &ndash; klucz główny (najlepiej typu serial),
    * `from_id` &ndash; klucz obcy do tabeli `users`,
    * `to_id` &ndash; klucz obcy do tabeli `users`,
    * `creation_date` &ndash; timestamp, dodawany automatycznie.
    Jeżeli istnieje już taka tabela, skrypt powinien poinformować o tym użytkownika, nie przerywając swojego działania
    (Podpowiedź: możesz przechwycić błąd: `DuplicateTable`).
    
**Pamiętaj o zamknięciu połączenia. Powinieneś też obsłużyć ewentualne błędy połączenia (`OperationalError`).** 


# Warsztat &ndash; Obiektowa obsługa bazy danych

Mamy już stworzoną naszą bazy danych. Pola na stworzenie biblioteki odwzorowującej nasze tabele w postaci obiektów.
Utwórz teraz osobny moduł (np. `models.py`). W nim umieść kod z klasami, obsługującymi poszczególne tabele.


## Klasa użytkownika

1. Stwórz klasę, obsługującą użytkownika. Powinna ona posiadać następujące atrybuty:
    * `_id` &ndash; ustawione podczas tworzenia na `-1`,
    * `usename` &ndash; nazwa użytkownika,
    * `_hashed_password` &ndash; zahaszowane hasło użytkownika.
2. Udostępnij `_id` i `_hashed_password` do odczytu na zewnątrz.
3. Dodaj metodę, która pozwoli, na ustawienie nowego hasła (Podpowiedź: możesz użyć **settera**).
4. Dodaj metody do obsługi bazy:
    `save_to_db` &ndash; zapis do bazy danych lub aktualizacja obiektu w bazie,
    `load_user_by_username` &ndash; wczytanie użytkownika z bazy danych na podstawie jego nazwy,
    `load_user_by_id` &ndash; wczytanie użytkownika z bazy danych na podstawie jego id,
    `load_all_users` &ndash; wczytanie wszystkich użytkowników z bazy danych,
    `delete` &ndash; usunięcie użytkownika z bazy i nastawienie jego `_id` na `-1`.
    
Podpowiedzi:
* Wszystkie powyższe metody, powinny przyjmować **kursor** do obsługi bazy danych.
* Możesz wykorzystać kod, który omówiliśmy w artykule poświęconym wzorcowi projektowemu **Active Record**.
    Wystarczy, że dodasz do niego metodę, wczytującą użytkownika z bazy na podstawie jego imienia.
    
## Klasa wiadomości

1. Utwórz teraz klasę, która będzie obsługiwała nasze wiadomości. Powinna ona posiadać następujące atrybuty:
    * `_id` &ndash; ustawione podczas tworzenia na `-1`,
    * `from_id` &ndash; id nadawcy, ustawiane podczas tworzenia obiektu,
    * `to_id` &ndash; id odbiorcy, ustawiane podczas tworzenia obiektu,
    * `text` &ndash; tekst do przesłania,
    * `creation_data` &ndash; data utworzenia wiadomości. Podczas tworzenia przypisz do niej `None`. Ustawisz ją
    w momencie zapisu do bazy danych.
2. Udostępnij `_id` na zewnątrz.
3. Dodaj metody do obsługi bazy:
    * `save_to_db` &ndash; zapis do bazy danych lub aktualizacja obiektu w bazie,
    * `load_all_messages` &ndash; wczytanie wszystkich wiadomości.
    
Podpowiedzi:
* Usuwanie wiadomości, nie będzie nam potrzebne. 
* Metody, będą bardzo podobne do tych z klasy użytkownika. Wystarczy, że lekko je zmodyfikujesz.


**Pamiętaj, żeby przetestować, czy biblioteka działa. Możesz wykorzystać scenariusze testowe, opisane w artykule
omawiającym Active Record.**

# Warsztat &ndash; Aplikacja do obsługi użytkowników

Utwórzmy teraz aplikację, obsługującą naszych użytkowników. Będzie to aplikacja konsolowa, przyjmująca argumenty
wprowadzone przez użytkownika. Wykorzystaj do tego bibliotekę `argparse`. 
Aplikacja powinna obsługiwać następujące parametry:
    * `-u`, `--username` &ndash; nazwa użytkownika,
    * `-p`, `--password` &ndash; hasło użytkownika,
    * `-n`, `--new_pass` &ndash; nowe hasło,
    * `-l`, `--list` &ndash; listowanie użytkowników,
    * `-d`, `--delete` &ndash; usuwanie użytkownika,
    * `-e`, `--edit` &ndash; edycja użytkownika.
    
Aplikacja powinna obsługiwać scenariusze opisane poniżej.
Najprościej będzie, przygotować osobną funkcję na każdy, ze scenariuszy. W głównym kodzie programu wystarczy wtedy
sprawdzić parametry instrukcję `if` &ndash; `elif`, a następnie wywołać odpowiednie funkcje. 

## Tworzenie użytkownika

Jeśli podczas wywołania aplikacji, użytkownik poda tylko parametry: `username` i `password`:
* jeśli użytkownik o podanej nazwie istnieje &ndash; zgłaszamy błąd 
    (Podpowiedź: możesz przechwycić błąd: `UniqueViolation`),
* jeśli nie ma takiego użytkownika:
    * jeśli hasło ma co najmniej 8 znaków, należy go utworzyć, korzystając z podanych danych 
    (pamiętaj, o zapisaniu obiektu do bazy danych),
    * jeśli hasło jest za krótkie, należy wyświetlić odpowiedni komunikat.


## Edycja hasła użytkownika

Jeśli podczas wywołania aplikacji, użytkownik poda parametry:
* `username`,
* `password`,
* `edit`,
* `new_pass`,
powinniśmy:
* sprawdzić, czy użytkownik istnieje
* sprawdzić, czy hasło jest poprawne:
    * jeśli tak, sprawdzamy, czy nowe hasło (`new_pass`) ma wymaganą długość:
        * jeśli jest krótsze niż 8 znaków, zgłaszamy to odpowiednim komunikatem,
        * jeśli jest wystarczającej długości, ustawiamy nowe hasło,
    * jeśli hasło jest niepoprawne, zgłaszamy to odpowiednim komunikatem.
    
> Podpowiedź: Do sprawdzenia hasła, możesz wykorzystać funkcję `check_password` z biblioteki `clcrypto`.

## Usuwanie użytkownika

Jeśli podczas wywołania aplikacji, użytkownik poda parametry:
* `username`,
* `password`,
* `delete`,
należy:
* sprawdzić poprawność hasła,
    * jeśli jest poprawne &ndash; usunąć użytkownika z bazy danych,
    * jeśli jest niepoprawne &ndash; poinformować o tym użytkownika odpowiednim komunikatem np. `"Incorrect Password!`.


## Listowanie użytkowników:

Jeśli podczas wywołania aplikacji, użytkownik poda parametr `-l` (`--list`), należy wypisać listę
wszystkich użytkowników. 
   

## Pomoc

Jeśli użytkownik poda inny zestaw parametrów, należy wyświetlić mu panel pomocy. Można to zrobić, wywołując:
metodę `print_help` z obiektu parsera.

##### Przykład:
```python
import argparse

parser = argparse.ArgumentParser()
parser.print_help()
```




# Warsztat &ndash; Aplikacja do obsługi wiadomości

Stwórzmy teraz naszą główną aplikację. Będzie to program konsolowy pozwalający wysyłać i odczytywać wiadomości.
Aplikacja powinna przyjmować od użytkownika następujące argumenty:
* `-u`, `--username` &ndash; nazwa użytkownika,
* `-p`, `--password` &ndash; hasło użytkownika,
* `-t`, `--to` &ndash; nazwa użytkownika, do którego ma zostać wysłana wiadomość,
* `-s`, `--send` &ndash; treść wiadomości,
* `-l`, `--list` &ndash; żądanie wylistowania wszystkich komunikatów użytkownika (flaga).

Do parsowania argumentów użyj biblioteki `argparse`.

Aplikacja powinna obsługiwać scenariusze opisane poniżej.
Najprościej będzie, przygotować osobną funkcję na każdy, ze scenariuszy. W głównym kodzie programu wystarczy wtedy
sprawdzić parametry instrukcję `if` &ndash; `elif`, a następnie wywołać odpowiednie funkcje. 

## Listowanie wiadomości

Jeśli podczas wywołania aplikacji, użytkownik poda parametry: `username` i `password` oraz ustawi flagę `-l`:
* sprawdź, czy użytkownik istnieje, jeśli nie wyświetl odpowiedni komunikat,
* sprawdź, czy hasło jest poprawne:
    * jeśli nie, wyświetl odpowiedni komunikat,
    * jeśli tak, wypisz wszystkie wiadomości wysłane do tego użytkownika.
    
Każda z wiadomości powinna zawierać:
* adresata,
* datę wysłania wiadomości,
* treść wiadomości.

## Wysłanie wiadomości

Jeśli podczas wywołania aplikacji, użytkownik poda parametry: `username` i `password` oraz dodatkowo 
ustawi parametr `-t` (`--to`) i `-s` (`--send`):
* sprawdź, czy użytkownik istnieje, jeśli nie wyświetl odpowiedni komunikat,
* sprawdź, czy hasło jest poprawne:
    * jeśli nie, wyświetl odpowiedni komunikat,
    * jeśli tak:
        * sprawdź, czy adresat wiadomości istnieje (`--to`), jeśli nie, poinformuj o tym użytkownika,
        * sprawdź, czy wiadomość jest krótsza, niż 255 znaków:
            * jeśli nie, wyświetl odpowiedni komunikat,
            * jeśli tak, utwórz wiadomość i zapisz ją do bazy danych.


## Pomoc

Jeśli użytkownik poda inny zestaw parametrów, należy wyświetlić mu panel pomocy. Można to zrobić, wywołując:
metodę `print_help` z obiektu parsera.

##### Przykład:
```python
import argparse

parser = argparse.ArgumentParser()
parser.print_help()
```






    
