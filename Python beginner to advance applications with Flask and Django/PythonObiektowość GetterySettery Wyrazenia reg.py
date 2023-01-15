# Zadanie 1 – zadanie rozwiązywane z wykładowcą
#
# Miecze świetlne w świecie Gwiezdnych Wojen mogą mieć następujące kolory *.
#
#     niebieski (jasna strona mocy),
#     zielony (jasna strona mocy),
#     fioletowy (jasna strona mocy),
#     czerwony (ciemna strona mocy).
#
# Utwórz klasę Lightsaber definiującą miecz świetlny. W metodzie __init__ dodaj atrybut:
#
#     _color, który nie powinien być używany na zewnątrz klasy
#     nadpisz metodę __str__() tak, by zwracała napis: "Lighstaber: kolor, force: jasna|ciemna".
#
# Niech konstruktor przyjmuje parametr color, wartość tego parametru przypisz do atrybutu _color, stronę mocy wyświetl dynamicznie na podstawie koloru.
#
# * bierzemy pod uwagę filmy z aktorami, epizody I – VIII.
#
# Podpowiedź: Dla ułatwienia możesz utworzyć stałą, przechowującą w krotce kolory dla ciemnej i jasnej strony mocy.
#
#

class Lightsaber:
    CIEMNE_KOLORY = ("czerwony",)

    def __init__(self, color):
        self._color = color

    def __str__(self):
        # moc = "ciemna" if self._color in Lightsaber.CIEMNE_KOLORY else "jasna"

        if self._color in Lightsaber.CIEMNE_KOLORY:
            moc = "ciemna"
        else:
            moc = "jasna"

        return f"Lighstaber: {self._color}, force: {moc}"


ls1 = Lightsaber("niebieski")
ls2 = Lightsaber("czerwony")

print(ls1)
print(ls2)



# Zadanie 2
#
# Utwórz setter i getter (@property i odpowiednio @własność.setter) o nazwie color, które zwrócą i nastawią
# prywatną własność _color. Sprawdź, czy podany kolor znajduje się na liście legalnych kolorów. Jeśli nie – wyrzuć wyjątek ValueError
# z komentarzem "Bad lightsaber color".
#
# Zmodyfikuj odpowiednio metodę __str__().


class Lightsaber:
    JASNE_KOLORY = ("niebieski", "zielony", "fioletowy")
    CIEMNE_KOLORY = ("czerwony",)

    def __init__(self, new_color):
        self.color = new_color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, nowy_kolor):
        if nowy_kolor in Lightsaber.JASNE_KOLORY or nowy_kolor in Lightsaber.CIEMNE_KOLORY:
            self._color = nowy_kolor
        else:
            raise ValueError(f"Unknown lightsaber color: {nowy_kolor}")

    def __str__(self):
        if self.color in Lightsaber.CIEMNE_KOLORY:
            moc = "ciemna"
        else:
            moc = "jasna"

        return f"Lighstaber: {self.color}, force: {moc}"


ls1 = Lightsaber("niebieski")
ls2 = Lightsaber("czerwony")

print(ls1)
print(ls2)

ls3 = Lightsaber("ciemna fuksja")
print(ls3)


# Zadanie 3
#
#     Utwórz własność wirtualną (@property), force_side, która przyjmie odpowiednią wartość, zależnie od wartości własności _color:
#         dla kolorów niebieskiego, zielonego i fioletowego – "light",
#         dla koloru czerwonego – "dark".
#
#     Zmodyfikuj odpowiednio metodę __str__().



class Lightsaber:
    JASNE_KOLORY = ("niebieski", "zielony", "fioletowy")
    CIEMNE_KOLORY = ("czerwony",)

    def __init__(self, color):
        self._color = color



    @property
    def force_side(self):
        if self._color in Lightsaber.CIEMNE_KOLORY:
            _color = "dark"
        else:
            _color = "light"
        return _color




    def __str__(self):


        return f"Lighstaber: {self._color}, force: {self.force_side}"


ls1 = Lightsaber("niebieski")
ls2 = Lightsaber("czerwony")

print(ls1)
print(ls2)

ls3 = Lightsaber("fioletowy")
print(ls3)



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



#METODY STATYCZNE I DZIEDZICZENIE

        # Zadanie 1 – zadanie rozwiązywane z wykładowcą
#
# Stwórz klasę AdvancedCalculator, która będzie dziedziczyła po klasie Calculator (klasa stworzona wczoraj). Do nowej klasy dopisz:
#
#     Atrybut klasowy (zmienną klasową) PI, który będzie miał przypisaną wartość 3.14159265.
#     Statyczną (dodaj odpowiedni dekorator) metodę compute_circle_area(r) która będzie zwracała pole koła. Ta metoda nie będzie dopisywać obliczeń do tablicy (napisz w komentarzu, dlaczego nie może tego robić).


class Calculator:
    def __init__(self):
        self.historia = []

    def add(self, num1, num2):
        result = num1 + num2
        log = f"added {num1} to {num2} got {result}"
        self.historia.append(log)
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.historia.append(f"multiplied {num1} with {num2} got {result}")
        return result

    def print_operations(self):
        for linia in self.historia:
            print(linia)

class AdvancedCalculator(Calculator):
    PI = 3.14159265

    @staticmethod
    def compute_circle_area(r):
        return AdvancedCalculator.PI * r * r

print(AdvancedCalculator.compute_circle_area(10))

ac = AdvancedCalculator()
x = ac.add(6, 7)
r = ac.multiply(x, 10)
pole1 = ac.compute_circle_area(r)
pole2 = AdvancedCalculator.compute_circle_area(r)

ac.print_operations()
print(pole1, "=", pole2)









# Zadanie 2
#
# Zmień klasę BankAccount w taki sposób żeby konstruktor sam nadawał numer konta bankowego. Dla uproszczenia będziemy nadawać kolejne liczby całkowite zaczynając od jedynki. Zeby to zrobić:
#
#     Dodaj do klasy atrybut klasowy (zmienną klasową) next_acc_number.
#     Nastaw jego wartość na 1.
#     Zmodyfikuj metodę __init__ w taki sposób żeby nie przyjmowała numeru konta, tylko przypisywał wartość atrybutu next_acc_number do atrybutu number wewnątrz obiektu, a nastepnie zwiększała wartość atrybutu klasy next_acc_number o jeden.
#
# Przetestuj jak generowane są numery twoich kont.


class BankAccount:
    next_acc_number = 1


    def __init__(self):
        self.number = BankAccount.next_acc_number
        self.cash = 0.0
        BankAccount.next_acc_number += 1


    def deposit_cash(self, amount):
        if amount > 0:
            self.cash += amount



    def withdraw_cash(self, amount):
        if amount > 0:
            if amount > self.cash:
                print(f"You can not take more than: {self.cash}")
                memored_cash = self.cash
                self.cash -= self.cash
                return print(f"Hurra you deploy: {memored_cash }")
            else:
                self.cash -= amount
                return print (f"Hurra you deploy: {amount}")
        else:
            print(f"Yo can not get cash with minus amount")


    def print_info(self):
        print(f"BanckAccount {self.number} , have: {self.cash} cash")
        #return f"BanckAccount, {self.number} have: {self.cash}"



kowalski = BankAccount()
kowalski.print_info()

kowalski.deposit_cash(100)
kowalski.print_info()
kowalski.withdraw_cash(150)
kowalski.print_info()

kowalski.deposit_cash(300)
kowalski.print_info()
kowalski.withdraw_cash(50)
kowalski.print_info()
kowalski.withdraw_cash(-50)
kowalski.print_info()
zenek = BankAccount()
zenek.print_info()





# Zadanie 3
#
# Zajrzyj do pliku exercise_3.py. Znajdziesz tam klasę Person, która w konstruktorze przyjmuje dwa parametry: name i age, po czym ustawia odpowiednie atrybuty. Dopisz metodę klasową create_person(), która:
#
#     przyjmie dwa parametry: name – oznaczający imię i year_of_birth – oznaczający rok urodzenia,
#     na podstawie roku urodzenia, obliczy wiek osoby i zwróci obiekt klasy Person, z odpowiednimi wartościami.

# exercise3.py:
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return "{} is {} years old.".format(self.name, self.age)

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_person(cls, name, year_of_birth):
        age = date.today().year - year_of_birth
        return cls(name, age)

    def __str__(self):
        return "{} is {} years old.".format(self.name, self.age)

firstp = Person.create_person("Antek", 2000)
print(firstp)












#GETTERY I SETTERY

# Zadanie 1 – kostka (wykonywane z wykładowcą)
#
# Napisz klasę Dice, która będzie miała własność dice_type. W tej własności będziesz przechowywać liczbę ścianek kostki. Kostka może być 3, 4, 6, 8, 10, 12, 20 lub 100-ścienna. Pamiętaj o sprawdzeniu, czy wartość parametru jest właściwa. Jeśli nie, wyrzuć błąd: ValueError.
#
# Napisz metodę roll(), która wylosuje liczbę z zakresu 1..dice_type, czyli zasymuluje rzut kostką.

import random

class Dice:
    KOSTKA_CACY = (3, 4, 6, 8, 10, 12, 20, 100)

    def __init__(self, dice_type):
        if dice_type not in Dice.KOSTKA_CACY:
            raise ValueError(f"Nieznany typ kości: {dice_type}")
        self.dice_type = dice_type

    def roll(self):
        return random.randint(1, self.dice_type)

d6 = Dice(6)
d20 = Dice(20)

for _ in range(5):
    print(d6.roll())

print("-----------------")

for _ in range(5):
    print(d20.roll())

print("-----------------")

d99 = Dice(99)



# Zadanie 2 – kostka jako iterator (wykonywane z wykładowcą)
#
# Przerób klasę Dice tak, aby dało się po niej iterować. W tym celu:
#
#     dodaj atrybut number_of_rolls, odpowiadający ilości rzutów.
#     dodaj odpowiednie metody, tak aby przy iterowaniu została zwrócona liczba rzutów odpowiadająca wcześniej dodanemu atrybutowi: number_of_rolls
#
# Przykład użycia:
#
# for throw in Dice(dice_type=6, number_of_rolls=3):
#
#     print(throw)
#
# Przykładowy wynik:
#
# 4
#
# 5
#
# 2

import random

class Dice:
    KOSTKA_CACY = (3, 4, 6, 8, 10, 12, 20, 100)

    def __init__(self, dice_type, number_of_rolls):
        if dice_type not in Dice.KOSTKA_CACY:
            raise ValueError(f"Nieznany typ kości: {dice_type}")
        self.dice_type = dice_type
        self.number_of_rolls = number_of_rolls

    def roll(self):
        return random.randint(1, self.dice_type)

    def __iter__(self):
        self.__roll_counter = 0
        return self

    def __next__(self):
        if self.__roll_counter >= self.number_of_rolls:
            raise StopIteration
        self.__roll_counter += 1

d6 = Dice(6, 5)
d20 = Dice(20, 5)

for roll in d6:
    print(roll)

print("-----------------")

for roll in d20:
    print(roll)



    # Zadanie 3 – generator
#
# Napisz funkcję generatora roll_the_dice(n), która:
#
#     przyjmie jeden parametr n - liczbę całkowitą,
#     wygeneruje ("zwróci") tyle rzutów kością ile zostało przekazane w parametrze n.

import random

class Dice:

    @staticmethod
    def roll_the_dice(n):
        for i in range(n):
            yield random.randint(1, 20)

d1 = Dice.roll_the_dice(5)
for roll in d1:
    print(roll)



# import random
#
# class Dice:
#     KOSTKA_CACY = (3, 4, 6, 8, 10, 12, 20, 100)
#
#     def __init__(self, dice_type):
#         if dice_type not in Dice.KOSTKA_CACY:
#             raise ValueError(f"Nieznany typ kości: {dice_type}")
#         self.dice_type = dice_type
#
#     def roll(self):
#         return random.randint(1, self.dice_type)
#
# def roll_the_dice(dice, n):
#     for _ in range(n):
#         yield dice.roll()
#
# rolls1 = roll_the_dice(Dice(10), 5)
# rolls2 = roll_the_dice(Dice(8), 3)
#
# print(list(rolls1))
# print(list(rolls2))






# Zadanie 4 – piosenka
#
# Napisz funkcję generatora sing, która będzie zwracała kolejne linie pierwszej zwrotki piosenki „Wlazł kotek na płotek”.
#
# Wlazł kotek na płotek
#
# i mruga,
#
# ładna to piosenka,
#
# nie długa.
#
# Nie długa, nie krótka,
#
# lecz w sam raz,
#
# zaśpiewaj koteczku,
#
# jeszcze raz.

text = """Wlazł kotek na płotek
i mruga,
ładna to piosenka,
nie długa.
Nie długa, nie krótka,
lecz w sam raz,
zaśpiewaj koteczku,
jeszcze raz."""

def sing():
    # return text.splitlines()
    for line in text.splitlines():
        yield line

print(list(sing()))

# class Songs:
#     _SONG = [
#         "Wlazł kotek na płotek,",
#         "i mruga,",
#         "ładna to piosenka,",
#         "nie długa.",
#         "Nie długa, nie krótka,",
#         "lecz w sam raz,",
#         "zaśpiewaj koteczku,",
#         "jeszcze raz"
#     ]
#     def __init__(self):
#         pass
#
#     def sing(self):
#         for i in (len(Songs._SONG)):
#             yield print(Songs._SONG[i])
#
#
#
# singer1 = Songs.sing(Songs._SONG)




 



## Zadanie 2.

### Część 1

Napisz klasę `Product`, która w metodzie `__init__` przyjmie argumenty: `name`, `price` i zapisze je jako atrybuty produktu.

Dodatkowo `__init__` powinno w produkcie ustawiać niepowtarzalny atrybut `id`.

### Część 2

Napisz klasę `ShoppingCart`. Jej metoda `__init__` nie wymaga żadnych atrybutów (oprócz oczywiście `self`).

Metoda `__init__` powinna w instancji koszyka stworzyć:
 - pusty słownik `products` (jako atrybut). Kluczem w tym słowniku będą `id` produktów, a wartością całe produkty (instancje klasy `Product`).
 - pusty słownik `quantities` (jako atrybut). Kluczem będą `id` produktów, a wartością będzie liczba sztuk tego produktu w koszyku.

Klasa powinna mieć też nastepujące metody:

 - `add_product(product)` - metoda ta powinna dodawać nowy produkt do słownika `products` oraz uaktualnić ilość tego produktu w słowniku `quantities`.
 - `remove_product(product)` - metoda ta powinna usuwać produkt z koszyka (weź pod uwagę oba słowniki: `products` i `quantities`). Jeśli taki produkt nie był wcześniej zeskanowany, to ma nic nie robić.
 - `change_product_quantity(product, new_quantity)` - metoda ta powinna zmianiać ilość danego produktu w koszyku. Jeśli taki produkt nie był wcześniej zeskanowany, to ma nic nie robić. Jeśli `new_quantity` to zero, należy produkt usunąć z koszyka. Podanie ujemnego `new_quantity` powinno skutkować rzuceniem wyjątku `ValueError` z odpowiednim komentarzem.
 - `get_receipt()` - metoda tworząca paragon. Nie powinna sama drukować (używać `print(...)`), zamiast tego powinna zwrócić string. Przykład oczekiwanego paragonu znajdziesz na końcu zadania.

Wszystkie ww. argumenty o nazwie `product` powinny być instancją klasy `Product`.

### Część 3

Zmodyfikuj metodę `get_receipt()` tak, aby nadawała rabat -30% na łączną cenę za dany produkt, jeśli w koszyku są co najmniej 3 sztuki tego produktu.

### Przykład użycia:
# ```python
# >>> bread = Product('Chleb', 2.70)
# >>> ham = Product('Szynka', 8.40)
# >>> cheese = Product('Ser', 4.40)
# >>> chive = Product('Szczypiorek', 1.50)
# >>> pepper = Product('Papryka', 2.35)

# >>> print(bread.id)
# 1
# >>> print(pepper.id)
# 5
# >>> print(pepper.name)
# 'Papryka'
# >>> print(pepper.price)
# 2.35

# >>> cart = ShoppingCart()
# >>> print(cart.products)
# {}
# >>> print(cart.quantities)
# {}
# >>> print(cart.get_receipt())
# Suma: 0zł

# >>> cart.add_product(bread)
# >>> cart.add_product(bread)
# >>> cart.add_product(bread)
# >>> cart.add_product(pepper)
# >>> cart.add_product(chive)
# >>> cart.change_product_quantity(pepper, 2)
# >>> print(cart.products)
# {1: <...Product object...>, 5: <...Product object...>, 4: <...Product object...>}
# >>> print(cart.quantities)
# {1: 3, 5: 2, 4: 1}

# >>> cart.remove_product(bread)
# >>> print(cart.get_receipt())
# # Kolejność produktów może się różnić
# Papryka - ilość: 2, cena: 2.35zł, suma: 4.7zł
# Szczypiorek - ilość: 1, cena: 1.5zł, suma: 1.5zł

# Suma: 6.2zł
# ```


ROZWIAZANIE:


class Product:
    _next_id = 1

    @classmethod
    def get_next_id(cls):
        current = cls._next_id
        cls._next_id += 1
        return current

    def __init__(self, name, price):
        self._id = type(self).get_next_id()
        self.name = name
        self.price = price

    @property
    def id(self):
        return self._id


class ShoppingCart:
    def __init__(self):
        self.products = {}
        self.quantities = {}

    def _product_present(self, product):
        return product.id in self.products and product.id in self.quantities

    def add_product(self, product):
        if self._product_present(product):
            self.quantities[product.id] += 1
        else:
            self.products[product.id] = product
            self.quantities[product.id] = 1

    def remove_product(self, product):
        if self._product_present(product):
            del self.products[product.id]
            del self.quantities[product.id]

    def change_product_quantity(self, product, new_quantity):
        if self._product_present(product):
            if new_quantity == 0:
                self.remove_product(product)
            elif new_quantity < 0:
                raise ValueError(f"Nowa ilość musi być dodatnia: {new_quantity}")
            else:
                self.quantities[product.id] = new_quantity

    def get_receipt(self):
        receipt = []
        total = 0
        for item in self.products.values():
            quantity = self.quantities[item.id]
            effective_price = item.price if quantity < 3 else 0.7 * item.price
            subtotal = quantity * effective_price
            line = f"{item.name} - ilość: {quantity}, cena: {effective_price}zł, suma: {subtotal}zł"
            total += subtotal
            receipt.append(line)
        receipt.append(f"\nSuma: {total}zł")
        return "\n".join(receipt).strip()


if __name__ == "__main__":
    bread = Product('Chleb', 2.70)
    ham = Product('Szynka', 8.40)
    cheese = Product('Ser', 4.40)
    chive = Product('Szczypiorek', 1.50)
    pepper = Product('Papryka', 2.35)

    print(bread.id)
    print(pepper.id)
    print(pepper.name)
    print(pepper.price)

    cart = ShoppingCart()
    print(cart.products)
    print(cart.quantities)
    print(cart.get_receipt())

    cart.add_product(bread)
    cart.add_product(bread)
    cart.add_product(bread)
    cart.add_product(pepper)
    cart.add_product(chive)
    cart.change_product_quantity(pepper, 2)
    print(cart.products)

    print(cart.quantities)

    cart.remove_product(bread)
    print(cart.get_receipt())
    print(cart.get_receipt())























#WYRAZENIA REGULARNE



## Zadanie 1
Wykorzystując moduł `re`, napisz funkcję `check_dice`, która przyjmie jeden parametr w postaci napisu.
Funkcja powinna sprawdzić czy w przekazanym parametrze znajduje się prawidłowy wzór rzutu kostką.

Wzór rzutu kostką ma następującą postać:

```plaintext
<liczba rzutów kostką>d/D<liczba ścianek na kostce>+/-<modyfikator wyniku>
```

np.

`2d10+20` - dwa rzuty 10-ścienną kostką, do wyniku dodajemy 20

`6D3-10`- sześć rzutów 3-ścienną kostką, od wyniku odejmujemy 10

`D6` - jeden rzut 6-ścienną kostką

Funkcja powinna zwrócić `True` jeżeli w przekazanym parametrze znajduje się prawidłowy wzór, 
w innym wypadku funkcja powinna zwrócić `False`.

Przykłady działania funkcji:

`check_dice("8d7+10")` - zwraca `True`

`check_dice("8s7+10")` - zwraca `False`

`check_dice("8D7+10 abcdefghijk")` - zwraca `True`

`check_dice("8d-h")` - zwraca `False`






import re


# DICE_PATTERN = re.compile(r"^[0-9]*[dD][0-9]+([+-][0-9]+)?$")
DICE_PATTERN = re.compile(r"^\d*[dD]\d+([+-]\d+)?$")


def check_dice(dice_text):
    return DICE_PATTERN.match(dice_text.split()[0])


print(check_dice("2d10+20"), True)
print(check_dice("6D3-10"), True)
print(check_dice("D6"), True)
print(check_dice("10d6"), True)
print(check_dice("d10-"), False)
print(check_dice("8d7+10"), True)
print(check_dice("8s7+10"), False)
print(check_dice("8D7+10 abcdefghijk"), True)
print(check_dice("8d-h"), False)
















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





import random
import re


DICE_PATTERN = re.compile(r"^(\d*)D(\d+)([+-]\d+)?$")


POSSIBLE_DICES = (
    "100",
    "20",
    "12",
    "10",
    "8",
    "6",
    "4",
    "3"
)


def roll_the_dice(dice_code):
    """
    Calculate dice roll from dice pattern.
    :param str dice_code: dice pattern ex. `7D12-5`
    :rtype: int, str
    :return: dice roll value for proper dice pattern, `Wrong Input` text elsewhere
    """
    match = DICE_PATTERN.search(dice_code)
    if not match:
        return "Wrong Input"

    multiply, dice, modifier = match.groups()
    if dice not in POSSIBLE_DICES:
        return "Wrong Input"

    multiply = int(multiply) if multiply else 1
    dice = int(dice)
    modifier = int(modifier) if modifier else 0

    return sum([random.randint(1, dice) for _ in range(multiply)]) + modifier


if __name__ == '__main__':
    print(roll_the_dice("2D10+10"))
    print(roll_the_dice("D6"))
    print(roll_the_dice("2D3"))
    print(roll_the_dice("D12-1"))
    print(roll_the_dice("DD34"))
    print(roll_the_dice("4-3D6"))

#######################################BARTEK ZACZYNSKI SOLUTION
import re
from random import randint
def throw(expression):
    if match := re.match(r"(\d*)D(\d+)([+-]\d+)?", expression):
        num_throws, dice, offset = match.groups()
        if num_throws == "":
            num_throws = 1
        else:
            num_throws = int(num_throws)
        dice = int(dice)
        offset = 0 if offset is None else int(offset)
        return offset + sum(randint(1, dice) for _ in range(num_throws))
    else:
        raise ValueError("Nieprawidłowe wyrażenie")
print(throw("2D51+10"))
print(throw("D51+10"))
print(throw("D51"))





















## Zadanie 2

Otwórz plik `exercise_2.py`. Znajduje się w nim zmienna `text_to_search`, w której znajduje się tekst Szymona Askenazego 
(tekst pobrany z serwisu [wolnelektury.pl](https://wolnelektury.pl/katalog/lektura/uwagi-z-powodu-listu-polaka-do-ministra-rosyjskiego.html)).

Używając modułu `re` wykonaj następujące zadania:

1. Znajdź wszystkie wystąpienia wyrazu `autor`.
2. Znajdź wszystkie wystąpienia pasujące do wzoru `<ciąg_cyfr>%`.
3. Znajdź wszystkie wystąpienia wyrazów, które kończą się znakiem `.`.
4. Znajdź wszystkie wyrazy, w których znajduje się ciąg znaków `polski` (niezależnie od wielkości znaków).



import re

with open('text.txt', 'r') as fin:
    text_to_search = fin.read()

    print(re.findall(r"\s+autor[,.]?\s+", text_to_search, re.IGNORECASE))

    print(re.findall(r"[0-9]+%", text_to_search))
    print(re.findall(r"\d+%", text_to_search))

    # print(re.findall(r"[a-zA-Z]+\.", text_to_search))
    # \w -> [a-zA-Z0-9_] + litery specyficzne dla języka :)
    print(re.findall(r"\w{2,}\.", text_to_search))

    print(re.findall("\w*polski\w*", text_to_search, re.IGNORECASE))









PLIK.TXT:
Szymon Askenazy
Uwagi z powodu listu Polaka do ministra rosyjskiego

Ten List ciekawy i ważny mógłby samym swoim tytułem budzić pewną usprawiedliwioną nieufność. Nie, żeby Polak nie miał dziś nic do powiedzenia ministrowi rosyjskiemu. Owszem, miałby zawsze a szczególnie, dzisiaj do powiedzenia mu dosyć, zadużo. Ale musiałby powiedzieć samą prawdę, całą prawdę, bez układnego optymizmu dworaka i bez miłosiernej litanii petenta, bez ogródek, a i bez rozjęczenia, ze świadomością naszej krzywdy a i mocy naszej, przyjść nie z prośbą ani nawet ze skargą, lecz ze światłem i przestrogą. To rzecz bardzo trudna i chybić tu w treści i nastroju niezmiernie łatwo. To też chybionych rzeczników przed rządem i opinią rosyjską miało społeczeństwo polskie pełno i odżegnywa się nieufnie od niepowołanej ich gorliwości. Na szczęście, w tym wypadku z innym jakimś, zgoła odmiennym głosem mamy do czynienia. Ten Polak nie udaje dyplomaty ani jałmużnika, nie kłania się i nie biada, mówi imieniem Polski, lecz jej nie adwokatuje, nie szuka dla niej łaski ani zlitowania, zajmuje się on w rzeczy samej jedynie „wykryciem istotnej prawdy”, a czyni to z godnością, powagą i zupełnym spokojem. Im bardziej rozczytywać się w tym niezwykłym Liście, tem jaśniejszem się staje, że tu nareszcie odezwał się ktoś taki, kto wybornie odczuwa ducha swego narodu, a zarazem jasno pojmuje ducha chwili i w lot pochwycił jej potrzeby. To pismo tak treściwe, rzetelne i proste jest dokumentem znamiennym, jest czemś więcej, bo czynem pożytecznym, przychodzącym w samą porę.

Pora istotnie jest wyjątkowa. Rosya znajduje się obecnie jeśli nie w dobie przełomu, to nadzwyczaj ostrego przesilenia. W takich chwilach krytycznych wszelakie nurtujące państwo nierozstrzygnięte zagadnienia zasadnicze, chociażby w zwykłym czasie najuporczywiej w głąb spychane, koniecznością przyrodzoną wydobywają się na wierzch i upominają się o rozwiązanie lub bodaj tylko o jasne postawienie. To był właśnie punkt wyjścia autora Listu. Wyraża on przekonanie, „że z powodu wielkich wypadków na Wschodzie przyjdzie, jeśli nie do radykalnych zmian, to przynajmniej do radykalnej rewizyi spraw i stosunków” rosyjskich w ogóle, a rosyjsko-polskich w szczególności. Dalsze jego wywody są trafnem rozwinięciem tego wytycznego pewnika pod adresem rosyjskim. Co z niemi uczyni petersburski minister, — tego nie wiemy i zgłębiać nie chcemy; być może, przejdzie nad niemi poprostu do porządku dziennego. Dla nas w tej chwili ważną jest rzeczą, jak należy ze stanowiska polskiego ocenić wystąpienie autora, i w takiej myśli, między sobą i dla swoich, pragniemy podzielić się niektóremi uwagami, jakie nastręczały się nam przy odczytywaniu jego Listu.

Autor wziął asumpt z obecnej wojny rosyjsko-japońskiej do podniesienia sprawy rosyjsko-polskiej i zrobił dobrze. Nie znaczy to bynajmniej, aby trzeba było dopiero nieszczęśliwej dla Rosyan wojny nad Oceanem Spokojnym, aby uczynić aktualną sprawę naszą nad Wisłą. Nie znaczy, abyśmy musieli spekulować na ich kłopoty zamorskie dla dobra tej naszej sprawy domowej. Wiemy doskonale, że fizycznie są oni jeszcze i pozostaną dość silni na nas bezbronnych. Ale chcemy wierzyć, że z doznawanego obecnie fizycznego wstrząśnienia powinna wyniknąć w nich samych zbawienna reakcya, która otworzy im oczy na własne ich ciężkie błędy, jak w wielu innych rzeczach, tak i w polskich. Nie spekulujemy na ich osłabienie: chcemy liczyć na ich otrzeźwienie. Szli dotychczas naoślep samą inercyą biurokratyczno-militarnego koloru, czy to w kierunku polityki wewnętrznej, czy światowej; doszli do absurdu w obudwóch; pragniemy, życzymy im szczerze dla własnego ich dobra, aby w obudwóch przejrzeli; a rzecz prosta, przedewszystkiem pragniemy, życzymy im, ażeby, przejrzawszy, rozpatrzyli się i rozrządzili uczciwie i rozumnie w swojej złej i niedorzecznej gospodarce polskiej.

Zaiste, sprawa polska w Rosyi nie potrzebowała dopiero doczekiwać się aktualności dnia dzisiejszego. Dojrzała ona nie od dziś ani od wczora, nie od Ukazu mobilizacyjnego w Królestwie Polskiem, ani od bitwy nad Szaho. Jestto rzecz niesłychana: sprawa tak paląca, tak straszliwie nękająca całe wielkie społeczeństwo polskie, tak głęboko wrzynająca się w sam rdzeń, w całą przyszłość ogromnego państwa rosyjskiego, od lat z górą 40 utrzymywana jest ciągle na punkcie absolutnie martwym, na doraźnym popowstańczym punkcie represyjnym. Aleć to blisko pół wieku, to jest duży odłam dziejowy, to jest okres, w jakim ongi zmieściły się rozbiór Rzpltej, Księstwo Warszawskie, Królestwo Kongresowe, Statut Organiczny, a teraz zmieścił się tylko jeden przeciągający się bez końca, bez celu, bez myśli, tępy anachronizm ucisku. W tych ostatnich latach 40 odmieniła się postać świata, na Zachodzie i Wschodzie podniosły się nowe państwa, zjawiły się nowe prądy, zdobycze i groźby społeczne, posunęła się naprzód ludzkość, kultura, dzieje, a urósł też niepomału, przeobraził się i postąpił naród polski. A sprawa polska w Rosyi po dawnemu stoi na miejscu nieruchomo jak bagno, stoi ciągle tam, gdzie przed 40 laty postawiła ją nie jakaś twórcza organiczna idea ewolucyjna, ale chwilowy gwałtowny rozmach tłumiącej siły. Sam fakt tej zupełnej negacyi niewstrzymanego pędu życia przez skostniały, zastygły w sobie, z gruntu przedawniony system rządzenia jest potwornością logiczną, stanowiącą najdobitniejsze własne swoje potępienie. Ten system zrzucić nie w naszej teraz jest mocy. Naszą rzeczą jest do czasu znosić go, przetrwać, i to czynimy ze skutkiem zgoła dla nas zadowalającym, choć z wysiłkiem niemałym i męką nieznośną. Zmienić go rzeczą jest jego twórców i wykonawców, którzy go stosują z wynikiem dla siebie zgoła ujemnym, a z demoralizującem poczuciem jego beznadziejnego bankructwa. Jest w tem oddawna aktualność polityczna ogromna, lecz obustronnie conajmniej równa: dla Rosyan aktualność czynna wydobycia się z nieobliczonego w swych następstwach, coraz pogarszającego się, kiedyś może śmiertelnego błędu; dla nas tylko aktualność bierna wydobycia się z coraz dotkliwszego, lecz niewspółmiernego z mocą naszą, niezdolnego nas zabić, cierpienia.

„Stałym stanem, w jakim żyje naród polski w państwie rosyjskiem — pisze autor — jest najgłębsze cierpienie”. Nie jestto skarga, jeno proste skonstatowanie oczywistego faktu. Dajemy temu państwu ponad możność naszą. Jego potęga w niemałej części stoi naszą krwią i mieniem. 10% ogólnego składu armii rosyjskiej, więc około 100 tysięcy ludzi na stopie pokojowej, około 300 tysięcy na wojennej, stanowią katolicy, t. j. Polacy. Z samego Królestwa Polskiego wybiera rząd corocznie 25 tysięcy popisowych. Idą te dzieci nasze w czasie pokoju na długą, najdłuższą w Europie, 4–5 letnią twardą służbę żołnierską pod obcem dowództwem, w dalekie krańce olbrzymiego imperyum, gdyż na miejscu, na ziemi swojej, służyć rekrutowi polskiemu nie wolno; idą w czasie wojny, dłużej niż gdzieindziej trzymani w zapasie, jak dzisiaj na śmierć na kraju świata. Podobnież udział nader poważny mamy w zasileniu skarbu państwa rosyjskiego. Dochody państwowe z Królestwa Polskiego wynoszą dziś corocznie około 150 milionów rs. Za Królestwa Kongresowego, również pod berłem rosyjskiem, cały nasz budżet roczny wynosił 10 milionów rs.; utrzymywaliśmy z tego własną wzorową armię krajową, własny sprawny rząd, własne doskonałe sądownictwo, instytucye reprezentacyjne, czyniliśmy wielkie i płodne inwestycye kulturalno-społeczne, podnieśliśmy kraj w lat kilkanaście z zupełnej ruiny do kwitnącego stanu. Od tego czasu ludność wzrosła niespełna 2½ razy, wkład nasz budżetowy wzrósł 15 razy, t. j. sześć razy wyżej niż ludność, zaś wydzielany stąd nakład na rzecz samego społeczeństwa zmniejszył się o nieskończoność razy, zmalał niemal do zera. Płacimy dziś przeciętnie około 15 rs. rocznie na głowę, dwa i trzy razy tyle, co najpłodniejsze wewnętrzne gubernie rosyjskie, a nie mamy za to dla siebie nic albo prawie nic. Z owych płaconych przez nas corocznie 150 milionów rs. około ⅓ idzie na utrzymanie dozorujących nas w kraju naszym wojsk rosyjskich; drugie tyle na utrzymanie administracyi rosyjskiej w tym kraju trzymającej nas w więzach; niedostrzegalnie drobny ułamek idzie na produkcyjne potrzeby społeczne, upominające się napróżno o poważne nakłady; reszta, niewiele mniej jak ⅓, wpływa czystą nadwyżką do skarbu państwowego. Siedzimy tym sposobem w domu naszym własnym wywłaszczeni przymusowo, niby komornicy na wysokiem, dowolnie z nas ściąganem komornem, zgoła na łasce gospodarza, który do samego ogniska narodowej rodziny naszej, do najnietykalniejszych, najświętszych spraw naszych się wdziera, a nawet o porządne utrzymanie zabranego domu nie dba, dochody z niego na postronne cele obraca, zaniedbuje najniezbędniejszych instalacyi, napraw, przebudowy, oświetlenia, nie troszczy się o to, że w tym domu wszędzie się wali, przecieka, że w nim coraz duszniej i coraz ciemniej.

„Rosyanie administrujący naszym krajem — pisze autor — idą zaraz po Turkach”. W tych mocnych słowach niema przesady. Znajdują one potwierdzenie we wszystkich gałęziach obecnej gospodarki rosyjskiej w Królestwie Polskiem. A więc nasampierw w zakresie ich gospodarki edukacyjnej. Tutaj od dołu do góry, od szkółki elementarnej, aż do uniwersytetu warszawskiego, najkonsekwentniej objawił się duch i owoce systemu. Królestwo na przeszło 30 tysięcy wsi i 7 milionów ludności wiejskiej katolickiej posiada 2½ tysiąca szkół początkowych wiejskich z frekwencyą 150 tysięcy uczniów obojga płci, t. j. jedną szkołę na wsi kilkanaście i jednego ucznia na 40 kilku mieszkańców. A szkoła to osobliwa, jakiej drugiej niema w Europie. W tej szkole wiejskiej dla katolickiego polskiego ludu niema naprawdę nauki religii katolickiej i języka polskiego. Narzucony przez władzę nauczyciel świecki, często prawosławny, wykłada katechizm polskiemu włościańskiemu dziecku, uczy je wiary ojców. Duchem opiekuńczym tej bezprzykładnej szkoły ludowej nie jest społeczeństwo i Kościół, ale komisarz i strażnik ziemski. Nie jestto instytucya umoralniająca i kształcąca maluczkich, ale rozmyślnie u samych podstaw społecznych podkopująca wiarę i pociąg do nauki.

Nie dziwota, że chłop nasz od takiej szkoły stroni, że dziecko chłopskie w niej nie wytrzymuje. Z powyższej liczby uczniów około 75% już po jednym roku przestaje uczęszczać do szkoły, zaś tylko 4% potrafi wytrwać w niej do końca. Wynik jest taki, że przyrost roczny umiejących czytać i pisać wynosi w Królestwie 1, 2%, kiedy natomiast sam naturalny przyrost wiejskiej ludności katolickiej w kraju wynosi rocznie 1·7%, czyli innemi słowy, absolutny odsetek analfabetów, zamiast zmniejszać się, corocznie stale wzrasta. Na ogół — wedle urzędowego obrachunku, który zawdzięczamy familijnemu zatargowi między dwoma naszymi ciemięzcami, generał-gubernatorem Hurką a kuratorem Apuchtinem, w ciągu ostatnich lat kilkunastu sprawa początkowego nauczania ludu wiejskiego w Królestwie cofnęła się wstecz w stosunku 8%. W podobnem położeniu znajdują się szkoły początkowe miejskie. Jest ich w Królestwie kilkaset zaledwo z liczbą uczących się niespełna 40 tysięcy na 400 kilkadziesiąt miast i osad z półtoramilionową ludnością katolicką, czyli znowuż w stosunku jednego ucznia na blisko 40 mieszkańców; zaś przy większej w mieście łatwości ucisku, są one poddane gorszemu jeszcze niż na wsi rygorowi policyjnemu. Najgorzej pod tym względem dzieje się tam, gdzie powinnoby dziać się najlepiej: w Warszawie. Tutaj, w bogatej stolicy kraju, której milionowe dochody zjada wielousty polip biurokratyczno-policyjny, na szkoły niema pieniędzy. Warszawa przy rocznym budżecie 13 milionów wydaje na cele wychowawcze około 300 tysięcy rs. t. j. absolutnie dwa razy mniej, aniżeli ubogi Lwów z ludnością pięćkroć mniejszą, więc stosunkowo dziesięć razy mniej. Zarazem inicyatywa wychowawcza najpoważniejszych nawet instytucyi społecznych jak Towarzystwo Dobroczynności, cóż dopiero osób prywatnych, prześladowana jest czujniej, niż zbrodnie kradzieży lub mordu. I oto pod okiem bezwładnej, nieszczęsnej naszej stolicy-matki około 100 tysięcy jej dziatwy w wieku szkolnym między 8 a 15 rokiem życia rośnie bez opieki i światła, oddane na pastwę występku i nędzy.

Co się tycze szkolnictwa średniego, t. j. gimnazyów rządowych klasycznych i realnych, zostało one jaknajgruntowniej doprowadzone do takiego stopnia ohydy, jakiej wprost niepodobna wyczerpać żadnym opisem. Łapownictwo, szpiegostwo, brutalstwo, nieuctwo — oto są cztery krawędzie, na których wznosi się wychowanie gimnazyalne w kraju naszym. Nadomiar gimnazya nawet ilościowo nie odpowiadają potrzebom; frekwencya w porównaniu do wzrostu ludności i tutaj cofa się w stosunku nadzwyczajnym, który już w okresie Apuchtinowskim dosięgnął 25%. Wynikające stąd chroniczne przepełnienie stało się obfitem źródłem dochodu dla dyrektorów i nauczycieli gimnazyów, dokąd bez wstępnego kubana dziecka wprowadzić zwykle niepodobna, ani bez ponawianych datków przeprowadzić go szczęśliwie do matury. A z jakim bolesnym niepokojem rodzice polscy wiodą tutaj synów swoich, z jakim głębokim wstrętem dorastający młodzieńcy wysiadują niby skazańcy w tem gimnazyalnem więzieniu. Ośmioletni pobyt w gimnazyum Królestwa równa się istotnie tyloletniej karze galer duchowych dla kilkunastu tysięcy najlepszej młodzieży polskiej. A jest ona zmuszona iść na tę długą kaźń dla zarobienia sobie t. z. praw dojrzałości, sprowadzających się naprawdę, wobec zamknięcia przed Polakami wszelkich posad, prawie wyłącznie do pewnych ulg w powinności wojskowej; jest zmuszona zdobywać ten mizerny przywilej za cenę cierpliwie znoszonej poniewierki tem, co człowiek, a zwłaszcza młodzieniec ma najświętszego: swoją narodowością, religią, honorem. Szkoły prywatne średnie, wraz niemiłosiernie uciskane i wyciskane przez tłocznię ssącą inspekcyi naukowej, poradzić na zło gimnazyalne skutecznie nie mogą, a nawet ostatniemi czasy pod postacią t. zw. gimnazyów prywatnych z prawami rządowych, coraz natarczywiej ujawnia się dążność do wyzyskania tych szkół dla celów rusyfikacyjnych, sposobem najdogodniejszym, bo darmym, na koszt już nawet nie państwa, lecz społeczeństwa samego.

Szkolnictwo wyższe, ten kwiat kultury wychowawczej, musiało oczywiście ucierpieć jeszcze dotkliwiej na stosunkach podobnych. Uniwersytet warszawski, jest pogrzebany wśród polskich, poniżony wśród rosyjskich, ostatni wśród europejskich. Ten uniwersytet w stolicy Królestwa Polskiego jest swego rodzaju unikatem. Zrusyfikowany doszczętnie w języku, treści, obsadzie wykładowej, nie zna on wcale nauki dziejów polskich ani prawa polskiego, nie daje polskiego wykładu literatury rodzimej, nie uczy obowiązującego katolickiego prawa kanonicznego, nie troszczy się o przedmioty naukowe niezbędnej wprost doniosłości życiowej, jak obowiązujące w tym kraju po dziś dzień polskie i francuskie prawodawstwo cywilne, handlowe, hypoteczne, odprawione bylejako przez całkiem obcych w tych rzeczach docentów Rosyan. Ten uniwersytet wystawiony na gruzach Szkoły Głównej, która tylu wydała mężów niepospolitych, odtąd w ciągu 30-kilkoletniego opłakanego swego istnienia, nie wydał, bo wydać nie mógł, ani jednego uczonego, pisarza, działacza istotnie wyższej miary. Co tylko śród młodzieży naszej jest zdolniejszego, wybitniejszego, ucieka z tej ciemnicy po światło do wszechnic polskich zakrajowych albo do obcych zagranicznych. Zresztą i w tym wypadku znieprawieniu zasad wychowawczych zakładu towarzyszyć musiało znamienne obniżenie frekwencyi. Dziś uniwersytet moskiewski liczy 5 tysięcy słuchaczów, petersburski 4, kijowski 3½, helsingforski 2½ tysiąca. Uniwersytet warszawski jedyny na 11-milionową ludność Królestwa, t. j. pięćkroć większą od całej Finlandyi, liczy słuchaczów 1½ tysiąca, w czem znaczna ilość Rosyan ściąganych rozmyślnie przez przywileje i ułatwienia z najdalszych gubernii, nawet z Syberyi, zaś Polaków niespełna tysiąc. Równocześnie Galicya z ludnością 7½ miliona posiada dwa uniwersytety, liczące, krakowski około 2, lwowski około 3, razem blisko 5 tysięcy słuchaczów.

Tak przedstawia się na wszystkich swych szczeblach działalność edukacyjna prowadzona w imię obecnego systemu przez t. zw. „kuratorów” oświaty Królestwa, jak dla pośmiewiska tytułują się jej grabarze. Konkluzyę ostateczną tej grabarskiej roboty ujmują lapidarnie następujące proste cyfry. Ilość analfabetów wśród popisowych, która w guberniach nadbałtyckich wynosi 5%, w Rosyi środkowej przeciętnie 65% — (gdzieindziej n. p. w Niemczech, zaledwo ½%) — w guberniach Królestwa Polskiego wynosi 82%. W urzędowem wydawnictwie petersburskiego Komitetu ministrów, przeznaczonem do informowania Europy o rzeczach rosyjskich (Statesman's Handbook for Russia ed. by the Chancery of the Commithee of ministers) czytamy taką hańbiącą nas przed światem lakoniczną wzmiankę: „najniższego procentu umiejących czytać i pisać pośród poborowych dostarcza Królestwo Polskie oraz Syberya”. A więc pod jednym z względów najpierwszej wagi dla społeczeństw cywilizowanych, doprowadzeni zostaliśmy, my, Królestwo Polskie, najkulturalniejsza, najoświeceńsza część państwa rosyjskiego, na jeden poziom, już nie z Europą zachodnią, już nawet nie z którąkolwiek gubernią Rosyi środkowej, ale z barbarzyńską dziczą pustyń azyatyckich.

To jest poprostu dewastacya kulturalna. Dalsze jej skutki nie dały na siebie czekać. Ujawniły się one między innemi w zastraszającym wzroście występności. Występność zmniejsza się w Anglii, trzyma się na równi w Austryi i Francyi, nie wykracza poza karby normalne w Niemczech: w Królestwie Polskiem wzrasta gwałtownie, w stosunku trzy razy wyższym aniżeli w Rosyi wewnętrznej. W ciągu ostatniego dziesięciolecia, w dziesięciu guberniach polskich wzrosła o 46%, w wewnętrznych rosyjskich zaledwo o 14%. Dla należytej oceny tego zjawiska trzeba wziąć na uwagę, że ludność nasza pod względem przysposobienia moralnego, n. p. pod względem trzeźwości znakomicie przewyższa rosyjską, oraz, że wśród osób sądownie skazanych w Królestwie jest 86% analfabetów.

Stosunki prawno-sądowe Królestwa w ogólności w ciągu ostatnich lat 30-tu, t. j. od wprowadzenia reformy sądowej, uległy równie systematycznemu spaczeniu od wierzchołka aż do podstaw. Prezydyum Izby sądowej warszawskiej, więc niejako ministeryum sprawiedliwości na Królestwo, spoczywa w ręku dygnitarzy rosyjskich, sprawujących nietyle sędziowską ile polityczną działalność. Sądownictwo apelacyjne, okręgowe, pokojowe, obsadzone zostało wyłącznie przez Rosyan, zgoła nieobeznanych ani z warunkami, ani nawet z prawodawstwem krajowem. W najsubtelniejszych zagadnieniach procesu cywilnego, wymagających zarówno głębokiej znajomości stosunków, pojęć i zwyczajów społeczeństwa polskiego, jakoteż oswojenia się z duchem miejscowej kodyfikacyi sejmowej i Napoleońskiej, orzekają nieświadomi tych rzeczy sądownicy rosyjscy, goszczący w tym kraju na przygodnym etapie swojej karyery służbowej. W najpoważniejszych wypadkach procesu karnego, gdzie chodzi o wolność i życie, orzekają oni wedle martwej litery kodeksowej, bez najmniejszej styczności z tętnem miejscowego życia prywatnego i zbiorowego, na podstawie wygłaszanych w języku dla nich niezrozumiałym zeznań świadkowych polskich przekładanych ex promptu na język urzędowy przez kancelaryjnego tłumacza. Ci sędziowie zresztą, choćby nawet osobiście uczciwi, są poddani bezpośredniej presyi administracyjnej występującej niekiedy wręcz skandalicznie w głośnych procesach przeciw uprzywilejowanym mordercom i gwałcicielom, którzy wychodzą z sądu obronną ręką, jeżeli są Rosyanami w mundurze i jeśli ich ofiarą jest artystka albo suchotnica polska. Sądów przysięgłych, jakie oddawna posiada cesarstwo, Królestwo jest pozbawione zupełnie, między innemi dlatego, że niema sposobu wprowadzić ich z językiem rosyjskim, a z polskim wzbrania system. Palestra polska piastująca tak wysokie tradycye, skąd niegdyś wychodzili nietylko znakomici prawnicy, lecz prawodawcy i statyści, jest poniewierana przez każdego prezesa sądu okręgowego, przez każdego sędziego pokoju. Rosyjscy sędziowie pokoju z urzędu dla ludności polskiej, ta dziwaczna jurysdykcya przeciwna samej swojej naturze, niedorastający godności sędziowskiej pod każdym względem, a najpierw pod moralnym, niemający szacunku u własnych swoich rodaków i kolegów z wyższych instancyi, prezydują z urzędu w polskich radach familijnych, wyrokują o codziennym trybie powszedniego życia całej ludności miejskiej, u której tyleż są w postrachu, co w zasłużonej pogardzie. Sędziowie gminni, jedyna w tym obrębie instytucya wyborcza, krępowani są i dozorowani najściślej w skromnej swojej działalności; nadto w znacznej części kraju obieralność ich poprostu jest zniesiona aktem samowoli administracyjnej i na ich miejsce w guberniach unickich, zwłaszcza lubelskiej i siedleckiej — niemal wyłącznie są mianowani prawosławni sędziowie gminni z urzędu.

Wiadomo powszechnie jak fatalnie ukształtowały się stosunki wyznaniowe w Królestwie. Kościół rzymsko-katolicki, pod którego pieczą przedstuletnią wzrósł naród nasz i kultura, traktowany jest otwarcie jako wróg. Polski ksiądz katolicki z pierwszego pasterza swego ludu zdegradowany został na stopień ostatniego oficyalisty rządowego, a zarazem osoby wiecznie podejrzanej i pod nadzorem będącej. Jest on pilnowany w swoich najprostszych obowiązkach duszpasterskich, krępowany w dobroczynnych, ścigany w wychowawczych. W każdej rzeczy, z każdego kroku musi referować się pierwszej lepszej władzy świeckiej. Ta władza innowiercza wchodzi do seminaryum katolickiego i opinią swoją względem dostatecznej znajomości literatury rosyjskiej stanowi o kwalifikacyi na dobrego księdza katolickiego. A potem jest ta rana otwarta: unia. Przyznaje się corocznie Synod petersburski do blisko 100 tysięcy „upornych” unitów, a jest ich w rzeczywistości liczba, conajmniej czterokrotna zaliczona do „nawróconych”. Los tych nieszczęśliwych od przeszło ćwierci wieku, w drugiem już pokoleniu męczonych bez miłosierdzia, jest okropny. Ci ludzie żyją bez chrztów, ślubów, pogrzebów, pod ciągłą groźbą Syberyi, pod cierpieniem fizycznem i duchowem i pod pokusą pozbycia się tych cierpień za zaprzaństwo wiary; żyją jak pierwsi chrześcijanie, pod jawnem prześladowaniem religijnem, dziś w XX wieku na samym skraju Europy Zachodniej. Na tem prześladowaniu zyskali jedno: utwierdzili się nietylko we wierze ale także w świadomości narodowej. Mamy gdzieindziej, w Galicyi, swoje z Rusinami zatargi i kłopoty, które niewątpliwie, prędzej czy później braterską ułatwimy zgodą: tutaj w guberniach unickich Królestwa „uporna” ludność pochodzenia rusińskiego dzięki uciskowi rządu tem prędzej spolszczyła się i unarodowiła. Wroga dla kraju polityka rządowa na swój sposób równie konsekwentnie ujawniła się w stosunku do wyznań obcych w Królestwie. Mamy tu około półmiliona ewangelików obojga obrządków. Dawni dysydenci, dziś coraz więcej dobrzy Polacy, są przez rząd popychani raczej ku germanizacyi, byle tylko oddalić ich od społeczeństwa, do którego należą. W guberniach Królestwa, tam nawet gdzie ewangelicy nie chcą znać albo i nie rozumieją już wcale niemczyzny, są oni przymuszani do nauki religii w języku niemieckim, — choć w guberniach nadbałtyckich dla ewangelików estów i łotyszów przepisany jest szkolny wykład religii w języku estońskim i łotyskim zamiast niemieckiego; gdyż to, co dobre jest w Mitawie, Rydze i Rewlu, jest oczywiście złe w Warszawie, Łomży lub Suwałkach i dla tych samych powodów. Podobna metoda wyodrębnienia, stosowana jest też względem ludności żydowskiej, której mamy w kraju do 1½ miliona. Niedość, że od przeszło stulecia przez rozmyślne stłoczenie jej w obrębie b. Rzpltej, przez wzniesienie t. z. linii osiedleńczej, zarazem unieszczęśliwiono tę ludność i uczyniono ją plagą kraju, że przed niedawnym czasem znów dziesiątkami tysięcy część jej zrusyfikowaną spędzono z głębi Rosyi do tego kraju, ale na dobitkę zaczęto z urzędu hodować najnowsze budzące się w niej instynkty nacyonalistyczne, popierać niebezpieczną agitacyę syonistyczną, nie w innej myśli, jak tylko dla wbicia nowego klina w budowę społeczną Królestwa.

W tem wszystkiem nie było jeszcze wcale mowy o podkopującej i więziącej Królestwo ogromnej akcyi administracyjnej w ściślejszem znaczeniu słowa. A więc o demoralizującem poddaniu polskiego ludu włościańskiego pod samowładny dozór policyjny wszelkich władz gubernialnych, powiatowych, komisarzów włościańskich, straży ziemskiej. O zupełnem skrzywieniu t. z. samorządu gminnego, którego wszystkie organy uczyniono naprawdę jedynie najniższem narzędziem wykonawczem w ręku rzeczonych władz, narzucających bezprawną swoją obecność i dyrektywę samym nawet zgromadzeniom gminnym. O kardynalnem spaczeniu tego rzekomego samorządu polskiego ludu przez narzucenie mu w czynnościach niezrozumiałego dla tego ludu języka rosyjskiego. O systematycznem zabagnieniu sprawy służebności włościańskich, oddawna skasowanych na Zachodzie, nieznanych w guberniach wewnętrznych, bez znaczenia w przyległych cesarstwa, a które jedynie w Królestwie za machiawelską poradą Murawiewa, dla zatrucia stosunków między obywatelstwem a włościaństwem polskiem zachowywane są troskliwie w całej pełni przez podstępną politykę serwitutową rządu, przez rozmyślną wadliwość represyi prawnej nadużyć serwitutowych, przez rozmyślne stworzenie chłopskiego liberum veto dla uniemożliwienia najdogodniejszych dla gminy dobrowolnych umów regulacyjnych. O rozmyślnem utrzymywaniu fatalnych stosunków komunikacyjnych w kraju, bądź przez chroniczną kradzież funduszów drogowych, bądź przez systematyczne tamowanie rozwoju sieci kolejowej, z takim skutkiem nadzwyczajnym, że dziś pod tym względem nietylko pozostaliśmy daleko w tyle za Europą Zachodnią, za Galicyą, Austryą lub Niemcami, gdzie przypada 8–9 kilometrów kolei na 10 tysięcy mieszkańców, ale nawet za samem cesarstwem rosyjskiem, mającem dziś na rzeczoną miarę 3, 2 kilometrów, kiedy Królestwo, przy nieskończenie wyższych potrzebach ma tylko 2, 7 kilometra. O całej haniebnej gospodarce rządów gubernialnych, o rujnującej gospodarce miejskiej, o bezprzykładnem położeniu Warszawy, jednego z najpierwszych miast w Europie, a pozbawionego tych elementarnych praw autonomicznych jakie posiada ostatnia mieścina w cesarstwie. O ponawianych nienawistnych zamachach na spokojną, a wzorową instytucyę tej powagi co Towarzystwo Kredytowe Ziemskie; o zniesieniu Banku Polskiego; o rusyfikacyi czysto prywatnych towarzystw akcyjnych; o taryfach dyferencyalnych godzących w rolnictwo i przemysł krajowy, zabijających nasze młynarstwo przez ułatwiony zalew rynków krajowych mąką rosyjską, albo krzywdzących nasz przemysł bawełniany w interesie okręgów fabrycznych cesarstwa, o nadużyciach inspekcyi fabrycznej; o ruszczącej agitacyi kuratorów trzeźwości; o nieznośnym ucisku cenzury sprawowanej autokratycznie nad prasą i piśmiennictwem polskiem przez małych urzędników rosyjskich, przed których codziennym ukazem korzyć się muszą najpierwsi pisarze, uczeni, publicyści polscy i t. d. bez końca. Ale wchodzić w to wszystko, choćby tylko wytknąć najpobieżniej, niema wcale sposobu ani nawet potrzeby. Te wszystkie szczegóły, jakkolwiek dotkliwe, to są tylko rozliczne symptomaty jednej choroby, a tą chorobą jest system.

Ów system t. zw. urzędownie „zjednoczenia Królestwa z państwowością rosyjską” czyli istotnie jego wynarodowienia, zruszczenia, kiedy przed 40 laty sformułowany był na poczekaniu przez Komitet do spraw Królestwa Polskiego, został wtedy oparty na jednej premissie głównej, mającej poręczyć jego wykonalność: a mianowicie na tem, że chłopa polskiego za uwłaszczenie można kupić, wynarodowić, obrócić przeciw opornej reszcie narodu i przykryć ją, przytłumić tą pozyskaną masą chłopską. Recepta była godna tych komitetowych empiryków udających lekarzy, polityka godna tych biurokratów udających mężów stanu. Chłop polski ziemię wziął, lecz oczywiście za tę własną swoją ojcowiznę kupić się nie dał. Umocniony ekonomicznie, tem żwawiej jął uświadamiać się narodowo i nabywaną siłę i samowiedzę doniósł do wspólnego skarbca zasobów zdrowia i energii swojemu narodowi, którego jest kręgosłupem. Inaczej być nie mogło. Ani ludu kupować nie można, ani duszy narodowej rozłupywać i gasić. To było jasne od początku. Rząd rosyjski dowiedział się o tem oficyalnie, czarno na białem, z memoryału ks. Imeretyńskiego. Dowiedział się, że naród polski, o którym po 1830 roku głoszono, że jestto garść szlachty, a po 1863 że jestto tłum mieszczan i duchowieństwa, — jestto także lud włościański. Z tem nadzwyczajnem odkryciem padła tamta mądra premissa, ale system pozostał.

Otóż radykalne zlikwidowanie tego systemu jest najpierwszym negatywnym warunkiem otwierającym dopiero przystęp do prawidłowego postawienia sprawy polskiej w Rosyi. Samego systemu, nietylko jednego lub drugiego szczegółu, gdyż chodzi tu o usunięcie choroby, a nietylko pojedynczych jej symptomatów. Jestto nieodzowny warunek przedwstępny, bez którego przystępować do dyskusyi niema wcale sposobu. Dlatego też wszelkie podejmowane dotychczas dyskusye na ten temat były po prostu stratą czasu. Pod tym względem wśród życzliwej nawet dla nas części opinii publicznej i prasy rosyjskiej zdaje się panować dziwne nieporozumienie. Stawiają tam kwestyę tak: że mogłaby nareszcie w takiej czy innej rzeczy spłynąć na nas niejaka folga, ale musielibyśmy nasamprzód uczynić coś takiego, co zapewniłoby nam zaufanie Rosyi i rządu. Trudno doprawdy wyobrazić sobie potworniejszy paradoks polityczny. Stoimy bezbronni, ubezwładnieni, wyzuci, wobec największej potęgi militarnej świata, która zabrała nam wszystko i jeszcze przychodzi do nas, abyśmy jej dali jakieś gwarancye. Ależ gwarancya należy się nam, pozbawionym wszelkiej poręki oprócz naszego prawa, a nie tym, którzy ją dzierżą w samej swojej sile fizycznej. „Nie państwo do nas — są z tego powodu rozsądne słowa autora Listu — ale my do państwa powinniśmy mieć zaufanie, z tej prostej przyczyny, że państwo ma w ręku siłę, że co przyzna, może w każdej chwili odjąć”. I czyliż ono nie robiło tak ciągle? Czyliż nie odebrało konstytucyi Królestwu, Statutu Organicznego, ostatnich resztek autonomii, ostatnich ubezpieczeń religijnych, prawnych, językowych, kulturalnych kraju naszego? Nie mamy dziś, bo mieć nie możemy, żadnego zaufania do tego państwa i musi ono dopiero na zaufanie nasze zasłużyć, a uczynić tego nie może inaczej, jak przez zupełne zerwanie z całym dotychczasowym systemem swojej polityki polskiej.

I na czem właściwie miałyby konkretnie polegać owe niepojęte, nieuchwytne gwarancye od nas z góry wymagane? Nawołują nas do porzucenia mściwych rekryminacyi przeszłości, zbliżenia się bez uprzedzeń do wielkiego społeczeństwa rosyjskiego, oswojenia się bez przesądów z bogatym językiem rosyjskim, jednem słowem do rozbrojenia się. Niewiadomo doprawdy, co w tem dziwniejsze: nieznajomość czy też niedocenienie i samej sprawy i naszej dojrzałości samozachowawczej. Dojrzeliśmy zanadto, abyśmy naszą politykę narodową mieli fundować na mściwem rozżaleniu albo nienawistnym przesądzie. Mściwość jest cechą narodów słabych, a polski jest silny. Dlatego mógł on w lat 20 po rzezi praskiej porozumieć się z Rosyą Aleksandra I. Dlatego w 20 lat po rzezi galicyjskiej mógł porozumieć się z Austryą Franciszka Józefa. Ale w jednym czy w drugim wypadku wprzódy z tamtej strony zerwano z fatalnym systemem. W Rosyi niestety nakrótko, i niebaczna recydywa państwa rosyjskiego pociągnęła też za sobą odporny nawrót Królestwa Polskiego; w Austryi, gdzie nowy kurs został dotrzymany bez zwichnięcia, Galicya pomimo tak trudnych skądinąd warunków ogólno-politycznych i ekonomicznych, dotrzymała również wiary, bez jednego drgnięcia w okresie już przeszło dwa razy dłuższym aniżeli całe trwanie Królestwa Kongresowego. Zresztą komuż tu mówić o rekryminacyach? Czyliż cała zawzięta, tępicielska polityka polska Rosyi, porewolucyjna i popowstańcza nie jest nawskróś rekryminacyjną? Krzywdziciel miewa zazwyczaj dłuższą pamięć od pokrzywdzonego. Trudniej wybaczyć te krzywdy, które się wyrządziło, aniżeli te, których się doznało. Nie mściwe jakieś instynkty, które czułą perswazyą możnaby ugłaskać, ale prosty instynkt samozachowawczy kieruje naszą polityką narodową i pod karą śmierci niedopuszcza rozbrojenia ani na jedną chwilę, wobec warunków obecnych. Zapewne Polak może i dziś bez uprzedzeń zejść się z dobrze myślącym Rosyaninem w Petersburgu lub Moskwie. Aleć my w Królestwie dźwigamy 100 tysięcy gnębiących nas urzędników i 250 tysięcy żołnierzy rosyjskich. W takiem położeniu najostrzejszy, bezwzględny separatyzm jest wręcz nieodzownym środkiem obronnym. Jakim sposobem Polak wdający się w „zbliżenie” z tutejszym działaczem rosyjskim w swoim pokoju gościnnym w Warszawie, wytłumaczy Kachnie czy Maryśce, żeby ona w kuchni nie „zbliżała się” z rosyjskim szeregowcem, żeby z nim nie poszła na ślub do nowej cerkwi na Placu Saskim i nie płodziła dzieci prawosławnych dla naszej stolicy? Albo znowuż każdy Polak może poza obrębem swego kraju szanować w języku rosyjskim piękny organ świetnego piśmiennictwa i nauki rosyjskiej; aleć u nas w Królestwie ten język jest obecnie tylko wilkiem, duszącym naszą mowę ojczystą, którego nie wpuszczać, którego tępić jest naszym obowiązkiem. Że tak jest, nie naszem jest dziełem, lecz Rosyi i jej systemu rządzenia w sprawie polskiej i tak być musi póty, póki ten system nie będzie uprzątnięty doszczętnie. Na ten fakt brutalny stworzony przez Rosyę nie poradzą żadne najpiękniejsze słowa, poradzić może tylko zbawienny realny czyn. „Polacy — tak niegdyś Rosyanin światły, dobrze nam życzący, długoletni mieszkaniec Warszawy kongresowej, ubolewał nad naszą łatwowiernością polityczną — nie wymagają bynajmniej, aby im istotnie świadczono dobro; dla nich starczy, byle im szeroko perorować (witijstwowat’) o oczekujących ich dobrodziejstwach”. Jeśli tak było kiedyś, teraz napewno już tak nie jest. Ogrom nieszczęść nauczył nas rozumu. Nie porywamy się niewcześnie do broni, ale też nie kwapimy się bynajmniej do różdżki oliwnej. Wytrzeźwieliśmy na obie strony. Możemy czekać.

Tak zwani ugodowcy są to ludzie, którzy wśród żadnych warunków czekać nie chcą albo nie mogą. „Nie znaleźli oni — postrzega trafnie autor Listu — gruntu w społeczeństwie i nie znaleźli go słusznie”. A jednak oni to przedewszystkiem wysuwają się natarczywie na rzekomych tego społeczeństwa przedstawicieli. Posiadają do tego, — zwłaszcza w najczystszej swojej postaci, najbardziej przedsiębiorczy, najdalej wysuwający się i innych ciągnący za sobą, trzy kwalifikacye następujące: popierwsze nic nie zrobili dla swego narodu, powtóre nie znają go, potrzecie naród ich nie zna i znać nie chce. Nie są to podobno kwalifikacye do przedstawicielstwa zupełnie dostateczne. Z Rosyą dzisiejszą nikt nie ma prawa ugadzać się, ubijać targu za społeczeństwo polskie. Można tylko, a nawet należy, skoro są po temu okoliczności, mówić z nią w interesach tego społeczeństwa. Ale i to jest rzeczą odpowiedzialności niezmiernej i Polak, przemawiający w takiem tylko znaczeniu, winien być do tego potrójnie uzdatniony, przez rzeczywistą narodową zasługę, rzeczywiste narodowe czucie, a co za tem idzie i co główna, przez rzeczywiste zaufanie narodowe, ażeby to co on rzeknie w ścisłym swoim charakterze, nie jakiegoś samozwańczego mandataryusza, lecz uprawnionego rzeczoznawcy, było istotnie sub spe rati, bo sub spe veritatis. A cóż dopiero, kiedy naodwrót, przychodzi o Rosyi mówić z własnem naszem społeczeństwem, oświecać i pokierować opinię polską w rzeczy tak ciemnej, niebezpiecznej a tak niesłychanie doniosłej, jakże wysokie muszą być kwalifikacye upoważniające do takiego kierownictwa. To też raz na zawsze w tych zawrotnych wirach, jakie przedstawia sprawa polsko-rosyjska, do sterowania skołataną nawą publiczną są powołani jedynie ludzie istotnej kompetencyi i autorytetu narodowego, a nie może być dopuszczony nigdy pierwszy lepszy pasażer, choćby nawet pierwszej klasy. Prawdopodobnie i takiemu pasażerowi na tem musi zależeć, aby okręt nie zatonął, aby nie rozbił się ze szczętem, a przecie dozwolić mu steru byłoby kapitalną niedorzecznością.

Z podobnych zaś pasażerów pierwszej klasy wyrywających się do rudla, rekrutują się z reguły ugodowcy, często zwyczajni dilettanti zabawiający się w politykę, kiedyindziej pospolite mouches du coche brzęczące po salonach warszawskich i petersburskich przedpokojach, a tem głośniej im parniej jest w powietrzu, w małej stosunkowo części powodowani osobistą rachubą, przeważnie nawet działający w najlepszej wierze, ale przez to ani na jotę mniej szkodliwi albo raczej właśnie przez dobrą swą wiarę tem szkodliwsi, bo tem łatwiej wprowadzający w błąd i siebie i innych. Gdyż w tem mianowicie tworzeniu, szerzeniu i gruntowaniu rdzennego błędu, we wszechstronnem fałszowaniu rzeczywistego położenia i samej natury sprawy polsko-rosyjskiej tkwi grzech śmiertelny roboty ugodowej. Ta robota to poprostu swego rodzaju brzuchomóstwo polityczne na dwie strony. Ci panowie naprzód mówią z siebie do rządu — a rozlega się przyjemnie jakoby od narodu. Potem mówią z siebie do narodu — a rozlega się przyjemnie jakoby od rządu. A ostatecznie okazuje się, że nie odezwał się naseryo rząd, ani myślał odzywać się naród, głos jest własny tych miłych figlarzów. Kogo się tu właściwie oszukuje? Podobno wszystkich i nikogo. Ale ta zabawa jest nadzwyczaj szkodliwa, gdyż koniec końcem, świadomie czy nieświadomie, w złej czy dobrej wierze, jestto mistyfikacya, która bałamuci na obie strony, zamąca jasność sądu, podstawia fikcyę zamiast realności, a przez to powstrzymuje ustalenie prostej, nagiej prawdy, bez której niemasz tu wyjścia. Tej prawdzie ugodowiectwo nie śmie spojrzeć w oczy, więc ją obchodzi, przesłania. Nie śmie w polskiej polityce rządu negować samego i całego systemu, nie śmie wytknąć źródła choroby, ima się szczególików, czepia symptomatów, w pocie czoła mozoli się nad wyżebraniem jakiejś ułamkowej doraźnej folgi, chwyta skwapliwie każdy podmuch opinii dworskiej, rządowej, publicznej w Rosyi, biegnie za każdym takim podmuchem, dzisiaj lojalne z sentymentu, jutro lojalne po ultrasowsku, pojutrze lojalne liberalnie, dzisiaj budując na ks. Imeretyńskim, jutro na ministrze Plehwem, a pojutrze na „ziemcach” twerskich, budując na wszystkiem, tylko nie na własnym narodzie. I tak wiecznie zaaferowane, projektujące, fatyganckie, przypomina się nieustannie i rządowi i społeczeństwu, tam zalecając się dobrze myślącą gotowością na każde zawołanie, tu popisując się mnogością swoich petenckich zachodów i stosunków, swoją polityką ulepszonych kałamarzów szkolnych czy municypalnych, swoją terapią kojących plastrów, które zaraz służą za pergamin dla polubownych umów politycznych. A cała ta hałaśliwa, ruchliwa akcya jest bez gruntu, cały rachunek robiony bez gospodarza — bez narodu.
Naród polski nie ma żadnego zaufania do tej kategoryi niepowołanych swoich przedstawicieli, działających bez wszelkiego od niego mandatu i bez żadnej podstawy ratyfikacyjnej; niema też naprawdę ich zaufania; ale ma zaufanie w sobie i w swojej przyszłości. Nie jest, jak oni mniemają, dziejowo-politycznym bankrutem, który winien co rychlej przyjąć chociażby najbardziej rujnującą regulacyę swoich interesów; jest narodem dziejowo i politycznie całkiem wypłacalnym, solidnie zagospodarowanym, dorabiającym się, który z ciężkiego swego dorobku nic uronić nie chce i nikomu zaprzepaścić go nie da. Z całą rozwagą, z zupełnym spokojem i ze ścisłym gospodarskim rachunkiem, nie oglądając się na złą poradę lekkomyślnych pośredników, prowadzi on swoje interesa polityczno-dziejowe. I nieinaczej też pojmuje i wyprowadzi będącą teraz na wokandzie sprawę swego stosunku do dzisiejszego przełomu w Rosyi w ogóle i sprawę Królestwa Polskiego w szczególności. „Co siła nam wydrze, — tę wielką naukę dał wielki Deák narodowi węgierskiemu, wstrzymując go całą siłą a z największym dlań pożytkiem od złakomienia się na przygodne koncesye pozorne, a zarazem dał tę naukę wszystkim narodom będącym w położeniu podobnem, — to powrócić może zbieg szczęśliwych okoliczności, lecz co samochcąc zatracimy, to przepadło na zawsze”. Kiedy swego czasu, w chwili zupełnej ruiny i fizycznej bezsilności Polski a najwyższego tryumfu i potęgi Rosyi, nadany był z rąk Aleksandra I prawny stan rzeczy dla gubernii zachodnich i prawno-polityczny dla Królestwa Polskiego, nie było to dziełem przypadku ani aktem filantropii, bo tego niemasz w historyi, ale było wynikiem dobrze zrozumianej konieczności historycznej. Niema żadnej rozumnej racyi, ażeby dziś, śród warunków w gruncie raczej pomyślniejszych, odbiegać zbyt daleko od samych podstaw jedynie koniecznej i zdrowej koncepcyi, chociażby zresztą wymagała ona odpowiednich modyfikacyi w szczegółach. Zaś na tej jedynie dobrej drodze nic nie może być uczynionem bez wypełnienia warunków tak kardynalnych, jak zupełna likwidacya dotychczasowego systemu ucisku narodowości polskiej w Rosyi oraz ustalenie tej rzeczy tak elementarnej i nieuniknionej: polskości Królestwa Polskiego.
