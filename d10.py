import math


def getVisibleAsteroids(a, asteroids):
    pos = {}
    for b in asteroids:
        if a == b:
            pass
        else:
            rel = (a[0] - b[0], a[1] - b[1])
            length = math.sqrt(rel[0] * rel[0] + rel[1] * rel[1])
            e = (rel[0] / length, rel[1] / length)
            rounded = (round(e[0], 6), round(e[1], 6))
            if rounded not in pos:
                pos[rounded] = (length, b)
            elif pos[rounded][0] > length:
                pos[rounded] = (length, b)

    return [v[1] for v in pos.values()]


def computeAngles(p, visible):
    rad = [math.atan2((v[0] - p[0]), (p[1]) - v[1]) for v in visible]
    degrees = [math.degrees(r) for r in rad]
    return [d if d >= 0 else d + 360 for d in degrees]


def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


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

relative_pos = {}
for a in asteroids:
    relative_pos[a] = getVisibleAsteroids(a, asteroids)

position = max(relative_pos, key=lambda k: len(relative_pos[k]))
print("station: " + str(position))

visible = relative_pos[position]
count = 0
while len(visible) > 0:
    angles = computeAngles(position, visible)
    idx = argsort(angles)
    for c, i in enumerate(idx):
        print((1 + c, visible[i]))
    count = 0
    count += len(idx)
    if count > 200:
        v = visible[idx[199]]
        print("The 200th asteroid to be vaporized is at " + str(v))
        print(v[0] * 100 + v[1])
        break
    else:
        print("next round")
        asteroids = [a for a, i in enumerate(asteroids) if i not in idx]
        visible = getVisibleAsteroids(position, asteroids)
