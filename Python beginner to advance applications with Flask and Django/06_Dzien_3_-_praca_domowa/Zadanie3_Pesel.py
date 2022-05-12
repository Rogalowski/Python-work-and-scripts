def validate_pesel(text):
    if not isinstance(text, str):
        raise TypeError(f"Expected a string but got {type(text).__name__}")
    if not text.isdigit():
        raise ValueError("Expected a string with digits")
    if len(text) != 11:
        raise ValueError("PESEL must be exactly 11 digits long")

    weights = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
    digits = [int(x) for x in text]  # list(map(int, text))

    control = 10 - sum([int(x)*y for x, y in zip(digits[:10], weights)]) % 10

    if control == 10:
        control = 0

    return control == digits[-1]


non_text = 264736478
non_digits = "26e73,478"
too_short = "1234"
too_long = "123456789000"
bad_pesel = "44051401358"
ok_pesel = "90070543671"

# validate_pesel(non_text)
# validate_pesel(non_digits)
# validate_pesel(too_short)
# validate_pesel(too_long)
print(validate_pesel(bad_pesel))
print(validate_pesel(ok_pesel))

validate_pesel(bad_pesel)
