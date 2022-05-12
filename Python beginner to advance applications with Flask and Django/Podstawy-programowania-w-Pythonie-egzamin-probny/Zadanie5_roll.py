# Napisz funkcję roll, która przyjmie 3 parametry:
#     liczbę kostek,
#     opcjonalnie: typ kostki (dozwolone kostki 3, 4, 6, 8, 10, 12 i 100 ścienne), standardowa wartość, to 6 ,
#     opcjonalnie: modyfikator wyniku (liczba dodana, lub odjęta od wyniku kośćmi), standardowa wartość, to 0.
# Następnie funkcja ma zasymulować rzut odpowiednią liczbą kostek, zsumować wyniki i dodać (lub odjąć) modyfikator. Wynik ma zwrócić.
# Dla uproszczenia możesz przyjąć, że wszystkie liczby podane jako parametry są liczbami naturalnymi.
# Jeśli użytkownik wpisze kostkę, której nie ma w powyższym zestawieniu, funkcja ma wyrzucić wyjątek Exception z komunikatem "No such dice!"


from random import randint

def roll(quantity_dism, type_dism = 6, moderator = 0):
    # try:
       # if type_dism is not (3 or 4 or 6 or 8 or 10 or 12 or 100):
        if type_dism not in (3, 4, 6, 8, 10, 12, 100):
            raise Exception(f"No such dism!: {type_dism}")
        else:
            total = 0
            for i in range(quantity_dism):
                shuffled_points = randint(1, type_dism)
                print(i+1, "los, wynosi:", shuffled_points)
                total += shuffled_points
            print(total + moderator)

    # except: Excption
    # print("No such dice!")

if __name__ == '__main__':

    roll(3, 10, )
    roll(1, 100, -20)
    roll(2, 7,20)