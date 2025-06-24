# Solution: 7273


with open("067.txt", "r") as f:
    grid = [list(map(int, line.strip().split())) for line in f.readlines()]

base = len(grid[-1]) * 2 - 1

for i in range(len(grid)):
    extra_zeros = (base - 2 * len(grid[i]) + 1) // 2

    new_line = []
    for el in grid[i]:
        new_line += [el, 0]

    line = (
        [0 for _ in range(extra_zeros)]
        + new_line[:-1]
        + [0 for _ in range(extra_zeros)]
    )

    grid[i] = line

for i, line in enumerate(grid):
    if i == 0:
        continue

    for j, el in enumerate(line):
        if el == 0:
            continue

        grid[i][j] = max(
            el + grid[i - 1][(j - 1) % len(line)], el + grid[i - 1][(j + 1) % len(line)]
        )

print(max(grid[-1]))
