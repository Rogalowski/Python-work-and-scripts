import random

# #Zadanie1
# no_of_stars = random.randint(1, 20)
# print (no_of_stars)
# print (no_of_stars * "*")

# i = 0
# # while i <= no_of_stars:
# #     i += i
# #     print ("*")


#Zadanie2

rows = random.randint(5, 15)
columns = random.randint(5, 15)

# while rows <= columns:
print("Wartosc rows:", columns)
print("Wartosc colums:", rows)
# print(rows * "*")


for i in range (columns):
    print(rows * "*")

#Zadanie3

size = random.randint(3, 9)
print("Wielkosc choinki:", size)

for i in range(1, size + 1):
    print("*" * i)

print("DRUGI SPOSOB:")
for i in range(1, size + 1):
    for n in range(i):
        print("*", end="")
    print("")
