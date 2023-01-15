#https://docs.python.org/3/library/doctest.html

import time
def timed(function):
    def wrapper(a, b):
        t1 = time.time()
        result = function(a, b)
        t2 = time.time()
        print("Funkcja wykonywała się przez", t2 - t1)
        return result
    return wrapper
# Dekoratory wbudowane w Pythona:
# @property
# @classmethod
# @staticmethod
# Własny dekorator, krtóry sam zdefiniowałem:
# @timed
@timed
def div(a, b):
    return a / b
@timed
def add(a, b):
    return a + b
# div = timed(div)
# add = timed(add)
print(div(3, 4))
print(add(3, 4))