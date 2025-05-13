# Solution: 906609


print(
    max(
        [
            m * n if str(m * n) == str(m * n)[::-1] else 0
            for m in range(100, 1000)
            for n in range(100, 1000)
        ]
    )
)
