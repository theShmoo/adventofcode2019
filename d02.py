import copy


def handleOpcode(arr, pos):
    try:
        if arr[pos] == 99:
            return False
        elif arr[pos] == 1:
            arr[arr[pos + 3]] = arr[arr[pos + 1]] + arr[arr[pos + 2]]
        elif arr[pos] == 2:
            arr[arr[pos + 3]] = arr[arr[pos + 1]] * arr[arr[pos + 2]]
        else:
            return False
    except:
        return False
    return True


def solve():
    line = input()
    inp = line.split(",")
    initial = [int(o) for o in inp]
    t = 19690720
    for noun in range(0, 100):
        for verb in range(0, 100):
            opcodes = copy.copy(initial)
            opcodes[1] = noun
            opcodes[2] = verb
            for pos in range(0, len(opcodes), 4):
                if handleOpcode(opcodes, pos) is False:
                    break
            if opcodes[0] == t:
                print(100 * noun + verb)
                break
    print("Finished")


solve()
