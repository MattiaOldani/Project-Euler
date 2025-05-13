# Solution: 104743


def is_prime(n):
    if n % 2 == 0:
        return False

    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            return False

    return True


n = 3
counter = 1
while counter < 10001:
    if is_prime(n):
        counter += 1

    n += 2

print(n - 2)
