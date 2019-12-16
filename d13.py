import intcode
import time


class Game(object):
    """docstring for Game"""

    def __init__(self):
        super(Game, self).__init__()
        self.panel = {}
        self.draw_mode = 'x'
        self.next_tile = [None, None]
        self.ball_pos = [0, 0]
        self.paddle_pos = 0

    def printGame(self):
        grid = list(('.' * 35 + '\n') * 23)
        for p in self.panel:
            c = '.'
            if self.panel[p] == 1:
                c = '#'
            elif self.panel[p] == 2:
                c = 'x'
            elif self.panel[p] == 3:
                c = '-'
                self.paddle_pos = p[0]
            elif self.panel[p] == 4:
                c = 'o'
                self.ball_pos = p[0]
            grid[p[1] * 36 + p[0]] = c
        print(str(''.join(grid)))
        time.sleep(.1)

    def setTile(self, v):
        if self.draw_mode == 'x':
            self.next_tile[0] = v
            self.draw_mode = 'y'
        elif self.draw_mode == 'y':
            self.next_tile[1] = v
            self.draw_mode = 't'
        elif self.draw_mode == 't':
            if(self.next_tile[0] < 0):
                print("Current Score: " + str(v))
            else:
                self.panel[tuple(self.next_tile)] = v
            self.draw_mode = 'x'

    def getTile(self):
        self.printGame()
        if self.paddle_pos < self.ball_pos:
            return 1
        elif self.paddle_pos > self.ball_pos:
            return -1
        return 0


data = [int(x) for x in input().split(',')]
panel = Game()
pc = intcode.Intcode(data, panel.getTile, panel.setTile)
pc.run()
