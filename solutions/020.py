# Solution: 648


def factorial(n):
    if n <= 2:
        return n

    return n * factorial(n - 1)


print(sum([int(x) for x in str(factorial(100))]))
