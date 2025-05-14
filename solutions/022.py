# Solution: 871198282


def name_score(name):
    return sum([ord(c) % 65 + 1 for c in name])


with open("022.txt", "r") as f:
    names = sorted(
        [x.removeprefix('"').removesuffix('"') for x in f.read().strip().split(",")]
    )

scores = 0
for i, name in enumerate(names):
    scores += (i + 1) * name_score(name)

print(scores)
