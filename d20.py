import utils
import re
from collections import deque
from itertools import permutations


def getColumn(matrix, i):
    return ''.join([row[i] for row in matrix])


def isOutside(pos, width, height):
    outside = pos[0] == 2 or pos[0] == width - 4
    outside = outside or pos[1] == 2 or pos[1] == height - 3
    return outside


def getDoors(lines):
    doors = {}
    width = len(lines[0])

    for i, line in enumerate(lines):
        for d in re.finditer(r"([A-Z][A-Z])", line):
            door = d.group()
            pos = d.start() - 1
            if pos < 0 or line[pos] != '.':
                pos += 3

            coords = (pos, i)
            if door in doors:
                doors[door].append(coords)
            else:
                doors[door] = [coords]

    columns = [getColumn(lines, i) for i in range(width)]
    for i, column in enumerate(columns):
        for d in re.finditer(r"([A-Z][A-Z])", column):
            door = d.group()
            pos = d.start() - 1
            if pos < 0 or column[pos] != '.':
                pos += 3

            coords = (i, pos)
            if door in doors:
                doors[door].append(coords)
            else:
                doors[door] = [coords]
    return doors


def getNeighbours(data, pos, ports, outside_ports):
    (x, y, z) = pos
    xy = (x, y)
    neighbours = getNeighboursWithoutPorts(data, xy)
    if xy in ports:
        if xy in outside_ports:
            if z != 0:
                neighbours.append((*ports[xy], z - 1))
        else:
            neighbours.append((*ports[xy], z + 1))

    return neighbours


def getNeighboursWithoutPorts(data, pos):
    (x, y) = pos

    to_check = (
        (x + 1, y),
        (x - 1, y),
        (x, y - 1),
        (x, y + 1)
    )

    neighbours = []
    for c in to_check:
        if data[c[1]][c[0]] == '.':
            neighbours.append(c)

    return neighbours


def findShortestPath(graph, ports, start, end):
    dist = {start: [start]}
    q = deque()
    q.append(start)
    while len(q):
        at = q.popleft()
        (x, y, z) = at
        for n in graph[(x, y)]:
            out = isOutside(n, 46, 37)

            if z == 0:
                if out:
                    continue
                elif n is end:
                    pos = (*end, 0)
                    dist[pos] = dist[at] + [pos]
                    q.append(pos)
                    continue
            elif n not in ports:
                continue

            p = ports[n]
            pos = (*p, z + (-1 if out else 1))
            if pos not in dist:
                dist[pos] = dist[at] + [pos]
                q.append(pos)
    print(dist)
    return dist.get(end)


def findShortestPathWithoutPorts(data, start, end):
    dist = {start: [start]}
    q = deque()
    q.append(start)
    while len(q):
        at = q.popleft()
        for n in getNeighboursWithoutPorts(data, at):
            if n not in dist:
                dist[n] = dist[at] + [n]
                q.append(n)
    return dist.get(end)


data = utils.get_input(2019, 20)[:-1].split("\n")
height = len(data)
width = len(data[0])
print(width)
print(height)
doors = getDoors(data)
start = doors["AA"][0]
goal = doors["ZZ"][0]
print(start)
print(goal)
ports = {}
for k, v in doors.items():
    if len(v) == 2:
        ports[v[0]] = v[1]
        ports[v[1]] = v[0]

distances = {i: {} for i in ports}
graph = {i: [] for i in ports}

for i, o in permutations(ports.values(), 2):
    path = findShortestPathWithoutPorts(data, o, i)
    if path:
        distances[o][i] = len(path)
        graph[o].append(i)

distances[start] = {}
distances[goal] = {}
graph[start] = []

for i in ports.values():
    path = findShortestPathWithoutPorts(data, start, i)
    if path:
        distances[start][i] = len(path)
        graph[start].append(i)

    path = findShortestPathWithoutPorts(data, i, goal)
    if path:
        distances[i][goal] = len(path)
        graph[i].append(goal)

print(graph)

start_3d = (*start, 0)
goal_3d = (*goal, 0)
path = findShortestPath(graph, ports, start_3d, goal_3d)
print(path)
