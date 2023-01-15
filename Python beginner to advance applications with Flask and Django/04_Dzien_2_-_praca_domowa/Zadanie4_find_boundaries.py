def find_boundaries(elements):
    converted =  tuple(i for i in elements)
    #for i in number:
    #list.append(elements)
    #return tuple(list)
    print(type(converted))
  #  j = 0
   # for j in elements:

         #   return f"{min(elements)}, {max(converted)}"


    print("Zmieniono na tuple:",converted)

    return f"{min(converted)}, {max(converted)}"



# def convert(list):
#     return tuple(i for i in list)
# # Driver function
# list = [1, 2, 3, 4]
# print(convert(list))

b = find_boundaries([1, 5, 2, 3.5, -1])
print(b)
#(-1, 5)
b = find_boundaries([0, 2.5, "a kuku!", 10])
print(b)
#(0, 10)