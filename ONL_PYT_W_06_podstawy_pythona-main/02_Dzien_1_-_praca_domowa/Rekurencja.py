def countdown(n):
    print(n)
    if n > 0:
        countdown(n - 1)

# countdown(10)

# def factorial(n):
#     # n! = 1 * 2 * ... * (n-1) * n
#     if n < 2:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(1))
# print(factorial(4))


def is_palindrome(word):
    # return word == word[::-1]
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome(word[1:-1])

print(is_palindrome("foo"))
print(is_palindrome("ana"))
print(is_palindrome("kajak"))
print(is_palindrome("hello"))
