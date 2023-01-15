#https://docs.python.org/3/library/doctest.html

def upper(function):
    def wrapper(arg):
        result = function(arg)
        return result.upper()
    return wrapper
@upper
def greet(name):
    return f"Hello, {name}"
print(greet("Bartek"))