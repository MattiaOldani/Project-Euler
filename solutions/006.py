# Solution: 25164150


"""
print(((100 * 101) // 2) ** 2 - (100 * 101 * 201) // 6)
"""


print(sum(range(1, 101)) ** 2 - sum(x**2 for x in range(1, 101)))
