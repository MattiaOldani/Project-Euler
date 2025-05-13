# Solution: 6857


def is_prime(n):
    if n % 2 == 0:
        return False

    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            return False

    return True


N = 600851475143

i = 3
max_prime = 0
while i <= N:
    if not is_prime(i):
        i += 2
        continue

    while N % i == 0:
        max_prime = max(max_prime, i)
        N //= i

    i += 2

print(max(max_prime, N))
