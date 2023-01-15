# ## Zadanie 1 &ndash; Pobieranie danych od użytkownika.

# W pliku `task.py` napisz program, który:

# 1. pobierze z klawiatury imię użytkownika,
# 2. pobierze z klawiatury nazwisko użytkownika,
# 3. wyświetli komunikat "Imię Nazwisko jest programistą Pythona!"

name = input('Podaj imię: ')
sur_name = input('Podaj nazwisko: ')

print(name, sur_name, 'jest programistą Pythona!')

# ## Zadanie 2 &ndash; Łączenie listy

# W pliku `task.py` zdefiniuj tablicę składającą się z liter od `a` do `e`. Następnie wypisz te litery połączone znakiem spacji.

# Do połączenia liter ze sobą użyj metody `join`.

# Wynikiem działania Twojego programu powinno być:
# ```
# a b c d e
```
litery = ['a', 'b', 'c', 'd', 'e']
print(' '.join(litery))



# ## Zadanie 7 &ndash; Dzielenie
# W pliku `task.py` utwórz zmienną `result` i nadaj jej wynik dzielenia 11 przez 7.
# Wyświetl wynik w postaci:
# ```
# 11 : 7 = (tu wstaw wynik)
# ```
#
# > ###### Podpowiedź: użyj funkcji `round`.

result = 11 / 7
print('11 / 7 =', round(result, 2))

name = input('Podaj swoje imię: ')
year = input('Podaj rok swojego urodzenia: ')

age = 2021 - int(year)

print('Użytkownik:', name, 'jest w wieku', age, 'lat')


## Zadanie 10 &ndash; Fizzbuzz

# W pliku `task.py` użyj pętli `for` aby napisać program FizzBuzz. W pętli, która wykona się dla liczb z zakresu od 1 do 100 (włącznie):
# * jeżeli liczba jest podzielna przez 3 i 5, wypisz na ekranie `FizzBuzz` (przykładowo dla liczby 15 ma się wypisać **tylko** `FizzBuzz`),
# * jeżeli liczba jest podzielna przez 3, wypisz na ekran `Fizz`,
# * jeżeli liczba jest podzielna przez 5, wypisz na ekran `Buzz`,
# * w przeciwnym wypadku wypisz na ekran liczbę.

# ```
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# ...
# ```

for i in range(1, 101, 1):

    if (i % 5 != 0) and (i % 3 != 0):
        print(i)
    if (i % 5 == 0) and (i % 3 == 0):
        print('FizzBuzz')

    if i % 3 == 0:
        print('Fizz')
    if i % 5 == 0:
        print('Buzz')
        '''for i in range(1, 20, 1):

            if (i % 5 != 0) and (i % 3 != 0):
                print(i)
            if (i % 5 == 0) and (i % 3 == 0):
                print('FizzBuzz')
            if i % 3 == 0:
                print('Fizz')
            if i % 5 == 0:
                print('Buzz')'''

















#Zadanie2

rows = random.randint(5, 15)
columns = random.randint(5, 15)

# while rows <= columns:
print("Wartosc rows:", columns)
print("Wartosc colums:", rows)
# print(rows * "*")


for i in range (columns):
    print(rows * "*")


## Zadanie 2
1. Zadeklaruj zmienne `rows` i `columns` w której będą losowe liczby z zakreso od 5 do 15.
2. Wyświetl na ekranie wylosowane liczby.
3. Wyśwetl na ekranie prostokąt zbudowany z gwiazdek (`*`) o wylosowanych rozmiarach. 

Przykład działania programu:
```python
Wartość zmiennej rows: 5
Wartość zmiennej columns: 10

**********
**********
**********
**********
**********
```




 

#Zadanie3## Zadanie 3
1. Zadeklaruj zmienne `size` w której będzie losowa liczba z zakresu od 3 do 9.
2. Wyświetl na ekranie wylosowaną liczbę.
3. Wyświetl na ekranie choinkę zbudowaną z gwiazdek (`*`) o wylosowanych rozmiarach.
> **Rozwiązując zadanie nie korzystaj z mnożenia stringów!** Zamiast tego użyj 2 pętli.   

Przykład działania programu:
```plaintext
Wielkość choinki: 5

# *
# **
# ***
# ****
# *****
# ```

size = random.randint(3, 9)
print("Wielkosc choinki:", size)

for i in range(1, size + 1):
    print("*" * i)

print("DRUGI SPOSOB:")
for i in range(1, size + 1):
    for n in range(i):
        print("*", end="")
    print("")




    # Zadanie 7
#
#     Napisz funkcję is_even, która przyjmie parametr number – dowolną liczbę całkowitą (możesz założyć, że programista wprowadzi prawidłową liczbę, nie musisz tego sprawdzać). Funkcja ma zwrócić True, jeśli liczba jest parzysta, False – jeśli nie.
#
# Hint: Liczba jest parzysta, jeśli dzieli się przez 2 bez reszty. Wykorzystaj operator modulo %.
#
#     Napisz funkcję iterate_through, która przyjmie parametr number (nie musisz sprawdzać poprawności). Następnie funkcja w pętli powinna przeitrerować od 1 do wartości number i sprawdzić parzystość kolejnej liczby. Wynik należy wypisać na ekranie (nie zwrócić). Do sprawdzenia parzystości wykorzystaj funkcję is_even, napisaną przed chwilą.

#ZADANIE 7

def is_even(number):
    return number % 2 == 0
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# print(is_even(10))


print("POD ZADANIE:")
def iterate_through(number):
    return number

for i in range(1, iterate_through(11)):
    print(i, "jest parzystą?:", is_even(i))









# Napisz funkcję `create_list`, która przyjmie dwa argumenty dowolnego typu, a następnie zwróci listę,
# której kolejne elementy będą parametrami powtórzonymi czterokrotnie.

temp = 15
temp_2 = '15'

# 1. Zmienne mają innne nazwy
# 2. Wskazują na różne obiekty (tzn. o różnych adresach w pamięci)
print(id(temp))
print(id(temp_2))
# 3. Obiekty, na które wskazują zmienne są różnych typów (int, str)
print(type(temp))
print(type(temp_2))

# print(temp + temp_2)  # Nie można dodać liczby do napisu
# print(temp_2 + temp)  # Nie można dodać napisu do liczby

print(temp * temp_2)
print("Hello" * 5)




#Napisz funkcję `list_keys(d)`, gdzie `d` to dowolny słownik. Niech funkcja przeiteruje pętlą **for** po kluczach
#słownika i zwróci listę tych kluczy. Sprawdź w dokumentacji, czy można zrobić to prościej.



temp = 15
temp_2 = '15'

print(type(temp))
print(type(temp_2))

x = '42'

if type(x) is int:
    print(x * 5)
elif type(x) is float:
    print(x / 5)
elif type(x) is str:
    print(x)

#isinstance(x, int)



# Napisz funkcję `find_short_words`, która przyjmie listę wyrazów.
# Funkcja powinna zwrócić listę słów krótszych od 5 znaków.

def find_short_words(words):
    short = []
    for word in words:
        if len(word) < 5:
            short.append(word)
    return short

    # for i in len.words[i]:
    #     i += 1
    #     if len.words[i] == 3:
    #         return words[]


l = find_short_words(['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie'])

print(l)





# Napisz funkcję `suma(numbers)` gdzie `numbers` to lista liczb dowolnego typu.
# Funkcja powinna zwrócić sumę wszystkichh elementów listy `numbers`. Dla uproszczenia możesz przyjąć,
# że wszystkie parametry wprowadzone przez programistę będą poprawnymi liczbami.
#
# **Uwaga:** funkcję nazywamy nieco niepoprawnie (po polsku) i robimy to świadomie!
# Nie możemy nazwać funkcji `sum()` ponieważ taka funkcja już istnieje w standardzie języka Python.



def suma(numbers):
    total = 0
    for i in numbers:
        total += 1

    return total

numbers = [2,3,3,4]
print(suma(numbers))

# def suma(numbers=None):
#     if numbers is None:
#         numbers = []
#     return sum(numbers)
# no = [1, 2.5, 3.6, 4.6, 5, 6, -7, 8]
# print(suma(no))






# Napisz funkcję `mean(numbers)`, gdzie `numbers` to lista liczb dowolnego typu.
# Funkcja powinna zwrócić średnią arytmetyczną wszystkich elementów listy numbers.
# Czy znasz jakiś sposób, by ułatwić sobie pracę?


def add(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def mean(numbers):
    return sum(numbers) / len(numbers) if len(numbers) > 0 else 0
    # if len(numbers) > 0:
    #     return add(numbers) / len(numbers)
    # else:
    #     return 0


print(mean([]))
print(mean([1, 2, 3]))
print(mean([3, 3, 3]))







## Zadanie 1

Napisz funkcję `message`, która jako parametr przyjmie słownik o następujących kluczach:

* **name**,
* **role**,
* **movie**.

Następnie niech funkcja przygotuje sformatowany napis: "In _movie_, _name_ is a _role_.", 
gdzie w odpoweidnie miejsca podstawi wartości z ww. kluczy. 
Jeśli któregoś z kluczy nie będzie w słowniku, funkcja ma zwrócić wartość `None`.

##### Przykład:

```python
input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

print(message(input_dict))
```

##### Wynik:
```plaintext
In Star Wars, Han Solo is a smuggler.
```
```python
input_dict = {
    "name": "Bilbo Baggins",
    "role": "burglar"
}

print(message(input_dict))
```

##### Wynik:
```plaintext
None
```




# def message(input_dict, movie=None):
#     print("In movie, name is a role.")
#     keys = {"movie", "name", "role"}
#    # input_dict = {"movie":, "name":, "role:"}
#     if set(input_dict.keys()) == keys:
#         return f"In {input_dict['movie']}, {input_dict['name']} is a {input_dict['role']}."
#     else:
#         return None
#
#   #  print(f"In {movie}, {name} is a {role}.")
#
#
#
#     input_dict = {
#         "name": "Han Solo",
#         "role": "smuggler",
#         "movie": "Star Wars"
#     }
#     print(message(input_dict))

#----------------------------------------------------------------------

def message(actor):
    # if "name" not in actor:
    #     return None
    # if "role" not in actor:
    #     return None
    # if "movie" not in actor:
    #     return None

    # for key in ("name", "role", "movie"):
    #     if key not in actor:
    #         return None

    if set(actor.keys()) != {"name", "role", "movie"}:
        return None

    return "In %(movie)s, %(name)s is a %(role)s." % actor

input_dict = {
    "name": "Han Solo",
    "role": "smuggler",
    "movie": "Star Wars"
}

# In Star Wars, Han Solo is a smuggler.
print(message(input_dict))

input_dict = {
    "name": "Bilbo Baggins",
    "role": "burglar"
}

# None
print(message(input_dict))





IMPOROTWANIE funkcji
from functions import quadratic_function
print(quadratic_function(0, 1, 2, 3))

from math_tools.functions  import quadratic_function   #folder.plik.py z funkcja
print(quadratic_function(1, 1, 2, 3))





## Zadanie 1
# Napisz funkcję `make_tuple`, która przyjmie cztery parametry: `a`, `b`, `c` i `d`. Niech parametry `c` i `d`
# bedą opcjonalne i ich standardowe wartości będą wynosiły odpowiednio 3 i 4. Zwróć krotkę czterech elementów,
# której kolejnymi elementami będą wartości parametrów.

def make_tuple(a, b, c="3" ,d="4"):
    tupla = []
    for i in (a, b ,c , d):
        tupla.append(i)
    return tupla


krotka = 2, 4.5, "tekst"
print(krotka)
krotka = tuple(range(1,11))
print(krotka)
lista = list(range(10,0,-1))
krotka = tuple(lista)
print(krotka)



a = make_tuple("mama", "tata")
print(a)

a = make_tuple(0, 0, 0, 0)

print(a)





## Zadanie 2

Napisz funkcję `find_first_and_last`, która przyjmie listę lub krotkę. Następnie zwróć krotkę,
która będzie zawierać pierwszy i ostatni element parametru.



def find_first_and_last(a, b, c, d):
    # liczba = [0]
    # for i in (a, b, c, d):
    #     liczba = [i+1]
    liczba = (a, b, c , d)
    return print(liczba[0], liczba[-1])

print (find_first_and_last(1,2,3,4))




## Zadanie 3

Napisz funkcję `format_date`, która przyjmie 3 parametry:

* `day`: dzień,
* `month`: miesiąc,
* `year`: rok.

Funkcja powinna sprawdzić, czy data jest poprawna: 
* miesiąc powinen być w granicach (1, 12),
* dzień nie może być większy od 30 - 31 (lub 28 w przypadku lutego, pomiń sprawdzanie lat przestępnych).

Jeśli któryś z warunków będzie niezgodzny z kalendarzem, funkcja ma zwrócić `None`.  

Funkcja powinna zwrócić sformatowany łańcuch tekstowy w formacie "dzień miesiąc rok".


def format_date(day, month, year):

    if day in range (1, 31) and month in range (1, 12):
        if month == 1: month = "styczen"
        elif month == 2: month = "luty"
    else:
        return

    return print(day, month, year)



d = format_date(12, 2, 2017)
print(d)

d = format_date(12, 13, 2017)
print(d)





## Zadanie 4

Napisz funkcję `find_boundaries`, która przyjmie listę liczb. 
Funkcja powinna zwrócić krotkę z najmniejszą i największą liczbą w zestawie. 
Jeśli na liście będzie element, nie będący liczbą, powinien zostać zignorowany. 
W przypadku wprowadzenia pustej listy, funkcja powinna zwrócić `None`.



def find_boundaries(elements):
    converted =  tuple(i for i in elements)
    #for i in number:
    #list.append(elements)
    #return tuple(list)
    print(type(converted))
  #  j = 0
   # for j in elements:

         #   return f"{min(elements)}, {max(converted)}"


    print("Zmieniono na tuple:",converted)

    return f"{min(converted)}, {max(converted)}"



# def convert(list):
#     return tuple(i for i in list)
# # Driver function
# list = [1, 2, 3, 4]
# print(convert(list))

b = find_boundaries([1, 5, 2, 3.5, -1])
print(b)
#(-1, 5)
b = find_boundaries([0, 2.5, "a kuku!", 10])
print(b)
#(0, 10)





## Zadanie 5

Napisz funkcję `censor`, która przyjmie jako parametr dowolnie długi łańcuch tekstowy. Następnie:

* rozbije łańcuch tekstowy na listę wyrazów,
* sprawdzi, czy nie znajdują się w nim słowa niedozwolone,
* jeśli tak -- zamieni je na cztery gwiazdki (`****`)
* ponownie połączy listę w string i zwróci wartość.
##### Słowa niedozwolone:
*Java*, *C#*, *Ruby*, *PHP*. 
(zwróć uwagę na wielkość znaków np. 'PhP' **nie** powinno być ocenzurowane)

def censor(text):
    words = []
    for word in text.split():
        if word in ("Java", "C#", "Ruby", "PHP"):
            words.append("*" * len(word))
        else:
            words.append(word)
    return " ".join(words)
print(censor("Java is the best, but PHP is the bestest!") )
# **** is the best, but **** is the bestest!






## Zadanie 6

Napisz funkcję `check_palindrome`, która pobierze jeden wyraz i sprawdzi, czy jest palindromem. 
Funkcja powinna zwracać `True`, jeśli łańcuch jest palindromem, `False`, jeśli nie jest.

def check_palindrome(word):
    return word == word[::-1]



palindrome = check_palindrome("kajak")
if palindrome:
    print("Yes")
else:
    print("No")
palindrome = check_palindrome("tak")
if palindrome:
    print("Yes")
else:
    print("No")
############################################################################
x = "malayalam"
w = ""
for i in x:
    w = i + w

if (x == w):
    print("Yes")
else:
    print("No")






OBSLUGA WYJATKOWOBSLUGA WYJATKOWOBSLUGA WYJATKOWOBSLUGA WYJATKOWOBSLUGA WYJATKOWOBSLUGA WYJATKOWOBSLUGA WYJATKOWOBSLUGA WYJATKOWOBSLUGA WYJATKOW BLEDOW


## Zadanie 2

W pliku **exercise2.py** znajdziesz prostą zgadywankę: komputer losuje liczbę od 1 do 10, po czym każe Ci ją zgadnąć. 
Przeanalizuj kod. Uruchom program. Spróbuj wpisać błędną daną i zobacz, jak w takiej sytuacji zachowuje się program. 

Popraw kod tak, aby po wpisaniu nieprawidłowej wartości nie zakończył działania komunikatem błedu, 
ale poinformował użytkownika o błędzie i kontynuował działanie. 

*Podpowiedź: Zobacz jaki wyjątek jest zgłaszany i odpowiednio go obsłuż.* 


from random import randint

guessed = False
rnd = randint(1, 2)

while not guessed:
    try:
        str_num = input("Podaj liczbę:")
        num = int(str_num)
        if num == rnd:
           print("Brawo!")
           guessed = True
        else:
           print("Pudło!")

    except ValueError:
        print('Błąd nie podałeś liczby!!!')

# while not guessed:
#
#         str_num = input("Podaj liczbę:")
#       try:
#         num = int(str_num)
#       except ValueError:
#           print('Błąd nie podałeś liczby!!!')
#       else:
#         if num == rnd:
#            print("Brawo!")
#            guessed = True
#         else:
#            print("Pudło!")
#




## Zadanie 3

Napisz funkcję `divide`, która przyjmie dwa argumenty: `a` i `b`. Muszą być to liczby naturalne. 
Funkcja ma działać następująco:

* ma sprawdzić, czy `a` i `b` to liczby,
* ma obsłużyć problem dzielenia przez zero.

Oba powyższe przypadki muszą być obsłużone przez wychwytywanie wyjątków.

Jeśli któryś z powyższych (nieprawidłowych) przypadków nie zostanie spełniony, funkcja ma zwrócić `None`.



def divide(a, b):
    try:
        return a/b
    except (ZeroDivisionError, TypeError):
        return None



a  = input('Podaj liczbe:')
b  = input('Podaj liczbe:')


print(divide(a, b))


## Zadanie 4

Napisz funkcję `phone`, która przyjmie parametr `number`, który oznacza numer telefonu. 
Funkcja ma sprawdzić, czy podany numer znajduje się na liście numerów (wymyśl jakieś). 
Jeśli tak – niech zwróci numer podany w parametrze. Jeśli nie - musi zwrócić wyjątek typu `Exception` z komentarzem 
`Nie ma takiego numeru!`.


def phone(number):
    known_numbers = (
        "555-123-456",
        "123-456-789",
        "333-555-444"
    )
    if number in known_numbers:
        return number
    raise Exception(f"Nie ma takiego numeru: {number}")
print(phone("123-456-789"))
print(phone("333-456-789"))


# def phone(number):
#     number = str(number)
#     number_list = ["1111","22222","3333333","444444"]
#     try:
#         find_index = number_list.index(number)
#         print(number)
#         return number
#     except Exception:
#         print("Nie ma takiego numeru")
#
# phone("1111")

# phone_book = (12121, 2121)
# def phone(number):
#     try:
#         num = number in phone_book
#     except Exception:
#         print("Nie ma takeigo numeru")
#     else:
#         print(num)
#
# print (phone(12121))
# print (phone(3131))









WARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATY
WARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATYWARSZTATY


## Zadanie 1

Napisz funkcję `random_average(n)`, która wylosuje `n` liczb naturalnych od 1 do 100, zsumuje je, 
po czym zwróci średnią arytmetyczną z tych liczb.

Ze względu na konstrukcję testów automatycznych użyj w zadaniu poniższej formy importu funkcji `randint`:
# ```python
# import random
# ```
# a następnie w kodzie używaj konstrukcji:

# ```python
# random.randint()
# ```

import random

def random_avarage(n):
    suma = 0

    for i in range (0, n):
        losowa_liczba = random.randint(1, 100)
        suma += losowa_liczba
        print("id losu:", i + 1," wynosi:", losowa_liczba)
    print("Suma z", n," wynosi:", suma)
    return suma / n if n != 0 else None #wyrazenie warunkowe if expression

print ("Srednia z tych liczb to:", random_avarage(3))







##### Zasady walidacji numeru PESEL

PESEL składa się z 11 cyfr, z czego ostatnia jest cyfrą kontrolną. Aby sprawdzić PESEL, należy:

* pierwsze dziesięć cyfr pomnożyć przez odpowiednią _wagę_, 
* otrzymane iloczyny zsumować,
* sumę podzielić modulo 10,
* wynik dodawania odjąć od 10, jeśli wynik będzie wynosił 10, należy wziąć 0.

Jeżeli wynik powyższej operacji będzie równy ostatniej cyfrze numeru PESEL, cały numer jest poprawny.

##### Wagi:

`1 3 7 9 1 3 7 9 1 3`


##### Przykład:
Chcemy sprawdzić PESEL 44051401358. Zgodnie z procedurą, sprawdzamy dziesięć pierwszych cyfr, 
ostatnia (8) jest cyfrą kontrolną.

|         |   |    |   |    |   |    |   |   |   |    |
|---------|---|----|---|----|---|----|---|---|---|----|
| **cyfra**   | 4 | 4  | 0 | 5  | 1 | 4  | 0 | 1 | 3 | 5  | 
| **waga**  | 1 | 3  | 7 | 9  | 1 | 3  | 7 | 9 | 1 | 3  |
| **iloczyn** | 4 | 12 | 0 | 45 | 1 | 12 | 0 | 9 | 3 | 15 |

Sumujemy iloczyny: 4 + 12 + 0 + 45 + 1 + 12 + 0 + 9 + 3 + 15 = **101**

Sumę dzielimy modulo 10: 101 % 10 = **1**

Wynik dzielenia modulo odejumemy od 10: 10 - 1 = **9**.

Podana w PESEL-u cyfra kontrolna wynosi **8**, zatem PESEL jest błędny.



def validate_pesel(text):
    if not isinstance(text, str):
        raise TypeError(f"Expected a string but got {type(text).__name__}")
    if not text.isdigit():
        raise ValueError("Expected a string with digits")
    if len(text) != 11:
        raise ValueError("PESEL must be exactly 11 digits long")

    weights = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
    digits = [int(x) for x in text]  # list(map(int, text))

    control = 10 - sum([int(x)*y for x, y in zip(digits[:10], weights)]) % 10

    if control == 10:
        control = 0

    return control == digits[-1]


non_text = 264736478
non_digits = "26e73,478"
too_short = "1234"
too_long = "123456789000"
bad_pesel = "44051401358"
ok_pesel = "90070543671"

# validate_pesel(non_text)
# validate_pesel(non_digits)
# validate_pesel(too_short)
# validate_pesel(too_long)
print(validate_pesel(bad_pesel))
print(validate_pesel(ok_pesel))

validate_pesel(bad_pesel)






# Napisz funkcję `d6(num)`, która zasymuluje rzuty kostką sześcienną. `num` to parametr,
# który oznacza liczbę rzutów kostką. Funkcja ma zwrócić sumę wyrzuconych oczek.

import random

def d6(num):
    suma = 0
    for i in range (num):
        liczba = random.randint(1,6)
        print('Rzut nr:', i+1, "wynosi:",liczba)
        suma += liczba

    return print("Suma:",suma)

num = 6
print(d6(num))




#ZADANIE1
Warsztat: Gra w zgadywanie liczb.

Napisz prostą grę w zgadywanie liczb. Komputer musi wylosować liczbę w zakresie 1 – 100. Następnie:

    Zadać pytanie: "Guess the number: " i pobrać liczbę z klawiatury.
    Sprawdzić, czy wprowadzony napis, to rzeczywiście liczba i w razie błędu wyświetlić komunikat "It's not a number!", po czym wrócić do pkt. 1
    Jeśli liczba podana przez użytkownika jest mniejsza niż wylosowana, wyświetlić komunikat "To small!", po czym wrócić do pkt. 1.
    Jeśli liczba podana przez użytkownika jest większa niż wylosowana, wyświetlić komunikat "To big!", po czym wrócić do pkt. 1.
    Jeśli liczba podana przez użytkownika jest równa wylosowanej, wyświetlić komunikat "You win!", po czym zakończyć działanie programu.

Przykład:
Guess the number: cześć
It's not a number!
Guess the number: 50
To small!
Guess the number: 75
To big!
Guess the number: 63
You win!
    Pamiętaj, aby obsłużyć odpowiednie błędy!



from random import randint

randomized = randint(1, 100)

print("GAME GUESS NUMBER 1-100\n", end="")

def guess(goal):
    number_int = -1
    while number_int > 0 and number_int < 100 or goal == True:
        try:

            number = input("Guess the number: ")
            number_int = int(number)
            goal = False
            if number_int < randomized:
                print("Too samll")
            elif number_int > randomized:
                print("Too big")
            else:
                print("You win")

        except ValueError:
            print("It's not a number!")
    else:
        print("Number out of range")
        print(guess(True))


print(guess(True))


#######################################OK##################################################
#
# from random import randint
# print("GRA W ZGADYWANIE LICZB 1-100\n", end="")
#
# #number = -1
# randomized = randint(1, 100)
# trafiona = False
#
#
# while not trafiona:
#     try:
#         number = input("Guess the number: ")
#         number = int(number)
#
#         if number > 0 and number < 100:
#
#
#             if number < randomized:
#                 print("Too samll")
#             elif number > randomized:
#                 print("Too big")
#             else:
#                 trafiona = True
#                 print("You win")
#
#
#         else:
#              print("Podales liczbe z poza zakresu")
#
#
#     except ValueError:
#         print("It's not a number!")











#ZADANIE2
Symulator LOTTO
Warsztat: Symulator LOTTO.

Jak zapewne wiesz, LOTTO to gra liczbowa polegająca na losowaniu 6 liczb z zakresu 1 – 49. 
Zadaniem gracza jest poprawne wytypowanie losowanych liczb. 
Nagradzane jest trafienie 3, 4, 5 lub 6 poprawnych liczb.

Napisz program, który:

    zapyta o typowane liczby, przy okazji sprawdzi następujące warunki:
        czy wprowadzony ciąg znaków jest poprawną liczbą,
        czy użytkownik nie wpisał tej liczby już poprzednio,
        czy liczba należy do zakresu 1-49,
    po wprowadzeniu 6 liczb, posortuje je rosnąco i wyświetli na ekranie,
    wylosuje 6 liczb z zakresu i wyświetli je na ekranie,
    poinformuje gracza, ile liczb trafił.





    from random import randint

lotto = [] #numbers randomized in lotto
choosen = [] #numbers choosen by player

#i,j - counters

def lotto_def(i = 0):

    # for i in range(6):
    while len(lotto) != 6:  # losuje tak dlugo az lista lotto nie bedzie dluga do 6
        i = i + 1
        rand_num = randint(1, 49)

        # print(i, "wylosowana:", rand_num) #sprawdzenie ile liczb musial wylosowac i jakich aby sie nie powtarzaly
        if rand_num not in lotto:
            lotto.append(rand_num)
    return sorted(lotto)

def shooting_def(i = 0):

    while len(choosen) != 6:  # losuje tak dlugo az lista wybranych liczb nie bedzie dluga do 6
        try:
            i = i + 1

            print("Provide", i, "number:", end=" ")
            number = int(input())

            if number in choosen:
                print("This number exist, try with another!")
                i = i - 1
            elif number < 1 or number > 49:
                print("This number out of range, try with another!")
                i = i - 1
            else:
                choosen.append(number)
        except ValueError:
            print("Please provide int number")
            i = i - 1
    return sorted(choosen)

def main_lotto_def():
    i = 0

    for j in range(6):



        if choosen[j] in lotto:
            j += 1
            print("You hit:", j)
            i += 1
    if i >= 3 and i <= 6:
        print("BRAVO, You hit in total:", i, "numbers")
    else:
        print("Unfourtenally its too less. You hit in total:", i)
    return ""

print("GAME LOTTO, Please Choose 6 numbers from 1 - 49")
print("Numbers of user:", shooting_def())
print("Numbers radomized by lotto:", lotto_def())
print(main_lotto_def())











#ZADANIE3
Gra w zgadywanie liczb 2
Warsztat: Gra w zgadywanie liczb 2

Odwróćmy teraz sytuację z pierwszego zadania: ("Gra w zgadywanie liczb"). Niech użytkownik pomyśli sobie liczbę z zakresu 1-1000, a komputer będzie zgadywał. Zrobi to maksymalnie w 10 ruchach (pod warunkiem, że gracz nie będzie oszukiwał).

Zadaniem gracza będzie udzielanie odpowiedzi "To small", "To big", "You win".

Do tego warsztatu dołączony jest schemat blokowy algorytmu. Zaimplementuj go w Pythonie. flowchart



print("Imagine number between 0 and 1000!")


def guess_def(mini=0, maxi=1000, j=1):
    guess = int((maxi - mini) / 2) + mini
    print("\n")

    # Proba dodania mozliwosci poprawy komendy przy jej blednym wprowadzeniu. W innym przypadku konyczl program
    while j <= 10:

        print(j, "chance ---> Guess: " + str(guess))

        answer = input("Available answers: \n - Correct \n - Too big \n - To small\nType here: ")

        if j < 10 and answer == "Correct" or "Too big" or "Too small":
            print(j + 1)

            if answer == "Correct" and j < 10:
                print("You WIN!!!")
                break
            elif answer == "Too big" and j < 10:
                j += 1
                print("Too much?")
                guess_def(mini, guess, j)
            elif answer == "Too small" and j < 10:
                j += 1
                print("Too less?")
                guess_def(guess, maxi, j)
            elif j == 9:
                print("Koniec Szans\n")
                j += 1

            else:
                if j == 10:
                    print("DO NOT CHEAT!!!\n")
                    break
    else:
        print("KONIEC")


if __name__ == '__main__':
    guess_def(0, 1000, )

###################MY SIMPLER:
# def guess_def(mini = 0, maxi = 1000, j = 1, flag = True):
#     guess = int((maxi-mini)/2)+mini
#     print("\n")
#     print(j, "chance ---> Guess: " + str(guess))
#
#
#
#
#     answer = input("Available answers: \n - Correct \n - Too big \n - To small\nType here: ")
#     if answer == "Correct" or "Too big" or "Too small":
#
#         if answer == "Correct" and j < 10:
#             print("You WIN!!!")
#         elif answer == "Too big" and j < 10:
#             print("Too much?")
#             guess_def(mini, guess, j + 1)
#         elif answer == "Too small" and j < 10:
#             print("Too less?")
#             guess_def(guess, maxi, j + 1)
#         else:
#             print("Do not cheat! Try again!!!\n")


##########################ODP Z LMS CODERSLAB:
# def user_input():
# """Return proper value provided by user.
# :rtype: str
# :return: value provided by user from ["to small", "to big", "you win"]
# """
#   possible_input = ["to small", "to big", "you win"]
#     while True:
#         user_answer = input().lower()
#         if user_answer in possible_input:
#             break
#         print("Input is not in ['to small', 'to big', 'you win']")
#     return user_answer
#
#
#
# def guess_the_number():
#     """Main function for our program."""
#     print("Imagine number between 0 and 1000!")
#     print("Press 'Enter' to continue")
#     input()
#     min_number = 0
#     max_number = 1000
#     user_answer = ""
#     while user_answer != "you win":
#         guess = (max_number - min_number) // 2 + min_number
#         print(f"Your number is: {guess}")
#         user_answer = user_input()
#         if user_answer == "to big":
#             max_number = guess
#         elif user_answer == "to small":
#             min_number = guess
#     print("Hurra! I guess!")
#
# if __name__ == '__main__':
#     guess_the_number()










#ZADANIE5
Kostka do gry
Warsztat: Kostka do gry

W grach planszowych i papierowych RPG używa się wielu rodzajów kostek do gry, nie tylko tych dobrze znanych, sześciennych. Jedną z popularniejszych kości jest np. kostka dziesięciościenna, a nawet stuścienna! Ponieważ w grach kośćmi rzuca się często, pisanie za każdym razem np. "rzuć dwiema kostkami dziesięciościennymi, a do wyniku dodaj 20" byłoby nudne, trudne i marnowałoby ogromne ilości papieru. W takich sytuacjach używa się kodu "rzuć 2D10+20".

Kod takiej kostki wygląda następująco:
xDy+z

gdzie:

    y – rodzaj kostek, których należy użyć (np. D6, D10),
    x – liczba rzutów kośćmi; jeśli rzucamy raz, ten parametr jest pomijalny,
    z – liczba, którą należy dodać (lub odjąć) do wyniku rzutów (opcjonalnie).

Przykłady:

    2D10+10: 2 rzuty D10, do wyniku dodaj 10,
    D6: zwykły rzut kostką sześcienną,
    2D3: rzut dwiema kostkami trójściennymi,
    D12-1: rzut kością D12, od wyniku odejmij 1.

Napisz funkcję, która:

    przyjmie w parametrze taki kod w postaci łańcucha znaków,
    rozpozna wszystkie dane wejściowe:
        rodzaj kostki,
        liczbę rzutów,
        modyfikator,
    jeśli podany ciąg znaków jest niepoprawny, zwróci odpowiedni komunikat,
    wykona symulację rzutów i zwróci wynik.

Typy kostek występujące w grach: D3, D4, D6, D8, D10, D12, D20, D100.


from random import randint

dism = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")


def game_cube(code):
###wyciagniecie pierwszej wartosci mnoznika
    print(type(code))
    print(code[0])
    if code[0].isdigit():
        x = int(code[0])
    else:
        x = 1

    y = []
    if code[1] =="D":
        y.append(code[1])
        y.append(code[2])
        d = int(y[1]) #ktory indeks ma D?


    wylosowana = randint(1, d)


    print(y) #rozdzielona kostak D6

    for i in range(len(code)):
        print(code[i], end="")

    if "+" in code:
        znak = code.split("+")
        koniec = x * wylosowana + int(znak[1])
    else:
        znak = code.split("-")
        koniec = x * wylosowana - int(znak[1])

    print(znak)

    #koniec = x * wylosowana

    #for i in code:
   #     print(code.index(i), code.join(","))


    print("Indeks D:", code.index("D"))
    print("Składowe---> Mnoznik:", x, "Kostka:",d, "wylosowana:", wylosowana, "dopelniacz:", znak[1])
    print("Konicowy wynik:", koniec)




print("BONES:")
letters = "2D6+5"
print(game_cube(letters))


# #######################################CODERS_LAB##########################################

# import random
#
# POSSIBLE_DICES = (
#
#     "D100",
#
#     "D20",
#
#     "D12",
#
#     "D10",
#
#     "D8",
#
#     "D6",
#
#     "D4",
#
#     "D3"
#
# )
#
#
# def roll_the_dice(dice_code):
#     """
#
#     Calculate dice roll from dice pattern.
#
#
#
#     :param str dice_code: dice pattern ex. `7D12-5`
#
#
#
#     :rtype: int, str
#
#     :return: dice roll value for proper dice pattern, `Wrong Input` text elsewhere
#
#     """
#
#     for dice in POSSIBLE_DICES:
#
#         if dice in dice_code:
#
#             try:
#
#                 multiply, modifier = dice_code.split(dice)
#
#             except ValueError:
#
#                 return "Wrong Input"
#
#             dice_value = int(dice[1:])
#
#             break
#
#     else:
#
#         return "Wrong Input"
#
#     try:
#
#         multiply = int(multiply) if multiply else 1
#
#     except ValueError:
#
#         return "Wrong Input"
#
#     try:
#
#         modifier = int(modifier) if modifier else 0
#
#     except ValueError:
#
#         return "Wrong Input"
#
#     return sum([random.randint(1, dice_value) for _ in range(multiply)]) + modifier
#
#
# if __name__ == '__main__':
#     print(roll_the_dice("2D10+10"))
#
#     print(roll_the_dice("D6"))
#
#     print(roll_the_dice("2D3"))
#
#     print(roll_the_dice("D12-1"))
#
#     print(roll_the_dice("DD34"))
#
#     print(roll_the_dice("4-3D6"))











import random


POSSIBLE_DICES = (
    "D100",
    "D20",
    "D12",
    "D10",
    "D8",
    "D6",
    "D4",
    "D3"
)


def roll_the_dice(dice_code):
    """
    Calculate dice roll from dice pattern.
    :param str dice_code: dice pattern ex. `7D12-5`
    :rtype: int, str
    :return: dice roll value for proper dice pattern, `Wrong Input` text elsewhere
    """
    for dice in POSSIBLE_DICES:
        if dice in dice_code:
            try:
                multiply, modifier = dice_code.split(dice)
            except ValueError:
                return "Wrong Input"
            dice_value = int(dice[1:])
            break
    else:
        return "Wrong Input"

    try:
        multiply = int(multiply) if multiply else 1
    except ValueError:
        return "Wrong Input"

    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return "Wrong Input"

    return sum([random.randint(1, dice_value) for _ in range(multiply)]) + modifier


if __name__ == '__main__':
    print(roll_the_dice("2D10+10"))
    print(roll_the_dice("D6"))
    print(roll_the_dice("2D3"))
    print(roll_the_dice("D12-1"))
    print(roll_the_dice("DD34"))
    print(roll_the_dice("4-3D6"))


def calculate_points(points):
    """Calculate points.
    :param int points:
    :rtype: int
    :return: new_points
    """
    roll = roll_the_dice("2D6")
    if roll == 7:
        points //= 7
    elif roll == 11:
        points *= 11
    else:
        points += roll
    return points


def game_2001():
    """2001 game."""
    user_points = 0
    computer_points = 0

    input("Press ENTER to roll the dice")
    user_points += roll_the_dice("2D6")
    computer_points += roll_the_dice("2D6")

    while user_points < 2001 and computer_points < 2001:
        print(f"User points: {user_points}\nComputer points: {computer_points}")
        input("Press ENTER to roll the dice")
        user_points = calculate_points(user_points)
        computer_points = calculate_points(computer_points)

    print(f"User points: {user_points}\nComputer points: {computer_points}")
    if computer_points > user_points:
        print("Computer win!")
    elif user_points > computer_points:
        print("User win!")
    else:
        print("Draw")


if __name__ == '__main__':
    game_2001()