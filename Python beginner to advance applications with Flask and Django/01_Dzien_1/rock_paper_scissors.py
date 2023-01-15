"""
Gra w kamień, papier i nożyce

Zasady:
- nożyce (2) tną papier (3)
- kamień (1) rozgniata nożyce (2)
- papier (3) owija kamień (1)
"""

import random

user_choice = int(input("Wybierz 1-kamień, 2-nożyce, 3-papier: "))
computer_choice = random.randint(1, 3)

print("Gracz:", user_choice, "Komputer:", computer_choice)

if user_choice == computer_choice:
    print("Remis!")
elif user_choice == 1:
    if computer_choice == 2:
        print("Wygrałeś! Kamień rozgniata nożyce")
    elif computer_choice == 3:
        print("Przegrałeś! Papier owija kamień")
elif user_choice == 2:
    if computer_choice == 1:
        print("Przegrałeś! Kamień rozgniata nożyce")
    elif computer_choice == 3:
        print("Wygrałeś! Nożycę tną papier")
elif user_choice == 3:
    if computer_choice == 1:
        print("Wygrałeś! Papier owija kamień")
    elif computer_choice == 2:
        print("Przegrałeś! Nożyce tną papier")
