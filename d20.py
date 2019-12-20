import utils
import re
from collections import deque


def getColumn(matrix, i):
    return ''.join([row[i] for row in matrix])


def getLocations(data):
    doors = {}

    lines = data[:-1].split("\n")
    height = len(lines)
    width = len(lines[0])
    print(f"h = {height}, w = {width}")
    for i, line in enumerate(lines):
        for d in re.finditer(r"([A-Z][A-Z])", line):
            door = d.group()
            pos = d.start() - 1
            if pos < 0 or line[pos] != '.':
                pos += 3
            if door in doors:
                doors[door].append((pos, i))
            else:
                doors[door] = [(pos, i)]

    columns = [getColumn(lines, i) for i in range(width)]
    for i, column in enumerate(columns):
        for d in re.finditer(r"([A-Z][A-Z])", column):
            door = d.group()
            pos = d.start() - 1
            if pos < 0 or column[pos] != '.':
                pos += 3
            if door in doors:
                doors[door].append((i, pos))
            else:
                doors[door] = [(i, pos)]
    return doors


def getGraph(data, ports):
    graph = {}
    lines = data[:-1].split("\n")
    height = len(lines)
    width = len(lines[0])

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if lines[y][x] not in (' ', '#'):
                this = (x, y)
                east = (x + 1, y)
                west = (x - 1, y)
                north = (x, y - 1)
                south = (x, y + 1)

                neighbours = []

                if this in ports:
                    neighbours.append(ports[this])

                if lines[east[1]][east[0]] == '.':
                    neighbours.append(east)

                if lines[west[1]][west[0]] == '.':
                    neighbours.append(west)

                if lines[north[1]][north[0]] == '.':
                    neighbours.append(north)

                if lines[south[1]][south[0]] == '.':
                    neighbours.append(south)

                graph[(x, y)] = neighbours
    return graph


def findShortestPath(graph, start, end):
    dist = {start: [start]}
    q = deque()
    q.append(start)
    while len(q):
        at = q.popleft()
        for n in graph[at]:
            if n not in dist:
                dist[n] = dist[at] + [n]
                q.append(n)
    print(dist[end])
    return dist.get(end)


data = utils.get_input(2019, 20)
doors = getLocations(data)
print(doors)
start = doors["AA"][0]
goal = doors["ZZ"][0]
ports = {}
for v in doors.values():
    if len(v) == 2:
        ports[v[0]] = v[1]
        ports[v[1]] = v[0]

graph = getGraph(data, ports)
graph[graph[goal][0]] = [goal]

path = findShortestPath(graph, start, goal)
print(f"Part 1 Shortest path is {len(path) - 1}")
