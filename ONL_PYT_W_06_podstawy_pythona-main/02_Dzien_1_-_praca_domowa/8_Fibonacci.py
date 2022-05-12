
#Wersja rekurencyjna:
def fib(n):
    return 1 if n< 3 else fib(n - 2) + fib(n - 1)


def fib(n):
    # print(f"fib({n})")
    if n < 3:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

for i in range(1, 10):
    print("ID:", i, "Fib:", fib(i))

    # Wersja iteracyjna:
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return  a

print(fib(10))