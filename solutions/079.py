# Solution: 73162890


from collections import defaultdict


with open("079.txt", "r") as f:
    numbers = [line.strip() for line in f.readlines()]

order = defaultdict(lambda: set())
for number in numbers:
    for i in range(2):
        if i == 0:
            order[number[i]].add(number[i + 2])
        order[number[i]].add(number[i + 1])

digits = sorted(order.items(), key=lambda x: len(x[1]))

number = ""
while len(digits) > 0:
    first = digits.pop(0)

    digit = first[1].pop()
    number = digit + number

    for other in digits:
        other[1].remove(digit)

    if len(digits) == 0:
        number = first[0] + number

print(int(number))
