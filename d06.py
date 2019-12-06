class Node(object):
    """docstring for Node"""

    def __init__(self, name):
        super(Node, self).__init__()
        self.children = set()
        self.name = name
        self.num_indirect_orbits = 0
        self.num_direct_orbits = 0
        self.parent = None

    def addChild(self, child):
        child.parent = self
        child.getNumIndirectOrbits()
        child.getNumOrbits()
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
            self.num_direct_orbits = 1

    def getNumIndirectOrbits(self):
        if self.parent and self.parent.parent:
            self.num_indirect_orbits = 1 + self.parent.num_indirect_orbits

    def getTotalNumOrbits(self):
        t = self.num_direct_orbits + self.num_indirect_orbits
        print(self.name + " orbits " + str(t))
        for c in self.children:
            t += c.getTotalNumOrbits()
        return t


def getCOM():
    root = None
    free_nodes = {}
    while True:
        line = input()
        if line == "break":
            break
        elif line:
            o = line.split(")")
            free_nodes[o[0]] = Node(o[1])
        else:
            break

    root = Node("COM")
    while len(free_nodes) > 0:
        for a in tuple(free_nodes):
            parent = root.findNode(a)
            if parent:
                parent.addChild(free_nodes[a])
                del free_nodes[a]
        print(len(free_nodes))

    return root


com = getCOM()
print(com.getTotalNumOrbits())

com.printNode(0)
