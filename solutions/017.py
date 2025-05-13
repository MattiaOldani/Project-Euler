# Solution: 21124


LOOKUP = {
    "1": 3,
    "2": 3,
    "3": 5,
    "4": 4,
    "5": 4,
    "6": 3,
    "7": 5,
    "8": 5,
    "9": 4,
    "10": 3,
    "11": 6,
    "12": 6,
    "13": 8,
    "14": 8,
    "15": 7,
    "16": 7,
    "17": 9,
    "18": 8,
    "19": 8,
    "20": 6,
    "30": 6,
    "40": 5,
    "50": 5,
    "60": 5,
    "70": 7,
    "80": 6,
    "90": 6,
}

count = 0
for i in range(1, 1000):
    i = str(i)

    if i in LOOKUP:
        count += LOOKUP[i]
        continue

    if len(i) == 2:
        count += LOOKUP[i[0] + "0"] + LOOKUP[i[1]]
        continue

    count += LOOKUP[i[0]] + 7

    i = i[1:]
    if i == "00":
        continue

    count += 3

    i = str(int(i))

    if i in LOOKUP:
        count += LOOKUP[i]
        continue

    count += LOOKUP[i[0] + "0"] + LOOKUP[i[1]]

print(count + 11)
