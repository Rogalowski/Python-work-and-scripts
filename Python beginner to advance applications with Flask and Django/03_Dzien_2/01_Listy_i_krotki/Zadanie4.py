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