class Node(object):
    """docstring for Node"""

    def __init__(self, name):
        super(Node, self).__init__()
        self.children = set()
        self.name = name
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.add(child)

    def findNode(self, name):
        if self.name == name:
            return self
        for c in self.children:
            found = c.findNode(name)
            if found:
                return found
        return None

    def printNode(self, depth):
        print(' ' * depth + str(self.name))
        depth += 1
        for c in self.children:
            c.printNode(depth)

    def getNumOrbits(self):
        if self.parent:
            return 1
        return 0

    def getNumIndirectOrbits(self):
        if self.parent and self.parent.parent:
            return 1 + self.parent.getNumIndirectOrbits()
        return 0

    def getTotalNumOrbits(self):
        t = self.getNumOrbits() + self.getNumIndirectOrbits()
        for c in self.children:
            t += c.getTotalNumOrbits()
        return t


def getCOM():
    nodes = {}
    while True:
        line = input()
        if line == "break":
            break
        elif line:
            o = line.split(")")
            center = o[0]
            orbit = o[1]

            if orbit not in nodes:
                nodes[orbit] = Node(orbit)

            if center not in nodes:
                nodes[center] = Node(center)

            nodes[center].addChild(nodes[orbit])
        else:
            break

    return nodes["COM"]


com = getCOM()
print(com.getTotalNumOrbits())
com.printNode(0)
