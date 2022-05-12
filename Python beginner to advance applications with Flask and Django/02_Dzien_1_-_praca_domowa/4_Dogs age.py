def dogs_age(age_of_dog):
    if age_of_dog <= 2:
        return age_of_dog * 10.5
    return 2 * 10.5 + (age_of_dog - 2) * 4

print("Azor: ", dogs_age(1.5))
print("Burek:",dogs_age(5))