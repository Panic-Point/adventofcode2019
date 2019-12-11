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
from math import gcd, atan2, degrees


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


test_input1 = """.##.#
.....
#####
....#
...##"""

test_map1 = parse_map(test_input1)
station = (1, 0)
# assert count_visible(station, test_map1) == 7
# assert max_visible(test_map1) == [(3,4), 8]

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


def asteroids_by_degree(asteroids: List[tuple], station: tuple) -> Dict:
    asteroids.remove(station)
    slope_dict = {}
    for asteroid in asteroids:
        dx = station[0] - asteroid[0]
        dy = station[1] - asteroid[1]
        radian = atan2(dy, dx)
        # adjusting degree so 0.0 is vertical up and to reflect 0-360
        degree = degrees(radian) - 90
        if degree < 0:
            degree += 360
        if degree in slope_dict.keys():
            slope_dict[degree].append(asteroid)
        else:
            slope_dict[degree] = [asteroid]
    return slope_dict


def vaporized(asteroids_dict: Dict) -> List[tuple]:
    degree_list = list(asteroids_dict.keys())
    degree_list.sort()
    vaporized_list = []
    for angle in degree_list:
        if len(asteroids_dict[angle]) > 0:
            vaporized_list.append(asteroids_dict[angle].pop())
    return vaporized_list


asteroids_dict = asteroids_by_degree(test_map2, (11, 13))
vaporized_list = vaporized(asteroids_dict)
assert vaporized_list[0] == (11, 12)
assert vaporized_list[1] == (12, 1)
assert vaporized_list[49] == (16, 9)
assert vaporized_list[199] == (8, 2)

# (20, 21) is station from part 1
ACTUAL_DICT = asteroids_by_degree(ACTUAL_MAP, (20, 21))
print(vaporized(ACTUAL_DICT)[199])
