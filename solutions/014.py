# Solution: 837799


from functools import cache


@cache
def collatz(n):
    if n == 1:
        return 1

    return 1 + collatz(n // 2 if n % 2 == 0 else 3 * n + 1)


chain = (0, 0)
for n in range(1, 10**6):
    steps = collatz(n)
    if steps > chain[1]:
        chain = (n, steps)

print(chain[0])
