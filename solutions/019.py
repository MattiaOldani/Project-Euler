# Solution: 171


def is_leap(year):
    if year % 100 == 0:
        return year % 400 == 0

    return year % 4 == 0


MONTHS = {
    "normal": [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    "leap": [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
}

count = 0

today = 1
for year in range(1901, 2001):
    if is_leap(year):
        months = MONTHS["leap"]
    else:
        months = MONTHS["normal"]

    for month in months:
        today = (today + month) % 7
        if today == 6:
            count += 1

print(count - 1 if today == 6 else count)
