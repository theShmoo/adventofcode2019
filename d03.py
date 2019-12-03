def addCells(grid, w, pos, le):
    for i in range(int(w[1:])):
        x = pos[0]
        y = pos[1]
        d = w[0]
        if d == "R":
            x += 1
        elif d == "L":
            x -= 1
        elif d == "U":
            y += 1
        elif d == "D":
            y -= 1
        pos = (x, y)
        le += 1
        if pos not in grid:
            grid[pos] = le
    return (pos, le)


i1 = input()
i2 = input()
w1 = i1.split(",")
w2 = i2.split(",")

pos = (0, 0)
l1 = 0
gridx = {}
for w in w1:
    (pos, l1) = addCells(gridx, w, pos, l1)
pos = (0, 0)
l2 = 0
gridy = {}
for w in w2:
    (pos, l2) = addCells(gridy, w, pos, l2)

inters = set(gridx.keys()).intersection(set(gridy.keys()))
lengths = []
for i in inters:
    le = gridx[i] + gridy[i]
    lengths.append(le)
print(min(lengths))
