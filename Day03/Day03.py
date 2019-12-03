"""
Part 1
The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find
the intersection point closest to the central port. Because the wires are on a grid, use the Manhattan distance for
this measurement. While the wires do technically cross right at the central port where they both start, this point
does not count, nor does a wire count as crossing with itself.

"""

coordinate = tuple()
path = list()


def manhattan_distance(coor1: coordinate, coor2: coordinate) -> int:
    return abs(coor1[0] - coor2[0]) + abs(coor1[1] - coor2[1])


def find_intersections(path1: path, path2: path) -> list:
    set_for_path1 = set()
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    intersections = []
    for s in path1:
        direction = s[0]
        length = int(s[1:])
        if direction == 'R':
            for i in range(length):
                x1 += 1
                set_for_path1.add((x1, y1))
        elif direction == 'L':
            for i in range(length):
                x1 -= 1
                set_for_path1.add((x1, y1))
        elif direction == 'U':
            for i in range(length):
                y1 += 1
                set_for_path1.add((x1, y1))
        elif direction == 'D':
            for i in range(length):
                y1 -= 1
                set_for_path1.add((x1, y1))
        else:
            raise RuntimeError(f"invalid direction path1: {direction}")
    for t in path2:
        direction = t[0]
        length = int(t[1:])
        if direction == 'R':
            for i in range(length):
                x2 += 1
                if (x2, y2) in set_for_path1:
                    intersections.append((x2, y2))
        elif direction == 'L':
            for i in range(length):
                x2 -= 1
                if (x2, y2) in set_for_path1:
                    intersections.append((x2, y2))
        elif direction == 'U':
            for i in range(length):
                y2 += 1
                if (x2, y2) in set_for_path1:
                    intersections.append((x2, y2))
        elif direction == 'D':
            for i in range(length):
                y2 -= 1
                if (x2, y2) in set_for_path1:
                    intersections.append((x2, y2))
        else:
            raise RuntimeError(f"invalid direction path2: {direction}")

    return intersections


def min_distance(coordinates: list) -> int:
    distance = manhattan_distance((0, 0), coordinates[0])
    for i in range(1, len(coordinates)):
        if manhattan_distance((0, 0), coordinates[i]) < distance:
            distance = manhattan_distance((0, 0), coordinates[i])
    return distance


test_path1 = ['R8', 'U5', 'L5', 'D3']
test_path2 = ['U7', 'R6', 'D4', 'L4']
assert (min_distance(find_intersections(test_path1, test_path2)) == 6)

test_path3 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
test_path4 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
assert (min_distance(find_intersections(test_path3, test_path4)) == 159)

input_file = open("Day03input.txt", "r")
lines = input_file.readlines()

part1 = min_distance(find_intersections(lines[0].split(','), lines[1].split(',')))
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

# lines[0].split(','), lines[1].split(',')


intersections1 = find_intersections(test_path1, test_path2)
steps1 = []
intersections2 = find_intersections(test_path3, test_path4)
steps2 = []

for cross in intersections1:
    s1 = count_steps(test_path1, cross)
    s2 = count_steps(test_path2, cross)
    steps1.append(s1 + s2)

for cross in intersections2:
    s1 = count_steps(test_path3, cross)
    s2 = count_steps(test_path4, cross)
    steps2.append(s1 + s2)

assert (min(steps1) == 30)
assert (min(steps2) == 610)

ACTUALINTERSECTIONS = find_intersections(lines[0].split(','), lines[1].split(','))
ACTUALSTEPS = []

for cross in ACTUALINTERSECTIONS:
    s1 = count_steps(lines[0].split(','), cross)
    s2 = count_steps(lines[1].split(','), cross)
    ACTUALSTEPS.append(s1 + s2)


part2 = min(ACTUALSTEPS)
print(part2)
