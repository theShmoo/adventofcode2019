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

    def find(self, name):
        if self.name == name:
            return self
        for c in self.children:
            found = c.find(name)
            if found:
                return found
        return None

    def printNode(self, depth):
        s = self.name + '\n'
        indent = '|  ' * depth
        if len(self.children) > 1:
            depth += 1

        for c in self.children:
            s += indent + c.printNode(depth)
        return s

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

    def getParents(self):
        parents = []
        if self.parent:
            parents.append(self.parent)
            parents.extend(self.parent.getParents())
        return parents


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
you = com.find("YOU")
santa = com.find("SAN")

you_parents = set(you.getParents())
san_parents = set(santa.getParents())
print(len(you_parents - san_parents) + len(san_parents - you_parents))

print(com.getTotalNumOrbits())
print(com.printNode(0))
