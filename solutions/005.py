# Solution: 232792560


"""
print(5 * 7 * 9 * 11 * 13 * 16 * 17 * 19)
"""


from collections import defaultdict
from functools import reduce


def get_prime_factors(n):
    primes = defaultdict(lambda: 0)
    for i in range(2, n + 1):
        while n % i == 0:
            primes[i] += 1
            n //= i

    return primes.items()


factors = defaultdict(lambda: 0)
for n in range(2, 21):
    for factor, repetition in get_prime_factors(n):
        factors[factor] = max(factors[factor], repetition)

print(reduce(lambda x, y: x * (y[0] ** y[1]), factors.items(), 1))
