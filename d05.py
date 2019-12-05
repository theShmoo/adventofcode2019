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


inp = input()
data = [int(x) for x in inp.split(',')]
inVal = 5
ins = 0
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
        setValueAtPos(data, ins + 1, inVal)
        ins += 2
    elif opcode == 4:
        # output
        p1 = getParamByMode(1, data, ins)
        print(p1)
        ins += 2
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
