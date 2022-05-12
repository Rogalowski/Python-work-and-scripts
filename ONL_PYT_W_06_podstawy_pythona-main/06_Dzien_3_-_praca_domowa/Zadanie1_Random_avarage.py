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