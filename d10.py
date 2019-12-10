import math


grid = []
while True:
    try:
        grid.append(input())
    except EOFError:
        break

asteroids = []

for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == '#':
            asteroids.append((x, y))


def getVisibleAsteroids(a, asteroids):
    pos = set()
    for b in asteroids:
        if a == b:
            pass
        else:
            rel = (a[0] - b[0], a[1] - b[1])
            length = math.sqrt(rel[0] * rel[0] + rel[1] * rel[1])
            e = (rel[0] / length, rel[1] / length)
            pos.add((round(e[0], 6), round(e[1], 6)))
    return pos


relative_pos = {}
for a in asteroids:
    relative_pos[a] = getVisibleAsteroids(a, asteroids)


distances = {}
for k in relative_pos:
    distances.append(len(relative_pos[k]))


print(max(distances))
