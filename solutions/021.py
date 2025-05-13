# Solution: 31626


def proper_divisors(n):
    divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors += [i]

    return sum(divisors)


numbers = {i: proper_divisors(i) for i in range(10000)}

count = 0
for number, divisors in numbers.items():
    if number == divisors:
        continue

    if numbers.get(divisors, -1) == number:
        count += number

print(count)
