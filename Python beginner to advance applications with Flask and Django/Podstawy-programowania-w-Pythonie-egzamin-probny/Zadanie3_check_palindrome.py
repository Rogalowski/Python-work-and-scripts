# Napisz funkcję check_palindrome, która pobierze dowolnie długi łańcuch tekstowy i sprawdzi, czy jest palindromem. Funkcja powinna zwracać True, jeśli łańcuch jest palindromem, False, jeśli nie jest.
# Podpowiedzi:
#
#     Palindrom to słowo lub zdanie, które czytane wspak brzmi tak samo, jak od początku, np. "kajak", "radar", czy "Kobyła ma mały bok".
#
#     Podczas sprawdzania palindromu, pamiętaj o spacjach.

def check_palindrome(word):


    #for i in range(len(word)):
    print("                Input:", word)
    print("Inverted and no space:", word.replace(" ","")[::-1]) #Replaced " " for "" and printed inverted

    word_no_space_lowered = word.replace(" ","").lower() #word in lower cases with no space

    if word_no_space_lowered == word_no_space_lowered[::-1]:

        print("True")

    else:
        print("False")
    print("")

if __name__ == '__main__':
    check_palindrome("kajak")
    check_palindrome("radar")
    check_palindrome("sdfdsfff")
    check_palindrome("Kobyła ma mały bok")