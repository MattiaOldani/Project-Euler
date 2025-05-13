# Solution: 4613732


def fibonacci_numbers():
    numbers = [1, 2]

    while numbers[-1] < 4 * 10**6:
        numbers += [numbers[-1] + numbers[-2]]

    return filter(lambda x: x % 2 == 0, numbers[:-1])


print(sum(fibonacci_numbers()))
