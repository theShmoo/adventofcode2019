import copy
import itertools

def getModeForParam(pos, data, ins):
    if pos == 1:
        return (data[ins] % 1000) // 100 is 1
    if pos == 2:
        return data[ins] // 1000 is 1


def getParamByMode(pos, data, ins):
    if getModeForParam(pos, data, ins):
        return data[ins + pos]
    else:
        return data[data[ins + pos]]


def setValueAtPos(data, pos, val):
    data[data[pos]] = val


class Amplifier(object):
    """Amplifier"""

    def __init__(self, code, phase):
        super(Amplifier, self).__init__()
        self.code = copy.copy(code)
        self.ins = 0
        self.halt = False
        self.config = False
        self.runIntcode(phase)

    def runIntcode(self, inp):
        if self.halt:
            print("ERROR")
        data = self.code
        ins = self.ins
        while data[ins] % 100 != 99:
            opcode = data[ins] % 100
            if opcode == 1:
                # add
                p1 = getParamByMode(1, data, ins)
                p2 = getParamByMode(2, data, ins)
                setValueAtPos(data, ins + 3, p1 + p2)
                ins += 4
            elif opcode == 2:
                # mul
                p1 = getParamByMode(1, data, ins)
                p2 = getParamByMode(2, data, ins)
                setValueAtPos(data, ins + 3, p1 * p2)
                ins += 4
            elif opcode == 3:
                # input
                setValueAtPos(data, ins + 1, inp)
                ins += 2
                if not self.config:
                    self.config = True
                    self.ins = ins
                    return -1
            elif opcode == 4:
                # output
                p1 = getParamByMode(1, data, ins)
                ins += 2
                self.ins = ins
                return p1
            elif opcode == 5:
                # jump-if-true
                p1 = getParamByMode(1, data, ins)
                p2 = getParamByMode(2, data, ins)
                if p1:
                    ins = p2
                else:
                    ins += 3
            elif opcode == 6:
                # jump-if-false
                p1 = getParamByMode(1, data, ins)
                p2 = getParamByMode(2, data, ins)
                if not p1:
                    ins = p2
                else:
                    ins += 3
            elif opcode == 7:
                # less than
                p1 = getParamByMode(1, data, ins)
                p2 = getParamByMode(2, data, ins)
                setValueAtPos(data, ins + 3, 1 if p1 < p2 else 0)
                ins += 4
            elif opcode == 8:
                # equals
                p1 = getParamByMode(1, data, ins)
                p2 = getParamByMode(2, data, ins)
                setValueAtPos(data, ins + 3, 1 if p1 == p2 else 0)
                ins += 4

        self.halt = True
        return inp


inp = input()
data = [int(x) for x in inp.split(',')]
all_settings = list(itertools.permutations(range(5, 10)))
thruster_signal = []

for phase_settings in all_settings:
    amps = [Amplifier(data, phase) for phase in phase_settings]
    val = 0
    while not amps[4].halt:
        for a in amps:
            val = a.runIntcode(val)

    thruster_signal.append(val)

print(max(thruster_signal))
