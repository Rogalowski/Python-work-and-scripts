def check_palindrome(word):
    return word == word[::-1]



palindrome = check_palindrome("kajak")
if palindrome:
    print("Yes")
else:
    print("No")
palindrome = check_palindrome("tak")
if palindrome:
    print("Yes")
else:
    print("No")
############################################################################
x = "malayalam"
w = ""
for i in x:
    w = i + w

if (x == w):
    print("Yes")
else:
    print("No")