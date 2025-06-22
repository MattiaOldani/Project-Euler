# Solution: 73682


def count(coins, current):
    if current > 200:
        return 0

    if len(coins) == 0:
        return 1 if current == 200 else 0

    accept = 0
    for i in range(coins[0][1] + 1):
        accept += count(coins[1:], current + coins[0][0] * i)

    return accept


COINS = [(200, 1), (100, 2), (50, 4), (20, 10), (10, 20), (5, 40), (2, 100), (1, 200)]

print(count(COINS, 0))
