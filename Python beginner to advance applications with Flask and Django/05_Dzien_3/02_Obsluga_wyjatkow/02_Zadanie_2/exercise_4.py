def phone(number):
    known_numbers = (
        "555-123-456",
        "123-456-789",
        "333-555-444"
    )
    if number in known_numbers:
        return number
    raise Exception(f"Nie ma takiego numeru: {number}")
print(phone("123-456-789"))
print(phone("333-456-789"))


# def phone(number):
#     number = str(number)
#     number_list = ["1111","22222","3333333","444444"]
#     try:
#         find_index = number_list.index(number)
#         print(number)
#         return number
#     except Exception:
#         print("Nie ma takiego numeru")
#
# phone("1111")

# phone_book = (12121, 2121)
# def phone(number):
#     try:
#         num = number in phone_book
#     except Exception:
#         print("Nie ma takeigo numeru")
#     else:
#         print(num)
#
# print (phone(12121))
# print (phone(3131))