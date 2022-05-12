# Napisz funkcję `create_list`, która przyjmie dwa argumenty dowolnego typu, a następnie zwróci listę,
# której kolejne elementy będą parametrami powtórzonymi czterokrotnie.

temp = 15
temp_2 = '15'

# 1. Zmienne mają innne nazwy
# 2. Wskazują na różne obiekty (tzn. o różnych adresach w pamięci)
print(id(temp))
print(id(temp_2))
# 3. Obiekty, na które wskazują zmienne są różnych typów (int, str)
print(type(temp))
print(type(temp_2))

# print(temp + temp_2)  # Nie można dodać liczby do napisu
# print(temp_2 + temp)  # Nie można dodać napisu do liczby

print(temp * temp_2)
print("Hello" * 5)
