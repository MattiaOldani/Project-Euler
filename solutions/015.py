# Solution: 137846528820


grid = [[1] + [0 for _ in range(20)] for _ in range(21)]
grid[0] = [1 for _ in range(21)]

for i in range(1, 21):
    for j in range(1, 21):
        grid[i][j] += grid[i - 1][j] + grid[i][j - 1]

print(grid[-1][-1])
