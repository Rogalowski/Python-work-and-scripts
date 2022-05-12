def censor(text):
    words = []
    for word in text.split():
        if word in ("Java", "C#", "Ruby", "PHP"):
            words.append("*" * len(word))
        else:
            words.append(word)
    return " ".join(words)
print(censor("Java is the best, but PHP is the bestest!") )
# **** is the best, but **** is the bestest!