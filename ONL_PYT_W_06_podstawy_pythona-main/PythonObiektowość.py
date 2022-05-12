# Zadanie 2
#
# Stwórz klasę Shape, która ma spełniać następujące wymogi:
#
#     Mieć atrybuty: x, y (określające środek tego kształtu) i color,
#     mieć metodę describe, wypisującą informacje o tym kształcie,
#     mieć metodę distance, zwracającą odległość od innego kształtu; niech metoda przyjmuje jako parametr inny obiekt klasy Shape i liczy odległość od środków obu figur (jak? przypomnij sobie twierdzenie Pitagorasa),
#     mieć nadpisaną metodę __str__ tak, aby po rzutowaniu obiektu do napisu program zwracał: "Figura koloru kolor o środku w punkcie (x, y)".
from math import sqrt

class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


    def describe(self):
        print(self)
        #return f"Shape with {x} width and with {y} lenght got {color}"

    def distance(self, second):
        dx = self.x - second.x
        dy = self.y - second.y
        sum_of_square = dx * dx + dy * dy
        return sqrt(sum_of_square)

    def __str__(self):
        return f"Shape with center point of shape {self.x} and {self.y}  got {self.color} color"

square = Shape(0, 0, "blue")
rectangle = Shape(1, 2, "green")

square.describe()
rectangle.describe()

#odleglosci miedzy jdnym a drugim a drugim i jednym krztaltem
print(square.distance(rectangle))
print(rectangle.distance(square))



# ## Zadanie 3
# Stwórz klasę `BankAccount`, która ma spełniać następujące wymogi:
#
# 1. Mieć atrybuty:
#  * `number` - atrubyt ten powinien trzymać numer identyfikacyjny konta (dla uproszczenia możemy założyć,
# że numerem konta może być dowolna liczba całkowita),
#  * `cash` - atrybut określający ilość pieniędzy na koncie. Ma to być liczba zmiennoprzecinkowa.
# 2. Posiadać konstruktor przyjmujący tylko numer konta. Atrybut `cash` powinien być zawsze nastawiany na 0.0
# dla nowo tworzonego konta.
# 3. Posiadać metodę `deposit_cash(amount)` której rolą będzie zwiększenie wartości atrybutu `cash` o podaną watość.
# Pamiętaj o sprawdzeniu czy podana wartość jest większa od 0.0
# 4. Posiadać metodę `withdraw_cash(amount)` której rolą będzie zmniejszenie wartości atrybutu `cash` o podaną watość.
# Metoda ta powinna zwracać ilość wypłaconych pieniędzy. Dla uproszczenia zakładamy że ilośc pieniędzy na koncie
# nie może zejść poniżej 0.0, np. jeżeli z konta na którym jest 300zł próbujemy wypłacić 500zł to metoda zwroci nam
# tylko 300zł. Pamiętaj o sprawdzeniu czy podana wartość jest większa od 0.0.
# 5. Posiadać metodę `print_info()` nie przyjmującą żadnych parametrów.
# Metoda ta ma wyświetlić informację o numerze konta i jego stanie.

class BankAccount:
    def __init__(self, number):
        int(number)


        self.number = number
        self.cash = 0.0

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
        print(f"BanckAccount, {self.number} have: {self.cash} cash")
        #return f"BanckAccount, {self.number} have: {self.cash}"



kowalski = BankAccount(11111)
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


#
# ## Zadanie 1 &ndash; zadanie rozwiązywane z wykładowcą.
# Stwórz klasę `Calculator`. Konstruktor ma nie przyjmować żadnych danych.
# Każdy nowo stworzony obiekt powinien mieć pustą
# listę, w której będzie trzymać historię wywołanych operacji (stwórz ją w konstruktorze).
# Następnie dodaj do klasy następujące metody:
#
# 1. `add(num1, num2)` &ndash; metoda ma dodać do siebie dwie zmienne i zwrócić wynik.
# Dodatkowo na liście operacji ma zapamiętać napis: "added `num1` to `num2` got `result`".
# 2. `multiply(num1, num2)` &ndash; metoda ma pomnożyć przez siebie dwie zmienne i zwrócić wynik.
# Dodatkowo na liście operacji ma zapamiętać napis: "multiplied `num1` with `num2` got `result`".
# 5. `print_operations()` &ndash; metoda ma wypisać wszystkie zapamiętane operacje.
#
# Pamiętaj o używaniu `self` w odpowiednich miejscach.
# Stwórz kilka kalkulatorów i przetestuj ich działanie.
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

calc = Calculator()
calc2 = Calculator()

x = calc.add(2, 2)
calc2.add(3, 3)
y = calc.multiply(3, 5)
calc.add(x, y)
calc2.multiply(10, 10)

calc.print_operations()
print("----------------------")
calc2.print_operations()


# ## Zadanie 4
# Stwórz klasę `Employee`, która ma spełniać następujące wymogi:
#
# 1. Mieć atrybuty:
#  * `id` - atrubyt ten powinien trzymać numer identyfikacyjny pracownika,
#  * `first_name` - atrybut określający imię pracownika,
#  * `last_name` - atrybut określający nazwisko pracownika,
#  * `_salary` - atrybut określający ile pracownik zarabia za godzinę. Zwróć uwagę na podkreślenie, które mówi,
# że atrybut ten nie powinien być dostępny poza klasą.
# 2. Posiadać konstruktor przyjmujący id, imię, nazwisko.
# 3. Posiadać metodę `set_salary(salary)` której rolą będzie ustawienie wartości atrybutu `salary`.
# Pamiętaj o sprawdzeniu czy podana wartość jest:
#  * Wartością numeryczną,
#  * Wieksza (lub równa) od 0.0.
#
# #### hint: jeśli chcesz sprawdzić typ zmiennej użyj funkcji `isinstance()`: https://docs.python.org/3/library/functions.html#isinstance


class Employee:
    def __init__(self, id, imie, nazwisko):
        self.id = id
        self.first_name = imie
        self.last_name = nazwisko
        self._salary = None

    def set_salary(self, salary):
        if not isinstance(salary, (int, float)):
            raise ValueError(f"Argument powinien być liczbą: {salary} ({type(salary)})")
        elif salary < 0.0:
            raise ValueError(f"Argument powinien być nieujemny: {salary}")
        else:
            self._salary = salary

    def __str__(self):
        return f"Pracownik {self.id}: {self.first_name} {self.last_name} ma stawkę {self._salary}"

emp1 = Employee(1, "Jan", "Kowalski")
emp2 = Employee(2, "Karol", "Nowak")

print(emp1)
print(emp2)

emp1.set_salary(15)
emp2.set_salary(100)

print(emp1)
print(emp2)

try:
    emp1.set_salary(-400)
except ValueError as e:
    print(e)

try:
    emp1.set_salary("400")
except ValueError as e:
    print(e)

try:
    emp2.set_salary("figa")
except ValueError as e:
    print(e)

try:
    emp2.set_salary(emp1)
except ValueError as e:
    print(e)

print(emp1)
print(emp2)




# ## Zadanie 1. – rozwiązywane z wykładowcą

# Zajrzyj do pliku **exercise_1.py**, znajdziesz tam klasę `Dinosaur`, która ma zaimplementowane następujące elementy:

# * metodę `walk()`,
# * metodę `make_sound()`.

# Napisz klasę `Bird`, która będzie dziedziczyła po klasie `Dinosaur`. Klasa `Bird` ma:

# * dostać nową metodę `fly()`, która będzie zwracała napis "Latam!",
# * nadpisać metodę `make_sound()`, która ma zwracać napis "Ćwir ćwir!".

# Przetestuj nową klasę.



class Dinosaur:

    def walk(self):
        return "Chodzę!"

    def make_sound(self):
        return "Roar!"


if __name__ == "__main__":
    d = Dinosaur()
    print("Dinozaur chodzi:")
    print(d.walk(), "\n")  # "\n" to znak oznaczający nową linię.

    print("Dinozaur wydaje dźwięk:")
    print(d.make_sound())






    # Zadanie 2
#
# Stwórz klasę Circle, która ma spełniać następujące wymogi:
#
#     Dziedziczyć po klasie definiującej kształt (zdefiniowanej przez nas wcześniej).
#     Mieć dodatkowy atrybut radius definiujący promień okręgu.
#     Mieć inicjującą przyjmującą zmienne określające wartości x, y, color i radius.
#     Metoda ta powinna wypisywać informacje o właśnie stworzonym okręgu (użyj do tego jednej z metod).
#     Nadpisywać metody klasy Shape (nadpisz tylko te, które tego wymagają).
#     Mieć funkcję area, zwracającą pole powierzchni.
#     Mieć funkcję perimeter zwracającą obwód.
#
# Hint: Wartość π znajdziesz w pakiecie math w zmiennej pi:
#
# import math
#
# print(math.pi)  # używaj do woli!

from math import sqrt
from math import pi



class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


    def describe(self):
        print(self)
        #return f"Shape with {x} width and with {y} lenght got {color}"

    def distance(self, second):
        dx = self.x - second.x
        dy = self.y - second.y
        sum_of_square = dx * dx + dy * dy
        return sqrt(sum_of_square)

    def __str__(self):
        return f"Shape with center point of shape {self.x} and {self.y}  got {self.color} color"

class Circle(Shape):
    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color)
        self.radius = radius
        self.describe()

    def describe(self):
        super().describe()
        print("Circle with radius:", self.radius)


    def area(self):
        field = pi * self.radius**self.radius
        return field

    def perimeter(self):
        return 2 * 3.14 * self.radius


square = Shape(0, 0, "blue")
rectangle = Shape(1, 2, "green")
circle = Circle(1, 1, "red", 1)


square.describe()
rectangle.describe()

#odleglosci miedzy jdnym a drugim a drugim i jednym krztaltem
print("Odleglosc A B:", square.distance(rectangle))
print("Odleglosc B A:", rectangle.distance(square))
print("Pole:", circle.area())
print("Powierzchnia:", circle.perimeter())






# Zadanie 3
#
# Stwórz klasę HourlyEmployee, która ma reprezentować pracownika któremu pracodawca płaci za godziny. Klasa ma spełniać następujące wymogi:
#
#     Dziedziczyć po klasie Employee.
#     Mieć dodatkową metodę compute_payment(hours), która będzie zwracała kwotę do wypłacenia pracownikowi za liczbę wypracowanych godzin.



class Employee:
    def __init__(self, id, imie, nazwisko):
        self.id = id
        self.first_name = imie
        self.last_name = nazwisko
        self._salary = None

    def set_salary(self, salary):
        if not isinstance(salary, (int, float)):
            raise ValueError(f"Argument powinien być liczbą: {salary} ({type(salary)})")
        elif salary < 0.0:
            raise ValueError(f"Argument powinien być nieujemny: {salary}")
        else:
            self._salary = salary

    def __str__(self):
        return f"Pracownik {self.id}: {self.first_name} {self.last_name} ma stawkę {self._salary}"

class HourlyEmployee(Employee):
    def __init__(self, id, imie, nazwisko, hours):
        super().__init__(id, imie, nazwisko)
        self.hours = hours

    def compute_payment(self):
        return self._salary * self.hours




emp1 = Employee(1, "Jan", "Kowalski")
emp2 = Employee(2, "Karol", "Nowak")
emp3 = HourlyEmployee(3, "Jacek", "Rogowski", 100)

print(emp1)
print(emp2)

emp1.set_salary(15)
emp2.set_salary(100)

print(emp1)
print(emp2)

try:
    emp1.set_salary(-400)
except ValueError as e:
    print(e)

try:
    emp1.set_salary("400")
except ValueError as e:
    print(e)

try:
    emp2.set_salary("figa")
except ValueError as e:
    print(e)

try:
    emp2.set_salary(emp1)
except ValueError as e:
    print(e)

print(emp1)
print(emp2)


emp3.set_salary(20)
print(emp3.compute_payment())
print(emp3, ",przepracował:", emp3.hours, "godzin i zarobił:", emp3.compute_payment())


######################################################################################################################


# class Employee:
#     def __init__(self, id, imię, nazwisko):
#         self.id = id
#         self.first_name = imię
#         self.last_name = nazwisko
#         self._salary = None
#
#     def set_salary(self, salary):
#         if not isinstance(salary, (int, float)):
#             raise ValueError(f"Argument powinien być liczbą: {salary} ({type(salary)})")
#         elif salary < 0.0:
#             raise ValueError(f"Argument powinien być nieujemny: {salary}")
#         else:
#             self._salary = salary
#
#     def __str__(self):
#         return f"Pracownik {self.id}: {self.first_name} {self.last_name} ma stawkę {self._salary}"
#
# class HourlyEmployee(Employee):
#     def compute_payment(self, hours):
#         return self._salary * hours
#
# emp1 = HourlyEmployee(1, "Jan", "Kowalski")
# emp2 = HourlyEmployee(2, "Karol", "Nowak")
#
# print(emp1)
# print(emp2)
#
# emp1.set_salary(15)
# emp2.set_salary(100)
#
# print(emp1, "dostaje", emp1.compute_payment(40))
# print(emp2, "dostaje", emp2.compute_payment(3))






 