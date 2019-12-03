def getMass(m):
    new_mass = int(m / 3) - 2
    if new_mass <= 0:
        return 0
    new_mass += getMass(new_mass)
    return new_mass


def solve():
    mass = 0
    while True:
        line = input()
        if line:
            mass += getMass(int(line))
        else:
            break
    print(mass)
