# -*- coding: cp1250 -*-
import unicodedata

print("Cześć")

with open('test.txt', encoding='cp1250') as f:
    s = f.read()
with open('test2.txt', "w", encoding='cp1250') as f:
    f.write(s)
    f.write("pięć")
print(s)

# Transliteracja: Cześć --> Czesc
s = unicodedata.normalize('NFKD', "Cześć").encode('ascii', 'ignore')
print(s.decode('utf-8'))
# nie działa dla Ł i ł !!!
s = unicodedata.normalize('NFKD', "Łódź").encode('ascii', 'ignore')
print(s.decode('utf-8'))