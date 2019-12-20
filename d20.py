import utils
import re


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
            pos = (d.start() - 1, i)
            if pos[0] < 0 or line[pos[0]] != '.':
                pos = (d.start() + 3, i)
            if door in doors:
                doors[door].append(pos)
            else:
                doors[door] = [pos]

    columns = [getColumn(lines, i) for i in range(width)]
    for i, column in enumerate(columns):
        for d in re.finditer(r"([A-Z][A-Z])", column):
            door = d.group()
            pos = (i, d.start() - 1)
            if pos[1] < 0 or column[pos[1]] != '.':
                pos = (i, d.start() + 3)
            if door in doors:
                doors[door].append(pos)
            else:
                doors[door] = [pos]
    return doors


def getGraph(data, ports):
    graph = {}
    lines = data[:-1].split("\n")
    height = len(lines)
    width = len(lines[0])

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if lines[y][x] == '.':
                east = (x + 1, y)
                west = (x - 1, y)
                north = (x, y - 1)
                south = (x, y + 1)

                neighbours = []
                if lines[east[1]][east[0]] == '.':
                    neighbours.append(east)
                elif east in ports:
                    neighbours.append(ports[east])

                if lines[west[1]][west[0]] == '.':
                    neighbours.append(west)
                elif west in ports:
                    neighbours.append(ports[west])

                if lines[north[1]][north[0]] == '.':
                    neighbours.append(north)
                elif north in ports:
                    neighbours.append(ports[north])

                if lines[south[1]][south[0]] == '.':
                    neighbours.append(south)
                elif south in ports:
                    neighbours.append(ports[south])

                graph[(x, y)] = neighbours
    return graph


def findShortestPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path

    if start not in graph:
        return None

    shortest = None
    for neighbour in graph[start]:
        if neighbour not in path:
            newpath = findShortestPath(graph, neighbour, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath

    return shortest


data = utils.get_input(2019, 20)
doors = getLocations(data)
start = doors["AA"][0]
goal = doors["ZZ"][0]
ports = {}
for v in doors.values():
    if len(v) == 2:
        ports[v[0]] = v[1]
        ports[v[1]] = v[0]

graph = getGraph(data, ports)
print(graph[goal])
print(doors["PC"])
print(doors["ZZ"])

path = findShortestPath(graph, start, goal)
print(len(path))
