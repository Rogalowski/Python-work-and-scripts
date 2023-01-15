from random import randint

guessed = False
rnd = randint(1, 2)

while not guessed:
    try:
        str_num = input("Podaj liczbę:")
        num = int(str_num)
        if num == rnd:
           print("Brawo!")
           guessed = True
        else:
           print("Pudło!")

    except ValueError:
        print('Błąd nie podałeś liczby!!!')

# while not guessed:
#
#         str_num = input("Podaj liczbę:")
#       try:
#         num = int(str_num)
#       except ValueError:
#           print('Błąd nie podałeś liczby!!!')
#       else:
#         if num == rnd:
#            print("Brawo!")
#            guessed = True
#         else:
#            print("Pudło!")
#
