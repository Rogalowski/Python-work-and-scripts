def is_even(number):
    return number % 2 == 0
    # if number % 2 == 0:
    #     return True
    # else:
    #     return False

# print(is_even(1))
# print(is_even(2))


def iterate_through(number):
    for i in range(1, number + 1):
        if is_even(i):
            print(i, "jest liczbą parzystą")
        else:
            print(i, "jest liczbą nieparzystą")


iterate_through(10)