# Podstawy-programowania-w-Pythonie-egzamin-probny

Egzamin
Podstawy programowania w Pythonie – egzamin próbny.

Przed przystąpieniem do rozwiązywania zadań przeczytaj poniższe wskazówki
Odpowiedzi na pytania programistyczne umieszczaj w odpowiednich plikach answers1.py – answer6.py





Zadanie 1. (2pkt)

Napisz funkcję shorten, która przyjmie dowolnie długi napis, po czym zwróci skrót napisu, jak w przykładzie:
shortened = shorten("Don't repeat yourself")
print(shortened)

DRY
shortened = shorten("Read the fine manual")
print(shortened)

RTFM
shortened = shorten("All terrain armoured transport")

print(shortened)
ATAT



#Napisz funkcję shorten, która przyjmie dowolnie długi napis, po czym zwróci skrót napisu,

def shorten(shortend="Domyslny tekst"):
    new_list = []


    #for i in len(shortend()):
    seperate = shortend.split(" ")
    print(seperate)

    print("I Spospb: ", end="")
    for i in range(len(seperate)):
        print(seperate[i][0].upper(), end="")
        #print(type(seperate))
        new_list.append(seperate[i][0])
    print("")
    print("")

    print("W postaci nowej listy:", new_list)
    print("Wersja krotsza: ", end="")
    x = ("".join(str(i) for i in new_list))
    print(x.upper())
    return ''





if __name__ == '__main__':
    shortend = shorten("Jacek Rogowski pochodze z miasta Szczecin")
    print(shortend)


# Zadanie 2. (3pkt)
# Napisz funkcję name_sorter, która przyjmie jako parametr listę imion.
# Funkcja ma zwrócić słownik:
#     klucz o nazwie male ma mieć jako wartość imiona męskie z listy wejściowej,
#     klucz o nazwie female ma mieć jako wartość imiona żeńskie z listy wejściowej.
# Dodatkowo, posortuj imiona w ramach swoich list.
# Należy przyjąć, że imiona żeńskie, to te, które kończą się literą "a". Barnabę możemy spokojnie zignorować. ;-)
#
# Przykład:
# names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]
# print(name_sorter(names))
# {'female': ['Alicja', 'Barbara'], 'male': ['Andrzej', 'Cezary', 'Henryk']}

def name_sorter(names):
    list_mal = []
    list_fem = []
    dict = {
        "female":"",
        "male":""
        }

    print("Zenskie: ", end="")
    for i in range(len(names)):
        if names[i][-1] == "a":
            print(names[i], end=" ")
            #dict.update({"female": names[i], })
            list_fem.append(names[i])
    dict.update({"female": list_fem, })


    print("")
    print("Meskie: ", end="")
    for i in range(len(names)):
       if names[i][-1] != "a":
           print(names[i], end=" ")
           #dict.update({"male": names[i]}, )
           list_mal.append(names[i])
    dict.update({"male": list_mal, })

    print("")
    print(dict)

    return ""

if __name__ == '__main__':
    names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]

    print(name_sorter(names))




    # Napisz funkcję check_palindrome, która pobierze dowolnie długi łańcuch tekstowy i sprawdzi, czy jest palindromem. Funkcja powinna zwracać True, jeśli łańcuch jest palindromem, False, jeśli nie jest.
# Podpowiedzi:
#
#     Palindrom to słowo lub zdanie, które czytane wspak brzmi tak samo, jak od początku, np. "kajak", "radar", czy "Kobyła ma mały bok".
#
#     Podczas sprawdzania palindromu, pamiętaj o spacjach.

def check_palindrome(word):


    #for i in range(len(word)):
    print("                Input:", word)
    print("Inverted and no space:", word.replace(" ","")[::-1]) #Replaced " " for "" and printed inverted

    word_no_space_lowered = word.replace(" ","").lower() #word in lower cases with no space

    if word_no_space_lowered == word_no_space_lowered[::-1]:

        print("True")

    else:
        print("False")
    print("")

if __name__ == '__main__':
    check_palindrome("kajak")
    check_palindrome("radar")
    check_palindrome("sdfdsfff")
    check_palindrome("Kobyła ma mały bok")



    # Funkcja ma jako wynik, zwrócić listę liczb w podanym zakresie, które jednocześnie są podzielne przez 2 i niepodzielne przez 3.
# Wprowadzony zakres powinien być domknięty, tzn. należy sprawdzić także liczby, które są początkiem i końcem zakresu.

def div(start, end):
    div2 = []
    div3 = []
    for start in range(end+1):  #domkniecie przedzialu <0 do 20>?
        if start % 2 == 0 and start % 3 != 0:
            div2.append(start)
        #if start % 3 == 0:
            #div3.append(start)

    print(div2)
    #print("")
    #print(div3)
    return ""




if __name__ == '__main__':
    result = div(0, 20)
    print(result)





    # Napisz funkcję roll, która przyjmie 3 parametry:
#     liczbę kostek,
#     opcjonalnie: typ kostki (dozwolone kostki 3, 4, 6, 8, 10, 12 i 100 ścienne), standardowa wartość, to 6 ,
#     opcjonalnie: modyfikator wyniku (liczba dodana, lub odjęta od wyniku kośćmi), standardowa wartość, to 0.
# Następnie funkcja ma zasymulować rzut odpowiednią liczbą kostek, zsumować wyniki i dodać (lub odjąć) modyfikator. Wynik ma zwrócić.
# Dla uproszczenia możesz przyjąć, że wszystkie liczby podane jako parametry są liczbami naturalnymi.
# Jeśli użytkownik wpisze kostkę, której nie ma w powyższym zestawieniu, funkcja ma wyrzucić wyjątek Exception z komunikatem "No such dice!"


from random import randint

def roll(quantity_dism, type_dism = 6, moderator = 0):
    # try:
       # if type_dism is not (3 or 4 or 6 or 8 or 10 or 12 or 100):
        if type_dism not in (3, 4, 6, 8, 10, 12, 100):
            raise Exception(f"No such dism!: {type_dism}")
        else:
            total = 0
            for i in range(quantity_dism):
                shuffled_points = randint(1, type_dism)
                print(i+1, "los, wynosi:", shuffled_points)
                total += shuffled_points
            print(total + moderator)

    # except: Excption
    # print("No such dice!")

if __name__ == '__main__':

    roll(3, 10, )
    roll(1, 100, -20)
    roll(2, 7,20)









# Python i bazy danych &ndash; egzamin próbny.

Przed przystąpieniem do rozwiązywania zadań przeczytaj poniższe wskazówki

##### Odpowiedzi na pytania programistyczne umieszczaj w odpowiednich plikach *answer1.py* &ndash; *answer5.py*

**Powodzenia!**

----------------------------------------------------------------------------------------

## Zadanie 1 (3pkt)

Napisz skrypt (program) w Pythonie tworzący bazę danych.
* Powinien utworzyć bazę danych o nazwie `exam2`
* Powinien być odporny na błędy połączenia.
* Powinien poinformować użytkownika, jeśli taka baza danych już istnieje.

Rozwiązanie umieść w pliku `answer1.py`.

---

## Zadanie 2 (5 pkt)

W bazie danych chcemy mieć następujące tabele:

```SQL
* Users: id :
    autonumerowany (klucz główny),
    name : varchar(60),
    email : varchar(60),
    password : varchar(60)
* Messages:
    id : autonumerowany (klucz główny),
    user_id: int,
    message : text
* Items: id :
    autonumerowany (klucz główny),
    name : varchar(40),
    description : text,
    price : decimal(7,2)
* Orders: id :
    autonumerowany (klucz główny),
    description : text
```

Zajrzyj do pliku **answer2.py**, znajdziesz tam zdefiniowane zmienne: `query_1`, `query_2` ... `query_9`.
W zmiennych umieść następujące zapytania SQL:

* **query_1**: Tworzące tabelę `Users` (email ma być unikatowy).
* **query_2**: Tworzące tabelę `Messages` (pamiętaj o relacji jeden do wielu z tabelą `Users`).
* **query_3**: Tworzące tabelę `Items`.
* **query_4**: Tworzące tabelę `Orders`.
* **query_5**: Stworzenie relacji wiele do wielu między tabelami `Items` a `Orders`
    (tabela ma się nazywać `ItemsOrders`, a pola relacji `item_id` i `order_id`).
* **query_6**: Wybranie wszystkich przedmiotów (Item) o cenie większej niż 13.
* **query_7**: Włożenie do tabeli `Orders` nowego zamówienia o opisie "przykładowy opis".
* **query_8**: Usuniecie użytkownika o `id` 7.
* **query_9**: Wybranie wszystkich użytkowników z tabeli `Users`,
    którzy mają przypisaną jakąś wiadomość w tabeli `Messages`.
* **query_10**: Dodanie do tabeli `Messages` pola `date_of_created`, przechowującego datę utworzenia wiadomości.
    Powinno być uzupełniane automatycznie podczas dodawania wiersza do bazy. Może przyjmować wartość `null`
    (dla wiadomości wpisanych do bazy, przed jego dodaniem.)     

Za każde zapytanie przysługuje pół punktu.

**Uwaga 1:** Podczas pisania zapytań nie używaj nazwy bazy danych w zapytaniu.
**Uwaga 2:** Pilnuj dokładności nazw tabel i pól oraz typów danych!

---






query_1 = """CREATE TABLE users (
    id SERIAL,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(60),

    PRIMARY KEY(id)
);"""
query_2 = """CREATE TABLE messages (
    id SERIAL,
    user_id INTEGER,
    message TEXT,

    PRIMARY KEY(id),
    FOREIGN KEY(message) REFERENCES users(id)
);"""
query_3 = """CREATE TABLE items (
    id SERIAL,
    name VARCHAR(40),
    description TEXT,
    price DECIMAL(7,2),

    PRIMARY KEY(id)
);"""
query_4 = """CREATE TABLE orders (
    id SERIAL,
    description TEXT,

    PRIMARY KEY(id)
);"""
query_5 = """CREATE TABLE itemsorders(
    id SERIAL NOT NULL,
item_id INT,
order_id INT,
PRIMARY KEY(item_id , order_id),
FOREIGN KEY(item_id) REFERENCES items(id),
FOREIGN KEY(order_id) REFERENCES orders(id)
);"""
query_6 = "SELECT * FROM  items WHERE price > 13;"
query_7 = "INSERT INTO orders(description) VALUES ('przykladowy opis');"
query_8 = "DELETE FROM users WHERE id=7;"
query_9 = """
SELECT Users.name AS user_name, Users.id AS user_id, Messages.message 
AS u_message FROM Users JOIN Messages on Users.id=Messages.user_id;
"""
query_10 = "ALTER TABLE Messages ADD date_of_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP"











## Zadanie 3 (3pkt)

Napisz **generator** `dividers`, który przyjmie jeden argument `number`.
Generator powinien generować kolejne dzielniki liczby przekazanej jako argument.

##### Przykład użycia:
```python
for i in dividers(6):
    print(i)
```

##### Wynik:
```
1
2
3
6
```

Rozwiązanie umieść w pliku `answer3.py`.

---




def deviders(n):
    for i in range(1, n+1):
        if n % i == 0:
            yield i




for i in deviders(8):
    print(i)




## Zadanie 4 (4pkt)

Używając frameworka **Flask**, napisz stronę udostępnioną pod adresem `/add_product`,
która spełni następujące założenia:

1. Po wejściu metodą GET wyświetli pusty formularz, który będzie zawierał następujące pola:
    * `name`: nazwę produktu,
    * `description`: opis produktu,
    * `price`: cenę produktu.

    Pamiętaj: nazwij pola dokładnie tak, jak w poleceniu (ustaw odpowiednio atrybut `name` tagu `<input>`)

2. Po wejściu metodą POST:
    * zweryfikuje poprawność danych,
    * zapisze te dane do bazy danych do tabeli `Items` (tabela taka sama jak w zadaniu 1) i wyświetli komunikat
    `Product added!`,
    * jeśli którakolwiek wartość będzie błędna, zamiast zapisywania do bazy, wyświetli na stronie komunikat:
    `Invalid data!`.

Pamiętaj o poprawnym połączeniu do bazy danych i jego zamknięciu.
Rozwiązanie umieść w pliku `answer4.py`.






from flask import request
import psycopg2
from psycopg2 import connect
from flask import Flask


USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"
PORT = 5431
DB = "exam2"


CREATE_DB = "CREATE DATABASE exam2"
SQL_INSERT_PRODUCT = """
INSERT INTO items (name, description, price) VALUES (%s, %s, %s);
"""

def create_database_exam2():
    conn = psycopg2.connect(user=USER, password=PASSWORD, port=PORT, host=HOST) #database=DB or "exam2"
    conn.autocommit = True
    try:
        with conn.cursor() as cursor:
            try:
                cursor.execute(CREATE_DB)
                return f"DATABASE CREATED: {CREATE_DB}"
            except psycopg2.errors.DuplicateDatabase:
                return f"<b>ERROR Database already exist</b>"
        #conn.commit()


    finally:
        conn.close()
        print("Bye")


def add_products_to_database(name, description, price):
    conn = psycopg2.connect(user=USER, password=PASSWORD, port=PORT, host=HOST, database=DB)
    # conn.autocommit = True
    try:
        with conn.cursor() as cursor:
            cursor.execute(SQL_INSERT_PRODUCT, (name, description, price))
        conn.commit()


    finally:
        conn.close()
        print("Bye")



html_GET = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
</head>

<body>

    <!-- products -->
    <div>
        <form class="add_product" method="post" action="#">
            <input type="hidden" name = "id">
            <label>Name</label><br>
            <input name="name" type="text" maxlength="255" value=""/><br>
            <label>Description</label><br>
            <input name="description" type="text" maxlength="255" value=""/><br>
            <label>Price</label><br>
            <input name="price" type="text"/><br>                                              <!-- type = number!! -->
            <button type="submit" name="submit" value="product_submit">Add</button>
        </form>
    </div>

</body>
</html>
"""

app = Flask(__name__)

@app.route('/')
def create_exam2_database():
    print("I try creating exam2 database")
    return create_database_exam2()



@app.route("/add_product", methods=["GET", "POST"])
def add_products():
    if request.method == 'GET':
        return "<h3>Fill to add Product</h3>" + html_GET

    if request.method == 'POST':

        name = str(request.form["name"])
        description = str(request.form["description"])
        try:
            price = float(request.form["price"])
        except ValueError:
            return f"<b>WRONG VALUE</b>"

        print(request.form)
        add_products_to_database(request.form['name'], request.form['description'], request.form['price'])
        return f"""
        Item added into database: <br>
        {name} <br>
        {description} <br>
        {price}
        """


if __name__ == '__main__':
    app.run()









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


#Exam_lib.py:
# Zadanie 5 (5pkt)
#
# Napisz w Pythonie klasę VIPUser. Klasa ma spełniać następujące właściwości:
#
#     Dziedziczyć po klasie User (zajrzyj do modułu exam_lib) oraz mieć dodatkowy atrybut: _vip_card_number. Atrybut ten nie powinien być dostępny na zewnątrz klasy (pamiętaj o odpowiedniej konwencji nazw).
#
#     Mieć metodę __init__, która przyjmuje następujące dane:
#         imię,
#         nazwisko,
#         mail,
#         numer karty VIP. Imię, nazwisko i mail mają być przekazywane do odpowiedniej metody klasy nadrzędnej. Metoda ta ma sprawdzać, czy podany numer jest prawidłowy.
#         Jeżeli jest – to go nastawiać.
#         Jeżeli nie – to numer ma być nastawiony na None.
#
#     Mieć metodę statyczną _check_card(new_number) – numer jest prawidłowy, jeżeli:
#         jest większy niż 999,
#         podzielny przez 2. Metoda ma zwracać wartość logiczną. Metoda nie powinna być dostępna z zewnątrz klasy.
#
#     Mieć metodę statyczną use_vip_card() – ciało metody może zostać puste (lub zwrócić wartość None).
#
#     Mieć setter i getter (@property) dla atrybutu _vip_card_number.
#         Setter ma nastawiać zmienną _vip_card_number (jeżeli podany nowy numer spełnia założenia).
#         Getter (property) ma po prostu zwrócić wartość atrybutu.
#
# Rozwiązanie zadania umieść w pliku answer5.py.


#from exam_lib import User

class User:
    def __init__(self, name, surname, mail):
        self.mail = mail
        self.name = name
        self.surname = surname

    def say_hello(self):
        return "User %(name)s %(surname)s says hello." % {
            "name": self.name,
            "surname": self.surname
        }

class VIPUser(User):
    __vip_card_number = 1

    # dlaczego nie vip_number nie powinien byc z __?
    def __init__(self, name, surname, mail, __vip_card_number):
        super().__init__(name=name, surname=surname, mail=mail)
        self._vip_card_number = __vip_card_number if isinstance(__vip_card_number, int) else None

    def __str__(self):
        return f"{self.name} | {self.surname} | {self.mail} | {self._vip_card_number}"



    @staticmethod
    def check_card(__vip_card_number):
        return __vip_card_number > 999 and __vip_card_number % 2 == 0

    @staticmethod
    def use_vip_card():
        pass

    @property
    def vip_card_number(self):
        return self._vip_card_number

    @vip_card_number.setter
    def vip_card_number(self, _vip_card_number):
        self._vip_card_number = __vip_card_number if self._check_card(__vip_card_number) else None

User2 = User("Kacper", "Szurek", "asdas@o2.pl")
User1 = VIPUser("Jacek", "Rogowski", "asdas@o2.pl", 12)
print("\n")
print(User1._vip_card_number)

print("\n")


print(User1.say_hello())
print(User1)
print(User1._vip_card_number)
print(User1.check_card(User1._vip_card_number))  #True 1222

User3 = VIPUser("Jacek", "Rogowski", "asdas@o2.pl", 4232)
print(User3)
User4 = VIPUser("Jacek", "Rogowski", "asdas@o2.pl", 222)
print(User4)

print(User2.say_hello())
print(User2)





























    EGZAMIN I MODUL PRAWDZIWY:


## Zadanie 1. (2pkt)

Napisz funkcję `check_character`, która:
* przyjmie napis oraz pojedynczy znak, 
* zwróci liczbę wystąpień znaku w napisie.

Nie korzystaj z metody `count`. Zamiast tego, użyj **pętli**, albo **list comprehension**.

##### Przykład:
```python
print(check_character('Order of the Phoenix', 'o'))
```
##### Wynik
```plaintext
2
```

> Wielkość znaków ma znaczenie `('A' != 'a' etc.)`.

Rozwiązanie wpisz w pliku `answer1.py`.



# Zadanie 1. (2pkt)
# Napisz funkcję check_character, która:
#     przyjmie napis oraz pojedynczy znak,
#     zwróci liczbę wystąpień znaku w napisie.
# Nie korzystaj z metody count. Zamiast tego, użyj pętli, albo list comprehension.
# Przykład:
# print(check_character('Order of the Phoenix', 'o'))
# Wynik
# 2
#     Wielkość znaków ma znaczenie ('A' != 'a' etc.).
# Rozwiązanie wpisz w pliku answer1.py.

def check_character(sentence, char):

    i = 0
    for _ in range (len(sentence)):
        if sentence[_] == char:
            i = i + 1

    return print("Wynik ", i)


if __name__ == '__main__':
    print(check_character('Order of the Phoenix', 'o')) #2
    print(check_character('Ooooo', 'o')) #4
    print(check_character('OooOo', 'O')) #2
    print(check_character('OooOo', 'x'))  #0




################################################################################################import random
def check_character(word, sign):
    amount = 0
    for i in word:
        if sign in i:
            amount += 1
    return amount


print(check_character("Oanusz protest", 'o'))




    ## Zadanie 2. (4pkt)

Napisz funkcję `get_random`.
Funkcja powinna:
* Przyjąć jeden opcjonalny parametr `number` &ndash; ilość liczb jakie mają zostać wylosowane. 
    **Domyślna wartość to `3`.**
* Losować kolejno liczby z przedziału 1-100. Wylosowane liczby nie mogą się powtarzać.
    Wykorzystaj do tego pętlę `while` i losuj tak długo, aż uzyskasz `number` unikalnych liczb.
    **Nie korzystaj z metod `sample` i `shuffle`.** 
* Jeżeli zostanie do niej przekazany błędny parametr funkcja powinna **wyrzucić** wyjątek `Exception` 
    z komunikatem `"Invalid Data!"`.
* Funkcja powinna zwrócić posortowaną listę wylosowanych liczb (od najmniejszej do największej).

Przykładowe wyniki działania funkcji:

##### Przykład:
```python
print(get_random(5))
```
##### Wynik (przykładowy):
```plaintext
[2, 33, 46, 81, 100]
```

##### Przykład:
```python
print(get_random())
```
##### Wynik (przykładowy):
```plaintext
[58, 66, 99]
```

Rozwiązanie zadania umieść w pliku `answer2.py`.





import random


def get_random(number = 3):

    i = 0
    list = []

    while i != number:
        randomized_number = random.randint(1, 100)

        if randomized_number not in list:
            list.append(randomized_number)
        else:
            i -= 1
        i += 1

    tuple(list)
    return sorted(list)




if __name__ == '__main__':
    try:
        print(get_random(4))
    except NameError:
        print("Invalid Data!")


#####################################################################################################


def get_random(number=3):
    try:
        number = int(number)
    except ValueError:
        raise Exception("Invalid Data!")
    if number > 100:
        raise Exception("Invalid Data!")
    our_numbers = []
    while len(our_numbers) < number:
        x = random.randint(1, 100)
        if x not in our_numbers:
            our_numbers.append(x)
    our_numbers.sort()
    return our_numbers


print(get_random(5))







        ## Zadanie 3. (5pkt)

W bazie chcemy mieć następujące tabele:
```SQL
* Readers:
    id : serial primary key,
    name : varchar(60),
    email : varchar(60),
    is_active : boolean, nie może być null, standardowa wartość: true
* Books:
    id : serial primary key,
    title : varchar(60),
    price : decimal(5, 2), 
    author : varchar(60),
    publishing_houses_id: int
* PublishingHouses:
    id : serial primary key,
    name : varchar(60),
    city : varchar(20),
    address : varchar(120)
```

W pliku `answers3.py` znajdziesz szereg zmiennych: `query_1 = ""` ... `query_10 = ""`.
Napisz następujące zapytania SQL i umieść je odpowiednio we wskazanych zmiennych:

1. Tworzące tabelę `Readers` (email ma być unikatowy).
2. Tworzące tabelę `PublishingHouses`.
3. Tworzące tabelę `Books` (dodaj odpowiednią relację z tabelą `PublishingHouses`:
    * każda książka może mieć jednego wydawcę,
    * każdy wydawca może mieć wiele książek w ofercie).
4. Tworzące relację wiele do wielu między tabelami `Readers` a `Books`.
5. Wyciągające z bazy wszystkie książki o cenie większej niż 10.
6. Wstawiające do tabeli `PublishingHouses` nowe wydawnictwo o nazwie "Super Książki",
    mieszczące się w miejscowości Kaczy Dół, przy ulicy Batorego 120.
7. Usuniecie książki o `id` 12.
8. Wybierające wszystkich czytelników, którzy kiedykolwiek wypożyczyli jakąś książkę
    (na podstawie relacji wiele do wielu między książką, a czytelnikiem; p. punkt 5).
9. Dezaktywujące użytkownika o id 2 (ustaw wartość `is_active` na false dla tego użytkownika,
    załóż że użytkownik już istnieje w bazie).
10. Dodanie do tabeli `Readers` pola `date_of_birth` przechowującego datę urodzenia czytelnika.
    Pole może przyjmować wartość `null`.

Za każde zapytanie przysługuje pół punktu.






query_1 = """
CREATE TABLE Readers
(
id SERIAL PRIMARY KEY,

name varchar(60),
email varchar(60) UNIQUE,
is_active BOOLEAN DEFAULT TRUE
);
"""
query_2 = """
CREATE TABLE PublishingHouses
(
id SERIAL PRIMARY KEY,
publishinghouses_id INT,

name varchar(60),
city varchar(20),
address varchar(120)

FOREIGN KEY(publishinghouses_id) REFERENCES cinemas(id),

);
"""
query_3 = """
CREATE TABLE Books
(
id SERIAL PRIMARY KEY,
book_id INT,

title varchar(60),
price DECIMAL(5,2),
author VARCHAR(60),
publishing_houses_id INT

FOREIGN KEY(book_id) REFERENCES PublishingHouses(id) ON DELETE CASCADE
FOREIGN KEY(publishinghouses_id) REFERENCES PublishingHouses(id)
);
"""
query_4 = """
CREATE TABLE Readers_Books(
reader_id INT,
book_id INT,
PRIMARY KEY(reader_id, book_id),
FOREIGN KEY(reader_id) REFERENCES Readers(id),
FOREIGN KEY(book_id) REFERENCES Books(id)
);
"""
query_5 = "SELECT * FROM  Books WHERE price > 10;"
query_6 = "INSERT INTO PublishingHouses(name, city, address) VALUES ('Super Książki', 'Kaczy Dół', 'Batorego 120');"
query_7 = "DELETE FROM Books WHERE id=12;"
query_8 = """
 SELECT Readers.name AS reader_name, Readers.id AS reader_id, Books.name AS Books_name
    FROM Readers JOIN Books ON Readers.id=Books.reader_id
"""

query_9 = """
UPDATE Readers
SET is_active= FALSE
WHERE id = 2; 
"""
query_10 = """ALTER TABLE Readers
ADD date_of_birth DATE DEFAULT NULL"""







## Zadanie 4. (4 pkt)

Używając frameworka **Flask**, napisz stronę, która spełni następujące założenia:

1. Po wejściu metodą GET wyświetli pusty formularz, który będzie zawierał następujące pola:
    * `name`: imię,
    * `email`: email czytelnika.

2. Po wejściu metodą POST:
    * zweryfikuje poprawność danych 
        (wystarczy sprawdzić, czy imię nie jest puste i w czy w polu `email` znajduje się znak "@"),
    * zapisze te dane do bazy danych do tabeli `Readers` (tabela taka sama jak w zadaniu 3),
    * jeśli którakolwiek dana będzie błędna, zamiast zapisywania do bazy, wyświetli na stronie komunikat o błędzie.

Pamiętaj o poprawnym połączeniu do bazy danych i jego zamknięciu.

Rozwiązanie zapisz w pliku `answer4.py`.



from flask import request
import psycopg2
from psycopg2 import connect
from flask import Flask


USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"
PORT = 5431
DB = "exam"

SQL_INSERT_IN_READERS = """
INSERT INTO Readers (name, email) VALUES (%s, %s);
"""


def add_products_to_database(name, email):
    conn = psycopg2.connect(user=USER, password=PASSWORD, port=PORT, host=HOST, database=DB)
    # conn.autocommit = True
    try:
        with conn.cursor() as cursor:
            cursor.execute(SQL_INSERT_IN_READERS, (name, email))
        conn.commit()


    finally:
        conn.close()
        print("Bye")



html_GET = """
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
</head>

<body>

    <!-- products -->
    <div>
        <form class="add_product" method="post" action="#">
            <label>Name</label><br>
            <input name="name" type="text" maxlength="255" value=""/><br>
            <label>Email</label><br>
            <input name="email" type="email" maxlength="255" value=""/><br>

            <button type="submit" name="submit" value="submit">Add</button>
        </form>
    </div>

</body>
</html>
"""

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def add_products():
    if request.method == 'GET':
        return html_GET

    if request.method == 'POST':
        try:
            name = str(request.form["name"])
            email = str(request.form["email"])

        except ValueError:
            return f"<b>WRONG VALUE</b>"

        print(request.form)
        add_products_to_database(request.form['name'], request.form['email'])
        return f"""
        Item added into database: <br>
        {name} <br>
        {email} <br>
        """


if __name__ == '__main__':
    app.run()




#####################################################################################################################
 
from flask import Flask, render_template, request
import re
from psycopg2 import connect, OperationalError

USERNAME = 'postgres'
PASSWORD = 'postgres'
HOSTNAME = "127.0.0.1"
PORT = '5431'
DATABASE = 'exam1_db'

app = Flask(__name__)


def save_reader(cursor, name, email):
    sql = """INSERT INTO Readers (name, email) VALUES (%s, %s);"""
    values = (name, email)
    cursor.execute(sql, values)


@app.route("/", methods=["GET", "POST"])
def get_or_post():
    if request.method == "GET":
        return html_form()
    elif request.method == "POST":
        name = str(request.form.get("name"))
        email = str(request.form.get("email"))

        if not name or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "Delivered data is invalid!"

        try:
            conn = connect(user=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, database=DATABASE)
            conn.autocommit = True
            curs = conn.cursor()
            try:
                save_reader(curs, name, email)
                return "Reader Added!"
            except:
                return ("Invalid data!")
        except OperationalError:
            print("Connection failed!!")
        finally:
            curs.close()
            conn.close()


def html_form():
    return render_template('form.html')


if __name__ == "__main__":
    app.run(host="localhost", port=8100, debug=True) 


##############################################################################################################

from flask import Flask, request
import psycopg2

app = Flask(__name__)

USER = 'postgres'
PASSWORD = 'coderslab'
HOST = 'localhost'
DATABASE = 'exam'

start = '''
<form method="POST">
    <label>Enter your name: </label>
    <input type="text" name="first_name">
    <label>Enter your email: </label>
    <input type="text" name="email">
    <input type="submit" value="Send">
</form>
'''

sql = '''
INSERT INTO Readers(name, email) VALUES (%s,%s)
'''


@app.route("/", methods=["GET", "POST"])
def web():
    if request.method == "GET":
        return start
    else:
        first_name = request.form.get("first_name")
        email = request.form.get("email")
        if first_name == '' or '@' not in email:
            return "Wrong values"
        else:
            try:
                conn = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, database=DATABASE)
                conn.autocommit = True
            except psycopg2.OperationalError:
                print("Connection error")
            try:
                with conn.cursor() as cursor:
                    cursor.execute(sql, (first_name, email))
                return "Thank You"
            finally:
                conn.close()


if __name__ == "__main__":
    app.run()



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

 




from exam_lib import Book


class Ebook(Book):
    def __init__(self, title, author, page, size, registration_code):
        super().__init__(title, author, page)
        self.size = size
        if isinstance(registration_code, str) and len(registration_code) == 16:
            self._registration_code = registration_code
        else:
            self._registration_code = None

    @staticmethod
    def check_code(registration_code):
        if isinstance(registration_code, str) and len(registration_code) == 16:
            return True
        else:
            return False

    @property
    def registration_code(self):
        return self._registration_code

    @registration_code.setter
    def registration_code(self, registration_code):
        if isinstance(registration_code, str) and len(registration_code) == 16:
            self._registration_code = registration_code

c = Ebook("książka","stefan", 12,"big", "qqqqqqqqqqqqqqqq")
print(c.registration_code)
print(c.check_code("wwwwwwwwwwwwwwww"))
print(c.check_code("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"))



#############################################################################################

import exam_lib


class EBook(exam_lib.Book):
    def __init__(self, title, author, pages, size, registration_code):
        super().__init__(title, author, pages)
        self.registration_code = registration_code
        self.size = size

    @staticmethod
    def check_code(registration_code):
        if isinstance(registration_code, str) and len(registration_code) == 16:
            return True
        else:
            return False

    @property
    def registration_code(self):
        return self._registration_code

    @registration_code.setter
    def registration_code(self, to_check):
        if self.check_code(to_check):
            self._registration_code = to_check
        else:
            self._registration_code = None


if __name__ == "__main__":
    test = EBook('test', 'test', 30, '30mb', '1234567891234567')
    print(test.registration_code) 



