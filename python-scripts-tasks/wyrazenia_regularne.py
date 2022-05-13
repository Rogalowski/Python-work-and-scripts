import re

s = "Ala ma kota. Ala ma mruczka."

print(re.findall("a", s))
print(re.findall("Ala", s))
print(re.findall("ala", s, re.I))  # case-insensitive

print(re.findall(".a", s))
print(re.findall(r"..\.", s))
print(re.findall(r" .*\.", s))  # operator zachłanny

print(re.findall("[aeiout]+", s))
print(re.findall("[^aeiout]+", s))

print(re.findall(r" [^ ]*\.", s))
print(re.findall(r" ([^ ]*)\.", s))  # "grupy"

s = "<b>this is <i>cool</i></b>"
print(re.findall(r"<(.*?)>", s))
print(re.findall(r"\w+", s))