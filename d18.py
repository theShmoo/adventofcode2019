import utils
import re
from collections import deque
from itertools import permutations
from itertools import combinations


def getLocations(data):
    keys = {}
    doors = {}

    for k in re.finditer("[a-z]", data):
        keys[k.group()] = k.start()

    for d in re.finditer("[A-Z]", data):
        doors[d.group()] = d.start()

    entrance = data.find("@")

    return (
            [v for _, v in sorted(keys.items())],
            [v for _, v in sorted(doors.items())],
            entrance)


def getPos(x, y):
    # 82 is width of the data
    return y * 82 + x


def getGraph(data):
    graph = {}
    width = data.find("\n")
    for y in range(1, width):
        for x in range(1, width):
            this = getPos(x, y)
            if data[this] != '#':
                east = getPos(x + 1, y)
                west = getPos(x - 1, y)
                north = getPos(x, y - 1)
                south = getPos(x, y + 1)

                neighbours = []
                if data[east] != '#':
                    neighbours.append(east)
                if data[west] != '#':
                    neighbours.append(west)
                if data[north] != '#':
                    neighbours.append(north)
                if data[south] != '#':
                    neighbours.append(south)

                graph[this] = neighbours
    return graph


def find_shortest_path(graph, doors, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path

    if start in graph:
        return None

    shortest = None
    for neighbour in graph[start]:
        if neighbour not in path:
            newpath = find_shortest_path(graph, doors, neighbour, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath

    return shortest


data = utils.get_input(2019, 18)
print(data)
(keys, doors, entrance) = getLocations(data)
graph = getGraph(data)

start = entrance
# keys are interesting nodes
# so we have to find the route from every key to every reachable key

result = []
for p in keys:
    sum = 0
    start = entrance
    for end in p:
        path = find_shortest_path(graph, doors, start, end)
        if path is not None:
            sum += len(path)
        start = end
    result.append(sum)
print(result)
print(min(result))
