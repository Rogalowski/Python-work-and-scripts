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