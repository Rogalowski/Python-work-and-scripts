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