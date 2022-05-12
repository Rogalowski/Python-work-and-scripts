def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Nie dzieli sie przez 0")



try:
    a  = int(input('Podaj liczbe:'))
    b  = int(input('Podaj liczbe:'))
except (TypeError, ValueError, NameError):
    print("Nie podales liczby")
    #return print("Nie podales liczb")
except ZeroDivisionError:
    print("Nie dzieli sie przez 0")
print(div(a, b))