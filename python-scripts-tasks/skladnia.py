
# To jest komentarz
"To jest string, może działać jako komentarz"
""" To jest string
wielolinijkowy, którego
często używa się
jako komentarz
"""

"tekst"
'tekst'
b"tekst - ciag bitow"
r"tutaj można użyawć \ dowoli np. napisać c:\new"
f"można wstawiać {1+1} albo {[x**2 for x in range(5)]}"
f"{1/3:.2f}"

print("Hello", "world")
a = 1 + 1
print(5/a)  # 2.5
print(5//a)  # 2
print(5 % a)  # 1
print(a+2 + a*2 + a**2)
print("Kot"+"let")
# tak nie można: a = "Falcon" + 9
print("Falcon" + str(9))

# Lektura - metody str: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

print(type(9), type(a))
print(type("Tekstowa"))
print(3e5)  # == float(3 * 10**5)

#    0123456 -->
a = "Programowanie"
#           <--  ^ -1
print(len(a))
print(a[0], '...', a[-1])
print(a[0:4])  # znaki o indeksach od 0 do 3 (4 nie chcemy)
print(a[0:-1], a[0:], a[-1::-1]) # do przedostatniego, do ostatniego, wspak

a = "Pisanie"
if a == "Programowanie":
    print("Let's code")
elif a[0] == 'P':
    print('Do other things starting with "p"')
else:
    print("Something completely different")

if a:  # bool(a)
    print("Mamy a")
else:
    print("Zmienna a jest pusta")

for s in "Salamandra":
    print(s.upper()+"!")

i = 0
while i < 10:
    print(i)
    i += 1  # /= *= **= ...

a = None
if a is None:
    print("w a jest None")

for i in range(101):
    print(i, '-', 100-i)

#'Kot' * 5 == 'Kot'+'Kot'+'Kot'+'Kot'+'Kot'

a = '1435322412'
for n in a:
    print(n, ':', 'x' * int(n))
print()

#zadanie extra:
a = '1,4,3,9,3,12,2,11'
for n in a.split(','):
    print(n, ':', 'x' * int(n))
print()

# listy
a = []
a = list("Python")
print(a)
a = [1, 2, "Cześć", 1==1, None]
a.append(123)
a.extend([3, 4])
a = a + [3, 4]
a[4] = "World"
a[6:8] = ["AAA", "BBB"]
print(a)
for x in a:
    print(x)
print(a[2], a[-1], a[0:3])
# usuwanie
a.pop()
a.pop(2)
del a[1]
del a[2:4]

# list comprehensions
print([x*5 for x in range(5)])
print([x for x in range(10) if x%2==0])

# unpacking
a, b = 1, 2
a, b = [1, 2]
# a, b = [1, 2, 3] # Exception!
a, b, c = "Aa!"  # nie używane, ale działa
print(a, b, c)
for x, y in [[0, 0], [2, 5], [4, 100]]:
    print("Ustaw współrzędne na", x, y)

for n, literka in enumerate("Python"):
    print("Literka nr.", n+1, "to", literka)

for x in reversed("Adam Małysz"):
    print(x, end='')
print()

a = ["Ala", "kot", "piesek"]
print("kot" in a)
print("pies" in a)
a = "Ala, kot i piesek"
print("kot" in a)
print("pies" in a)  # inaczej w list i str

print([i*2 for i in range(50)])
print([i for i in range(100) if i%2==0])
print(list(range(0, 99, 2)))  # tak samo jak slice [0::2]

# tuple
a = ()  # może czytelniej tuple()
a = (1,) # może czytelniej tuple(1)
a = (1, 2, 3)
print(a[0], a[-1])
a += (2, 3)
#a[1] = 1
a = (1, 2) + (3, 4)
tuple(x for x in range(5))  # (x for x in range(5)) - to zwróci generator


#set
b = set()  # pusty set tylko w ten sposób
b = set([1, 2, 3])
c = {2, 3, 4}
#b[0] nie można
for x in b:  # dowolna kolejność
    print(x)
print(1 in b)
print(b & c)  # b.intersection(c)
print(b ^ c)
print(b | c)

#dict
a = {}  # dict()
a = {1: "a", 2: "b", 3: "c"}
a = {True: "a", "hej": (1, 2, 3), 3: [1, 2, 3]}
#a = {[1, 2]: 1, {1, 2}: 1, {1:1}: 1} nie zadziała, klucz nie może być mutowalny
print(a[True], a["hej"], a[3])
a[3] == a.get(3)
a.get(5, 123)  # drugi argument to wartość domyślna, jeśli nie ma klucza 5
a[True] = "bcd"
a[1] = "asdas"  # działa! inaczej niż w list
1 in a # sprawdza w kluczach
1 in a.values()
[x for x in a] # po kluczach
[x for x in a.values()]
for key, value in a.items():
    print("Pod", key, "jest", value)
{x: x**2 for x in range(5)}
{x: y for x, y in [[1, 10], [3, 30]]} == dict([[1, 10], [3, 30]])
# warto wiedzieć o defaultdict

def funkcja():
    pass  # niejawnie zwraca None

def funkcja():
    return 1, 2, 3  # tuple
a, b, c = funkcja()
a = funkcja()

def f1():
    """Dokumentacja"""
    def f2():
        return 1
    return f2() + 1
# f2() - poza f1 nie można

def policz_bmi(waga, wzrost, czy_sportowiec=False):
    bmi = waga / wzrost ** 2
    if czy_sportowiec:
        bmi /= 1.1
    return bmi
print(policz_bmi(100, 1.80))
print(policz_bmi(100, wzrost=1.80))
print(policz_bmi(wzrost=1.80, waga=100))
#print(policz_bmi(waga=100, 1.80))

#uwaga, problem łatwy do przeoczenia
def funkcja(lista_imion=[]): # tak nie można!
    lista_imion.append("Mikołaj")
    print(lista_imion)
#funkcja()
#funkcja()

# funkcja(*[1, 2, 3]) == funkcja(1, 2, 3)
# policz_bmi(wzrost=1.80, waga=100) == policz_bmi(**{"wzrost":1.80, "waga":100})

def sprytna_funkcja(*args, **kwargs):
    print(args) # tupla
    print(kwargs) # dict
sprytna_funkcja(1, 3, "asda", 1.5, asdasdas=1)

#x = input("Podaj wiek: ")
#print(int(x) * 2 - 4)

import przyklad_import  # importy dwawajmy zawsze na początku pliku
przyklad_import.przywitaj("Konrad")

from przyklad_import import przywitaj
przywitaj("Konrad")

from przyklad_import import przywitaj as p
p("Konrad")

class Pies:
    ile_nog = 4
    def __init__(self, szczekanie="Woof"):
        self.szczekanie = szczekanie
    def daj_glos(self):
        "Drukuje na konsole szczekniecie"
        print(self.szczekanie+"!")

rex = Pies()
azor = Pies("Hau")
rex.daj_glos()
azor.daj_glos()
azor.szczekanie = "Wrr"
azor.daj_glos()