# Napisz funkcję `mean(numbers)`, gdzie `numbers` to lista liczb dowolnego typu.
# Funkcja powinna zwrócić średnią arytmetyczną wszystkich elementów listy numbers.
# Czy znasz jakiś sposób, by ułatwić sobie pracę?


def add(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def mean(numbers):
    return sum(numbers) / len(numbers) if len(numbers) > 0 else 0
    # if len(numbers) > 0:
    #     return add(numbers) / len(numbers)
    # else:
    #     return 0


print(mean([]))
print(mean([1, 2, 3]))
print(mean([3, 3, 3]))
