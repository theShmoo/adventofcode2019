import intcode
import utils


class Droid(object):

    def __init__(self):
        super(Droid, self).__init__()
        self.grid = []
        self.current_line = []
        self.width = 0
        self.height = 0
        self.neighborhoods = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def printGrid(self):
        s = ""
        for line in self.grid:
            s += str(''.join(line)) + "\n"
        print(s)

    def getNumNeighbors(self, x, y):
        num = 0
        if self.grid[y][x] != '#':
            return 0

        for n in self.neighborhoods:
            check_x = x + n[0]
            check_y = y + n[1]
            if check_x > 0 and check_x < self.width:
                if check_y > 0 and check_y < self.height:
                    if self.grid[check_y][check_x] == '#':
                        num += 1
        return num

    def setOutput(self, v):
        if v > 127:
            print(f"{v} dust collected")

        if v == 10:
            self.grid.append(self.current_line)
            if len(self.current_line) > 0:
                self.width = len(self.current_line)
                self.height += 1
                self.current_line = []
        else:
            self.current_line.append(chr(v))

    def getInput(self):
        return 0


data = [int(x) for x in utils.get_input(2019, 17).split(',')]
data[0] = 2
droid = Droid()
pc = intcode.Intcode(data, droid.getInput, droid.setOutput)
pc.run()

droid.printGrid()

intersections = []
for x in range(droid.width):
    for y in range(droid.height):
        if droid.getNumNeighbors(x, y) > 2:
            intersections.append((x, y))

print(intersections)
s = [i[0] * i[1] for i in intersections]
print(sum(s))

