import math


class Element(object):
    """docstring for Element"""

    def __init__(self, name):
        super(Element, self).__init__()
        self.name = name
        self.children = {}
        self.quantity = 1
        self.parent = None

    def addChild(self, child, amount):
        child.parent = self
        self.children[child] = amount

    def produce(self, quantity, values, waste):
        n = self.name
        if n in values:
            values[n] += quantity
        else:
            values[n] = quantity

        left = waste[n] if n in waste else 0
        if left >= quantity:
            waste[n] -= quantity
            quantity = 0
        elif left > 0:
            del waste[n]
            quantity -= left

        produce_times = math.ceil(quantity / self.quantity)
        if produce_times > 0:
            produced = produce_times * self.quantity
            spare = produced - quantity
            if spare > 0:
                if n in waste:
                    waste[n] += spare
                else:
                    waste[n] = spare

            for c, a in self.children.items():
                c.produce(a * produce_times, values, waste)


def getElement(l):
    res = l.strip().split(" ")
    return (res[1], int(res[0]))


formulars = {}
while True:
    try:
        line = input().split("=>")
        res = getElement(line[1].strip())

        curr = None
        if res[0] in formulars:
            curr = formulars[res[0]]
        else:
            curr = Element(res[0])
            formulars[res[0]] = curr

        curr.quantity = res[1]

        ing = [getElement(a.strip()) for a in line[0].split(",")]
        for i in ing:
            if i[0] not in formulars:
                formulars[i[0]] = Element(i[0])

            curr.addChild(formulars[i[0]], i[1])

    except EOFError:
        break

root = formulars["FUEL"]
waste = {}
produced = {}
root.produce(1, produced, waste)
limit = 100_000_000_0000
v = produced["ORE"]
start = (limit // v)
end = start * 2
last_too_low = start
while start < end:
    produced = {}
    root.produce(start, produced, {})
    if produced['ORE'] > limit:
        end = start
    else:
        last_too_low = start
    step = (end - last_too_low) // 2
    if step == 0:
        break
    start = last_too_low + step
print(last_too_low)
