"""
https://adventofcode.com/2019/day/10

part 1:
1. create List[List[str]] from input
2. y will be the position in outer list, and x will be position in inner list
    for example [[1,2,3],[4,5,6]] 6 would be at position (x = 2, y = 1)
3. create set of list of tuples for all asteroids that have each position that fall on the same line
4. for each list in set, if a tuple in the list has an asteroid count += 1
"""
from typing import List, Dict
from math import gcd


# reads map string and outputs list of list with each position indicated
def parse_map(map: str) -> List[tuple]:
    latitudes = map.split('\n')
    asteroids = []
    for y in range(len(latitudes)):
        for x in range(len(latitudes[0])):
            if latitudes[y][x] == '#':
                asteroids.append((x, y))
    return asteroids


def count_visible(station: tuple, asteroids: List[tuple]) -> int:
    # dictionary with slope as key
    sightlines = {}
    for asteroid in asteroids:
        if station != asteroid:
            dx = station[0] - asteroid[0]
            dy = station[1] - asteroid[1]
            div = gcd(dx, dy)
            slope = (dx // div, dy // div)
            if slope not in sightlines.keys():
                sightlines[slope] = asteroid
    return len(sightlines.keys())


def max_visible(asteroids: List[tuple]) -> Dict:
    best_dict = {}
    for station in asteroids:
        visible = count_visible(station, asteroids)
        best_dict[station] = visible
    max_station = max(best_dict, key=(lambda key: best_dict[key]))
    return [max_station, best_dict[max_station]]


test_input1 = """.#..#
.....
#####
....#
...##"""

test_map1 = parse_map(test_input1)
station = (1, 0)
assert count_visible(station, test_map1) == 7
assert max_visible(test_map1) == [(3,4), 8]

test_input2 = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""

test_map2 = parse_map(test_input2)
assert max_visible(test_map2) == [(11, 13), 210]

ACTUAL_INPUT = """#..#.#.###.#...##.##....
.#.#####.#.#.##.....##.#
##..#.###..###..#####..#
####.#.#..#....#..##.##.
.#######.#####...#.###..
.##...#.#.###..###.#.#.#
.######.....#.###..#....
.##..##.#..#####...###.#
#######.#..#####..#.#.#.
.###.###...##.##....##.#
##.###.##.#.#..####.....
#.#..##..#..#.#..#####.#
#####.##.#.#.#.#.#.#..##
#...##.##.###.##.#.###..
####.##.#.#.####.#####.#
.#..##...##..##..#.#.##.
###...####.###.#.###.#.#
..####.#####..#####.#.##
..###..###..#..##...#.#.
##.####...##....####.##.
####..#..##.#.#....#..#.
.#..........#..#.#.####.
###..###.###.#.#.#....##
########.#######.#.##.##"""


ACTUAL_MAP = parse_map(ACTUAL_INPUT)
print(max_visible(ACTUAL_MAP))


