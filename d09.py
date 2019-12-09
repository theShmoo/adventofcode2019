import copy


def get_digit(number, n):
    return number // 10**(1 + n) % 10


class Intcode(object):
    """docstring for Intcode"""

    def __init__(self, code):
        super(Intcode, self).__init__()
        self.code = copy.copy(code)
        self.additional_memory = {}
        self.ins = 0
        self.relative_base = 0

    def getModeForParam(self, pos):
        val = self.read(self.ins)
        mode = get_digit(val, pos)
        # print("val " + str(val) + " pos: " + str(pos) + " mode: " + str(mode))
        return mode

    def checkMemorySize(self, pos):
        available_size = len(self.code)
        if available_size <= pos:
            self.code.extend([0] * (pos - available_size + 1))

    def read(self, pos):
        self.checkMemorySize(pos)
        return self.code[pos]

    def getParamByMode(self, pos):
        mode = self.getModeForParam(pos)
        p1 = self.read(self.ins + pos)
        if mode == 0:
            # position mode
            return self.read(p1)
        elif mode == 1:
            # immediate mode
            return p1
        elif mode == 2:
            # relative base mode
            return self.read(self.relative_base + p1)
        else:
            print("Error")
            return None

    def setValueAtPos(self, pos, val):
        self.checkMemorySize(pos)
        self.code[pos] = val

    def setValueByMode(self, relpos, val):
        mode = self.getModeForParam(relpos)
        pos = self.read(self.ins + relpos)
        if mode == 0:
            self.setValueAtPos(pos, val)
        elif mode == 1:
            print("immediate mode is not writable")
        elif mode == 2:
            self.setValueAtPos(self.relative_base + pos, val)

    def add(self):
        p1 = self.getParamByMode(1)
        p2 = self.getParamByMode(2)
        self.setValueByMode(3, p1 + p2)
        self.ins += 4

    def mul(self):
        p1 = self.getParamByMode(1)
        p2 = self.getParamByMode(2)
        self.setValueByMode(3, p1 * p2)
        self.ins += 4

    def input(self, inp):
        print("input: ")
        self.setValueByMode(1, inp)
        self.ins += 2

    def output(self):
        p1 = self.getParamByMode(1)
        print("Out: " + str(p1))
        self.ins += 2

    def jumpIfTrue(self):
        p1 = self.getParamByMode(1)
        p2 = self.getParamByMode(2)
        if p1:
            self.ins = p2
        else:
            self.ins += 3

    def jumpIfFalse(self):
        p1 = self.getParamByMode(1)
        p2 = self.getParamByMode(2)
        if not p1:
            self.ins = p2
        else:
            self.ins += 3

    def lessThan(self):
        p1 = self.getParamByMode(1)
        p2 = self.getParamByMode(2)
        self.setValueByMode(3, 1 if p1 < p2 else 0)
        self.ins += 4

    def equals(self):
        p1 = self.getParamByMode(1)
        p2 = self.getParamByMode(2)
        self.setValueByMode(3, 1 if p1 == p2 else 0)
        self.ins += 4

    def relativeBaseOffset(self):
        p1 = self.getParamByMode(1)
        self.relative_base += p1
        self.ins += 2

    def run(self, inp):
        while self.code[self.ins] % 100 != 99:
            opcode = self.code[self.ins] % 100
            if opcode == 1:
                self.add()
            elif opcode == 2:
                self.mul()
            elif opcode == 3:
                self.input(inp)
            elif opcode == 4:
                self.output()
            elif opcode == 5:
                self.jumpIfTrue()
            elif opcode == 6:
                self.jumpIfFalse()
            elif opcode == 7:
                self.lessThan()
            elif opcode == 8:
                self.equals()
            elif opcode == 9:
                self.relativeBaseOffset()


data = [int(x) for x in input().split(',')]
pc = Intcode(data)
pc.run(2)
