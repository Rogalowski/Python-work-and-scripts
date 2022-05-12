import random
from coderslab import words

#print(coderslab.random_word())

def random_word():
    return random.choice(words)

print(random_word())