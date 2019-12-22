import intcode
import utils


def turn(direction):
    return (direction[1], -direction[0])


def calcNextPos(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])


class Droid(object):
    """docstring for Droid"""

    def __init__(self, grid, data, pos):
        super(Droid, self).__init__()
        self.pc = intcode.Intcode(data, self.getInput, self.setOutput)
        self.grid = grid
        self.pos = pos
        self.next_pos = None

    def getNextPos(self):
        i = 0
        next_dir = (0, 1)
        poss = []
        while i < 4:
            next_pos = self.calcNextPos(pos, next_dir)
            if next_pos in self.grid:
                if self.grid[next_pos] == 1:
                    poss.append((next_pos, i))
            elif self.current_length + 1 < self.best:
                break
            next_dir = turn(next_dir)
            next_pos = self.calcNextPos()
            i += 1

        if next_pos not in self.grid:
            return (next_pos, i)
        else:
            print(poss[0])
            self.current_length -= 1
            self.grid[self.pos] = 4
            return poss[0]

    def setOutput(self, v):
        self.printGrid()
        if v == 0:
            # hit wall
            self.grid[self.next_pos] = 0
        elif v == 1:
            # move one step
            self.grid[self.next_pos] = 1
            self.pos = self.next_pos
            self.current_length += 1
        elif v == 2:
            # found oxygen system
            self.grid[self.next_pos] = 2
            self.pos = self.next_pos
            self.printGrid()
            print("found")

    def getInput(self):
        if self.found:
            return 0
        (self.next_pos, self.dir) = self.getNextPos()
        if self.dir == 0:
            return 1
        elif self.dir == 1:
            return 4
        elif self.dir == 2:
            return 2
        elif self.dir == 3:
            return 3

        print("Error")
        return 0


def printGrid(grid):
    s = list((' ' * 50 + '\n') * 50)
    for p in grid:
        c = '.'
        if grid[p] == 0:
            c = '#'
        elif grid[p] == 1:
            c = '.'
        elif grid[p] == 2:
            c = 'X'
        elif grid[p] == 3:
            c = 'D'
        elif grid[p] == 4:
            c = 'H'
        s[p[1] * 51 + p[0]] = c
    print(str(''.join(s)))


data = [int(x) for x in utils.get_input(2019, 15)[:-1].split(',')]
grid = {}
droid = Droid(grid, data, (0, 0))
droid.pc.run()
