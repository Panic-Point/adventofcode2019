"""
Part 1
The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find
the intersection point closest to the central port. Because the wires are on a grid, use the Manhattan distance for
this measurement. While the wires do technically cross right at the central port where they both start, this point
does not count, nor does a wire count as crossing with itself.

"""

coordinate = tuple()
path = set()


def manhattan_distance(coor1: coordinate, coor2: coordinate) -> int:
    return abs(coor1[0] - coor2[0]) + abs(coor1[1] - coor2[1])


def get_path(wire):
    x = 0
    y = 0
    coordinates = set()
    for i in wire:
        direction = i[0]
        length = int(i[1:])
        if direction == 'R':
            for j in range(length):
                x += 1
                coordinates.add((x, y))
        elif direction == 'L':
            for j in range(length):
                x -= 1
                coordinates.add((x, y))
        elif direction == 'U':
            for j in range(length):
                y += 1
                coordinates.add((x, y))
        elif direction == 'D':
            for j in range(length):
                y -= 1
                coordinates.add((x, y))
        else:
            raise RuntimeError(f"invalid direction path1: {direction}")
    return coordinates


def find_intersections(path1: path, path2: path) -> set:
    intersections = path1.intersection(path2)
    return intersections


def min_distance(coordinates: set) -> int:
    distance = set()
    for c in coordinates:
        distance.add(manhattan_distance((0, 0), c))
    return min(distance)


test1 = ['R8', 'U5', 'L5', 'D3']
test2 = ['U7', 'R6', 'D4', 'L4']
test_path1 = get_path(['R8', 'U5', 'L5', 'D3'])
test_path2 = get_path(['U7', 'R6', 'D4', 'L4'])
assert (min_distance(find_intersections(test_path1, test_path2)) == 6)

test3 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
test4 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
test_path3 = get_path(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'])
test_path4 = get_path(['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'])
assert (min_distance(find_intersections(test_path3, test_path4)) == 159)


input_file = open("Day03input.txt", "r")
lines = input_file.readlines()

ACTUALPATH1 = get_path(lines[0].split(','))
ACTUALPATH2 = get_path(lines[1].split(','))
part1 = min_distance(find_intersections(ACTUALPATH1, ACTUALPATH2))
print(part1)


"""
Part 2
It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where 
the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value 
from the first time it visits that position when calculating the total value of a specific intersection. 

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, 
including the intersection being considered. 
"""


def count_steps(path, coordinate) -> int:
    x1 = y1 = 0
    steps = 0
    for s in path:
        direction = s[0]
        length = int(s[1:])
        if direction == 'R':
            for i in range(length):
                x1 += 1
                steps += 1
                if (x1, y1) == coordinate:
                    return steps
        elif direction == 'L':
            for i in range(length):
                x1 -= 1
                steps += 1
                if (x1, y1) == coordinate:
                    return steps
        elif direction == 'U':
            for i in range(length):
                y1 += 1
                steps += 1
                if (x1, y1) == coordinate:
                    return steps
        elif direction == 'D':
            for i in range(length):
                y1 -= 1
                steps += 1
                if (x1, y1) == coordinate:
                    return steps
        else:
            raise RuntimeError(f"invalid direction path1: {direction}")

    return steps


intersections1 = find_intersections(test_path1, test_path2)
steps1 = []
intersections2 = find_intersections(test_path3, test_path4)
steps2 = []

for cross in intersections1:
    s1 = count_steps(test1, cross)
    s2 = count_steps(test2, cross)
    steps1.append(s1 + s2)

for cross in intersections2:
    s1 = count_steps(test3, cross)
    s2 = count_steps(test4, cross)
    steps2.append(s1 + s2)

assert (min(steps1) == 30)
assert (min(steps2) == 610)

ACTUALINTERSECTIONS = find_intersections(ACTUALPATH1, ACTUALPATH2)
ACTUALSTEPS = []

for cross in ACTUALINTERSECTIONS:
    s1 = count_steps(lines[0].split(','), cross)
    s2 = count_steps(lines[1].split(','), cross)
    ACTUALSTEPS.append(s1 + s2)


part2 = min(ACTUALSTEPS)
print(part2)

