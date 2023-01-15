# Zadanie 2. (3pkt)
# Napisz funkcję name_sorter, która przyjmie jako parametr listę imion.
# Funkcja ma zwrócić słownik:
#     klucz o nazwie male ma mieć jako wartość imiona męskie z listy wejściowej,
#     klucz o nazwie female ma mieć jako wartość imiona żeńskie z listy wejściowej.
# Dodatkowo, posortuj imiona w ramach swoich list.
# Należy przyjąć, że imiona żeńskie, to te, które kończą się literą "a". Barnabę możemy spokojnie zignorować. ;-)
#
# Przykład:
# names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]
# print(name_sorter(names))
# {'female': ['Alicja', 'Barbara'], 'male': ['Andrzej', 'Cezary', 'Henryk']}

def name_sorter(names):
    list_mal = []
    list_fem = []
    dict = {
        "female":"",
        "male":""
        }

    print("Zenskie: ", end="")
    for i in range(len(names)):
        if names[i][-1] == "a":
            print(names[i], end=" ")
            #dict.update({"female": names[i], })
            list_fem.append(names[i])
    dict.update({"female": list_fem, })


    print("")
    print("Meskie: ", end="")
    for i in range(len(names)):
       if names[i][-1] != "a":
           print(names[i], end=" ")
           #dict.update({"male": names[i]}, )
           list_mal.append(names[i])
    dict.update({"male": list_mal, })

    print("")
    print(dict)

    return ""

if __name__ == '__main__':
    names = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]

    print(name_sorter(names))