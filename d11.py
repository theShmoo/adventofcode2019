import intcode


class Panel(object):
    """docstring for Panel"""

    def __init__(self):
        super(Panel, self).__init__()
        self.panel = {(0, 0): 1}
        self.position = (0, 0)
        self.direction = (0, 1)
        self.draw_mode = True

    def turnLeft(self):
        d = self.direction
        self.direction = (-d[1], d[0])

    def turnRight(self):
        d = self.direction
        self.direction = (d[1], -d[0])

    def setTile(self, x):
        if self.draw_mode:
            self.panel[self.position] = x
        else:
            self.turnLeft() if x == 0 else self.turnRight()
            self.position = (self.position[0] + self.direction[0],
                             self.position[1] + self.direction[1])
        self.draw_mode = not self.draw_mode

    def getTile(self):
        color = self.panel[self.position] if self.position in self.panel else 0
        return color


data = [int(x) for x in input().split(',')]
panel = Panel()
pc = intcode.Intcode(data, panel.getTile, panel.setTile)
pc.run()

grid = list(('.' * 42 + '\n') * 6)
for p in panel.panel:
    if panel.panel[p] is 1:
        grid[abs(p[1]) * 43 + p[0]] = '#'

print(str(''.join(grid)))
