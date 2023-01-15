# Funkcja ma jako wynik, zwrócić listę liczb w podanym zakresie, które jednocześnie są podzielne przez 2 i niepodzielne przez 3.
# Wprowadzony zakres powinien być domknięty, tzn. należy sprawdzić także liczby, które są początkiem i końcem zakresu.

def div(start, end):
    div2 = []
    div3 = []
    for start in range(end+1):  #domkniecie przedzialu <0 do 20>?
        if start % 2 == 0 and start % 3 != 0:
            div2.append(start)
        #if start % 3 == 0:
            #div3.append(start)

    print(div2)
    #print("")
    #print(div3)
    return ""




if __name__ == '__main__':
    result = div(0, 20)
    print(result)
