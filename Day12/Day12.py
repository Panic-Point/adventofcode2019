"""
https://adventofcode.com/2019/day/12
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class Moon:
    name: str
    x_pos: int
    y_pos: int
    z_pos: int
    pot: int = 0
    kin: int = 0
    total_energy: int = 0
    velocity: list = field(default_factory=list)

    def __post_init__(self):
        self.velocity.append(0)
        self.velocity.append(0)
        self.velocity.append(0)
        self.set_pot()
        self.set_kin()

    def set_positions(self):
        self.x_pos += self.velocity[0]
        self.y_pos += self.velocity[1]
        self.z_pos += self.velocity[2]

    def set_pot(self):
        self.pot = abs(self.x_pos) + abs(self.y_pos) + abs(self.z_pos)

    def set_kin(self):
        self.kin = abs(self.velocity[0]) + abs(self.velocity[1]) + abs(self.velocity[2])

    def set_total_energy(self):
        self.total_energy = self.pot * self.kin


"""
<x=-17, y=9, z=-5>
<x=-1, y=7, z=13>
<x=-19, y=12, z=5>
<x=-6, y=-6, z=-4>
"""

testmoons1 = [Moon('IO', -1, 0, 2),
              Moon('Europa', 2, -10, -7),
              Moon('Ganymede', 4, -8, 8),
              Moon('Callisto', 3, 5, -1)]

testmoons2 = [Moon('IO', -8, -10, 0),
              Moon('Europa', 5, 5, 10),
              Moon('Ganymede', 2, -7, 3),
              Moon('Callisto', 9, -8, -3)]

ACTUALMOONS = [Moon('IO', -17, 9, -5),
               Moon('Europa', -1, 7, 13),
               Moon('Ganymede', -19, 12, 5),
               Moon('Callisto', -6, -6, -4)]


def set_velocity(moons: List[Moon]):
    for moon in moons:
        for moon2 in moons:
            if moon.x_pos < moon2.x_pos:
                moon.velocity[0] += 1
            elif moon.x_pos > moon2.x_pos:
                moon.velocity[0] += -1
            if moon.y_pos < moon2.y_pos:
                moon.velocity[1] += 1
            elif moon.y_pos > moon2.y_pos:
                moon.velocity[1] += -1
            if moon.z_pos < moon2.z_pos:
                moon.velocity[2] += 1
            elif moon.z_pos > moon2.z_pos:
                moon.velocity[2] += -1


def step(moons: List[Moon]):
    set_velocity(moons)
    for moon in moons:
        moon.set_positions()
        moon.set_pot()
        moon.set_kin()
        moon.set_total_energy()


def run(moons, steps):
    system_energy = 0
    for _ in range(steps):
        step(moons)
    for moon in moons:
        system_energy += moon.total_energy
    return system_energy


assert (run(testmoons1, 10) == 179)
assert (run(testmoons2, 100) == 1940)

print(run(ACTUALMOONS, 1000))
