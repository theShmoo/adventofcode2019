import itertools

class Moon(object):
    """docstring for Moon"""

    def __init__(self):
        super(Moon, self).__init__()
        self.pos = [0, 0, 0]
        self.velo = [0, 0, 0]

    def applyVelocity(self):
        for coord in range(0, 3):
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


print("After 0 steps:")
for m in moons:
    print("pos= " + str(m.pos) + " vel= " + str(m.velo))

for i in range(1, 1001):
    # grafity combinations:
    for pair in itertools.combinations(moons, 2):
        for coord in range(0, 3):
            pull_direction = 1
            if pair[0].pos[coord] > pair[1].pos[coord]:
                pull_direction = -1
            elif pair[0].pos[coord] == pair[1].pos[coord]:
                pull_direction = 0
            pair[0].velo[coord] += pull_direction
            pair[1].velo[coord] -= pull_direction

    for m in moons:
        m.applyVelocity()

    print("After " + str(i) + " steps:")
    total = 0
    for m in moons:
        # print("pos= " + str(m.pos) + " vel= " + str(m.velo))
        p = m.getPot()
        k = m.getKin()
        total += p * k
    print("Total " + str(total))

