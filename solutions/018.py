# Solution: 1074


with open("018.txt", "r") as f:
    grid = [list(map(int, line.strip().split())) for line in f.readlines()]

for i, line in enumerate(grid):
    new_line = []
    for element in line:
        new_line += [element, 0]

    half_padding_len = (33 - len(new_line) - 1) // 2
    zeros = [0 for _ in range(half_padding_len)]
    grid[i] = zeros + new_line[::-1] + zeros

for i in range(1, len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            continue

        grid[i][j] = max(
            grid[i][j] + grid[i - 1][j - 1], grid[i][j] + grid[i - 1][j + 1]
        )

print(max(grid[-1]))
