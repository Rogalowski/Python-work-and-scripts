#Napisz funkcję shorten, która przyjmie dowolnie długi napis, po czym zwróci skrót napisu,

def shorten(shortend="Domyslny tekst"):
    new_list = []


    #for i in len(shortend()):
    seperate = shortend.split(" ")
    print(seperate)

    print("I Spospb: ", end="")
    for i in range(len(seperate)):
        print(seperate[i][0].upper(), end="")
        #print(type(seperate))
        new_list.append(seperate[i][0])
    print("")
    print("")

    print("W postaci nowej listy:", new_list)
    print("Wersja krotsza: ", end="")
    x = ("".join(str(i) for i in new_list))
    print(x.upper())
    return ''





if __name__ == '__main__':
    shortend = shorten("Jacek Rogowski pochodze z miasta Szczecin")
    print(shortend)



