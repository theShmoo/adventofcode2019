import intcode


class Droid(object):
    """docstring for Droid"""

    def __init__(self):
        super(Droid, self).__init__()
        self.start_pos = (21, 15)
        self.grid = {}
        self.grid[self.start_pos] = 3
        self.pos = self.start_pos
        self.next_dir = (0, 1)
        self.next_pos = self.next_dir
        self.current_path = []
        self.found = False
        self.best = 395

    def turn(self):
        self.next_dir = (self.next_dir[1], -self.next_dir[0])

    def calcNextPos(self):
        return (self.pos[0] + self.next_dir[0],
                self.pos[1] + self.next_dir[1])

    def getNextPos(self):
        i = 0
        self.next_dir = (0, 1)
        poss = []
        while i < 4:
            next_pos = self.calcNextPos()
            if next_pos in self.grid:
                if self.grid[next_pos] == 1:
                    poss.append((next_pos, i))
            elif self.current_length + 1 < self.best:
                break
            self.turn()
            next_pos = self.calcNextPos()
            i += 1

        if next_pos not in self.grid:
            return (next_pos, i)
        else:
            print(poss[0])
            self.current_length -= 1
            self.grid[self.pos] = 4
            return poss[0]

    def peek(self):
        return self.getNextPos() in self.grid

    def printGrid(self):
        grid = list((' ' * 50 + '\n') * 50)
        for p in self.grid:
            c = '.'
            if self.grid[p] == 0:
                c = '#'
            elif self.grid[p] == 1:
                c = '.'
            elif self.grid[p] == 2:
                c = 'X'
            elif self.grid[p] == 3:
                c = 'D'
            elif self.grid[p] == 4:
                c = 'H'
            grid[p[1] * 51 + p[0]] = c
        print(str(''.join(grid)))

    def setOutput(self, v):
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
            self.found = True
            self.printGrid()
            print("found")
            print(self.current_length)

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


data = [int(x) for x in input().split(',')]
panel = Droid()
pc = intcode.Intcode(data, panel.getInput, panel.setOutput)
pc.run()
