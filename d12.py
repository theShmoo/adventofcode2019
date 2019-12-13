import itertools
import math

class Moon(object):
    """docstring for Moon"""

    def __init__(self):
        super(Moon, self).__init__()
        self.pos = [0, 0, 0]
        self.velo = [0, 0, 0]

    def applyVelocity(self, to_compute):
        for coord in to_compute:
            self.pos[coord] += self.velo[coord]

    def getPot(self):
        pot = sum([abs(x) for x in self.pos])
        # print("Pot " + str(pot))
        return pot

    def getKin(self):
        kin = sum([abs(x) for x in self.velo])
        # print("kin " + str(kin))
        return kin


moons = []
while True:
    try:
        inp = input()[1:-1]
        pos = []
        moon = Moon()
        for i in inp.split(','):
            pos.append(int(i.strip().split('=')[-1]))
        moon.pos = pos
        moons.append(moon)

    except EOFError:
        break

dim = 3


def getHashForDimension(moons, c):
    return tuple((m.pos[c], m.velo[c]) for m in moons)


start = [0] * dim
for c in range(dim):
    start[c] = getHashForDimension(moons, c)

cycle_idx = [None] * dim

cycle = 0
to_compute = list(range(dim))

while None in cycle_idx:
    cycle += 1
    # grafity combinations:
    for pair in itertools.combinations(moons, 2):
        for coord in to_compute:
            pull_direction = 1
            if pair[0].pos[coord] > pair[1].pos[coord]:
                pull_direction = -1
            elif pair[0].pos[coord] == pair[1].pos[coord]:
                pull_direction = 0
            pair[0].velo[coord] += pull_direction
            pair[1].velo[coord] -= pull_direction

    for m in moons:
        m.applyVelocity(to_compute)

    for c in to_compute:
        if cycle_idx[c] is None:
            if getHashForDimension(moons, c) == start[c]:
                cycle_idx[c] = cycle
                print("Cycle detected in: " + str(c) + " at " + str(cycle))
                to_compute.remove(c)

print(cycle_idx)


def computeLCM(x, y):
    return (x * y) // math.gcd(x, y)


lcm = computeLCM(computeLCM(cycle_idx[0], cycle_idx[1]), cycle_idx[2])
print(lcm)
