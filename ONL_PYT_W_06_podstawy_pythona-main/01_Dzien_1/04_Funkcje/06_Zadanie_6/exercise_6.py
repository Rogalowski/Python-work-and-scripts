
#ZADANIE 6

def calculate_net(gross, vat):
    print("Brutto:", gross, "Vat:", vat, )
    return gross - gross * vat * 0.01

print("Netto kwota to", calculate_net(100,23))
print(f"{calculate_net}.2f")

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


