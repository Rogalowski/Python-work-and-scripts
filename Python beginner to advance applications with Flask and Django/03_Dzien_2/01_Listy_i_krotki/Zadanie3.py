# Napisz funkcję `find_short_words`, która przyjmie listę wyrazów.
# Funkcja powinna zwrócić listę słów krótszych od 5 znaków.

def find_short_words(words):
    short = []
    for word in words:
        if len(word) < 5:
            short.append(word)
    return short

    # for i in len.words[i]:
    #     i += 1
    #     if len.words[i] == 3:
    #         return words[]


l = find_short_words(['Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie'])

print(l)