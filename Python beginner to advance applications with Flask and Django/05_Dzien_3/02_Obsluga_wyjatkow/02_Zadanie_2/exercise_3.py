def divide(a, b):
    try:
        return a/b
    except (ZeroDivisionError, TypeError):
        return None



a  = input('Podaj liczbe:')
b  = input('Podaj liczbe:')


print(divide(a, b))