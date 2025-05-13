# Solution: 31875000


print(
    max(
        [
            a * b * c if a**2 + b**2 == c**2 else 0
            for a in range(1, 999)
            for b in range(1, 1000 - a)
            for c in range(1000 - a - b, 1000 - a - b + 1)
        ]
    )
)
