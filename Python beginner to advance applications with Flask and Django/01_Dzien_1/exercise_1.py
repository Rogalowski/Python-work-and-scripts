import math

# tutaj napisz funkcję z zadania 1
def square(num):
    return num**2
    # return num*num
    # return int(math.pow(num, 2))

# poniższe linijki przetestują Twoją funkcję:
print("2 podniesione do potęgi drugiej, to:", square(2))  # powinno być 4
print("16^2=", square(16))  # powinno być 256
print("256 do potęgi 2 =", square(256))  # powinno być 65536

def square_print(num):
    print(num**2)


a = square(10) + 10
b = square_print(10) + 10
