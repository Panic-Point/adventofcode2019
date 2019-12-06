"""
Part 1
https://adventofcode.com/2019/day/6
Whenever A orbits B and B orbits C, then A indirectly orbits C. This chain can be any number of objects long: 
if A orbits B, B orbits C, and C orbits D, then A indirectly orbits D.

What is the total number of direct and indirect orbits in your map data?
"""

from typing import List, Dict


def parse_input(orbits: List[str]) -> Dict:
    output = {}
    for orbit in orbits:
        s = orbit.split(')')
        output.update({s[1]: s[0]})
    return output


assert parse_input(['AAA)BBB']) == {'BBB': 'AAA'}

# create list of orbital chains back to COM
def get_orbit_chains(orbits: Dict) -> List[List[str]]:
    chains = [[]]
    for planet in orbits.keys():
        chain = [planet]
        while planet != 'COM':
            planet = orbits.get(planet)
            chain.append(planet)

        chains.append(chain)
    return chains

# count chain back to COM for each non-COM. Shouldn't be too bad given each object has exactly 1 direct orbit
def checksum(chains: List[List[str]]) -> int:
    count = 0
    for chain in chains:
        # Don't count the initial body the chain is originating from
        length = len(chain) - 1
        # deal with the empty set. 
        if length >= 0:
            count += length
    return count


test_input = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""

orbits = []
for line in test_input.split('\n'):
    orbits.append(line)

orbits_dict = parse_input(orbits)
chains = get_orbit_chains(orbits_dict)
assert checksum(chains) == 42

with open("Day06_input.txt") as f:
    ACTUAL_ORBITS = [line.strip() for line in f]

ACTUAL_ORBITS_DICT = parse_input(ACTUAL_ORBITS)
ACTUAL_CHAINS = get_orbit_chains(ACTUAL_ORBITS_DICT)
print(checksum(ACTUAL_CHAINS))

"""
Part 2
You start at the object YOU are orbiting; your destination is the object SAN is orbiting. 
An orbital transfer lets you move from any object to an object orbiting or orbited by that object.

What is the minimum number of transfers to get to Santa
"""
"""
if we compare the chains beginning with 'YOU' and 'SAN' removing the commonalities. The length of the 
resulting set, minus 'YOU' and 'SAN' will be the number of transfers that need to be made. 
"""
def get_to_santa(chains: List[List[str]]) -> int:
    my_chain = [chain for chain in chains if 'YOU' in chain]
    my_set = set(my_chain[0])
    santa_chain = [chain for chain in chains if 'SAN' in chain]
    santa_set = set(santa_chain[0])
    exlusive_set = my_set ^ santa_set
    return len(exlusive_set) - 2


test_input2 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""

orbits2 = []
for line in test_input2.split('\n'):
    orbits2.append(line)

orbits_dict2 = parse_input(orbits2)
chains2 = get_orbit_chains(orbits_dict2)
assert get_to_santa(chains2) == 4

print(get_to_santa(ACTUAL_CHAINS))
