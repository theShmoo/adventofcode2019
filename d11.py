import intcode


class Game(object):
    """docstring for Game"""

    def __init__(self):
        super(Game, self).__init__()
        self.panel = {}
        self.draw_mode = 'x'
        self.next_tile = [None, None]

    def setTile(self, v):
        if self.draw_mode is 'x':
            self.next_tile[0] = v
            self.draw_mode = 'y'
        elif self.draw_mode is 'y':
            self.next_tile[1] = v
            self.draw_mode = 't'
        elif self.draw_mode is 't':
            self.panel[tuple(self.next_tile)] = v
            self.draw_mode = 'x'

    def getTile(self):
        # nothing to do
        return 1


data = [int(x) for x in input().split(',')]
panel = Game()
pc = intcode.Intcode(data, panel.getTile, panel.setTile)
pc.run()


tiles = [p for p in panel.panel.values() if p is 2]

print(len(tiles))
