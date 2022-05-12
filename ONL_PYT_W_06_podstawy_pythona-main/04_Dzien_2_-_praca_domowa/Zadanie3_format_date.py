def format_date(day, month, year):

    if day in range (1, 31) and month in range (1, 12):
        if month == 1: month = "styczen"
        elif month == 2: month = "luty"
    else:
        return

    return print(day, month, year)



d = format_date(12, 2, 2017)
print(d)

d = format_date(12, 13, 2017)
print(d)