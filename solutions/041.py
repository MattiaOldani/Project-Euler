# Solution: 7652413


from itertools import permutations


def is_prime(n):
    if n % 2 == 0:
        return False

    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            return False

    return True


max_pandigital = 0

for i in range(9, 1, -1):
    for permutation in permutations([x for x in range(1, i + 1)]):
        n = int("".join([str(p) for p in permutation]))
        if is_prime(n):
            max_pandigital = max(max_pandigital, n)

    if max_pandigital > 0:
        break

print(max_pandigital)
