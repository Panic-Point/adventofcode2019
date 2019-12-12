from enum import Enum
from typing import List, Tuple, Dict


class Opcode(Enum):
    ADD = 1
    MULTIPLY = 2
    STORE_INPUT = 3
    SEND_TO_OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    OFFSET = 9
    END_PROGRAM = 99


Modes = List[int]


def parse_opcode(opcode: int, num_modes: int = 3) -> Tuple[Opcode, Modes]:
    opcode_part = opcode % 100

    modes: List[int] = []
    opcode = opcode // 100

    for _ in range(num_modes):
        modes.append(opcode % 10)
        opcode = opcode // 10

    return Opcode(opcode_part), modes


class EndProgram(Exception):
    pass


class Computer:
    def __init__(self, program: List[int]):
        program.extend([0] * 10000)
        self.program = program[:]
        self.inputs = []
        self.pos = 0
        self.rel_base = 0
        self.step = 0

    def get_value(self, pos, mode: int) -> int:
        if mode == 0:
            # pointer mode
            return self.program[self.program[pos]]
        elif mode == 1:
            # immediate mode
            return self.program[pos]
        elif mode == 2:
            # relative mode
            return self.program[self.rel_base + self.program[pos]]
        else:
            raise ValueError(f"unknown mode: {mode}")

    def get_out_pos(self, pos: int, mode: int):
        if mode == 0:
            # pointer mode
            return self.program[pos]
        if mode == 2:
            # relative mode
            return self.program[pos] + self.rel_base

    def run(self, input: List[int]) -> List[int]:
        program = self.program

        while True:
            opcode, modes = parse_opcode(program[self.pos])

            if opcode == Opcode.END_PROGRAM:
                raise EndProgram
            elif opcode == Opcode.ADD:
                value1 = self.get_value(self.pos + 1, modes[0])
                value2 = self.get_value(self.pos + 2, modes[1])
                out_pos = self.get_out_pos(self.pos + 3, modes[2])
                program[out_pos] = value1 + value2
                # print(
                #    f"current location {self.pos}, value at position {program[self.pos]}, current instruction {opcode}, value1 {value1}, value2 {value2}, output {value1 + value2} to {out_pos}")
                self.pos += 4
            elif opcode == Opcode.MULTIPLY:
                value1 = self.get_value(self.pos + 1, modes[0])
                value2 = self.get_value(self.pos + 2, modes[1])
                out_pos = self.get_out_pos(self.pos + 3, modes[2])
                program[out_pos] = value1 * value2
                # print(
                #    f"current location {self.pos}, value at position {program[self.pos]}, current instruction {opcode}, value1 {value1}, value2 {value2}, output {value1 * value2} to {out_pos}")
                self.pos += 4
            elif opcode == Opcode.STORE_INPUT:
                # Get input and store at location
                out_pos = self.get_out_pos(self.pos + 1, modes[0])
                input_value = input[0]
                input = input[1:]
                # print(
                #    f"current location {self.pos}, value at position {program[self.pos]}, current instruction {opcode}, input_value {input_value} stored to {out_pos}")
                self.program[out_pos] = input_value
                self.pos += 2
            elif opcode == Opcode.SEND_TO_OUTPUT:
                # Get output from location
                value = self.get_value(self.pos + 1, modes[0])
                # print(
                #   f"current location {self.pos}, value at position {program[self.pos]}, current instruction {opcode}, value1 {value}, output {output}")
                self.pos += 2
                return value

            elif opcode == Opcode.JUMP_IF_TRUE:
                # jump if true
                value1 = self.get_value(self.pos + 1, modes[0])
                value2 = self.get_value(self.pos + 2, modes[1])

                if value1 != 0:
                    # print(
                    #    f"current location {self.pos}, value at position {program[self.pos]}, current instruction {opcode}, value1 {value1}, value2 {value2}, jump to {value2}")
                    self.pos = value2
                else:
                    # print(
                    #    f"current location {self.pos}, value at position {program[self.pos]}, current instruction {opcode}, value1 {value1}, value2 {value2}, don't jump")
                    self.pos += 3

            elif opcode == Opcode.JUMP_IF_FALSE:
                value1 = self.get_value(self.pos + 1, modes[0])
                value2 = self.get_value(self.pos + 2, modes[1])

                if value1 == 0:
                    # print(
                    #    f"current location {self.pos}, value at position {program[self.pos]}, current instruction {opcode}, value1 {value1}, value2 {value2}, jump to {value2}")
                    self.pos = value2
                else:
                    # print(
                    #    f"current location {self.pos}, value at position {program[self.pos]}, current instruction {opcode}, value1 {value1}, value2 {value2}, don't jump")
                    self.pos += 3

            elif opcode == Opcode.LESS_THAN:
                value1 = self.get_value(self.pos + 1, modes[0])
                value2 = self.get_value(self.pos + 2, modes[1])
                out_pos = self.get_out_pos(self.pos + 3, modes[2])

                if value1 < value2:
                    program[out_pos] = 1
                    # print(
                    #    f"current location {self.pos}, value at position {program[self.pos]}, current instruction {opcode}, value1 {value1}, value2 {value2}, output 1 to {out_pos}")
                else:
                    program[out_pos] = 0
                    # print(
                    #   f"current location {self.pos}, value at position {program[self.pos]}, current instruction {opcode}, value1 {value1}, value2 {value2}, output 0 to {out_pos}")
                self.pos += 4

            elif opcode == Opcode.EQUALS:
                value1 = self.get_value(self.pos + 1, modes[0])
                value2 = self.get_value(self.pos + 2, modes[1])
                out_pos = self.get_out_pos(self.pos + 3, modes[2])

                if value1 == value2:
                    program[out_pos] = 1
                    # print(
                    #    f"current location {self.pos}, value at position {program[self.pos]}, current instruction {opcode}, value1 {value1}, value2 {value2}, output 1 to {out_pos}")
                else:
                    program[out_pos] = 0
                    # print(
                    #    f"current location {self.pos}, value at position {program[self.pos]}, current instruction {opcode}, value1 {value1}, value2 {value2}, output 0 to {out_pos}")
                self.pos += 4

            elif opcode == Opcode.OFFSET:
                value1 = self.get_value(self.pos + 1, modes[0])
                # print(
                #    f"current location {self.pos}, value at position {program[self.pos]}, current instruction {opcode}, current base {self.rel_base}, offset by {value1}, new base {self.rel_base + value1}")
                self.rel_base += value1
                self.pos += 2

            else:
                raise RuntimeError(f"invalid opcode: {opcode}")
            self.step += 1


ACTUAL_INPUT = [3, 8, 1005, 8, 314, 1106, 0, 11, 0, 0, 0, 104, 1, 104, 0, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10,
                108, 1, 8, 10, 4, 10, 1002, 8, 1, 28, 2, 2, 16, 10, 1, 1108, 7, 10, 1006, 0, 10, 1, 5, 14, 10, 3, 8,
                102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 108, 1, 8, 10, 4, 10, 102, 1, 8, 65, 1006, 0, 59, 2, 109, 1, 10,
                1006, 0, 51, 2, 1003, 12, 10, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 108, 1, 8, 10, 4, 10, 1001,
                8, 0, 101, 1006, 0, 34, 1, 1106, 0, 10, 1, 1101, 17, 10, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10,
                1008, 8, 0, 10, 4, 10, 1001, 8, 0, 135, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 108, 0, 8, 10, 4,
                10, 1001, 8, 0, 156, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 108, 0, 8, 10, 4, 10, 1001, 8, 0,
                178, 1, 108, 19, 10, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 108, 0, 8, 10, 4, 10, 1002, 8, 1, 204,
                1, 1006, 17, 10, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 108, 1, 8, 10, 4, 10, 102, 1, 8, 230,
                1006, 0, 67, 1, 103, 11, 10, 1, 1009, 19, 10, 1, 109, 10, 10, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4,
                10, 1008, 8, 0, 10, 4, 10, 101, 0, 8, 268, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 1008, 8, 1, 10,
                4, 10, 1002, 8, 1, 290, 2, 108, 13, 10, 101, 1, 9, 9, 1007, 9, 989, 10, 1005, 10, 15, 99, 109, 636, 104,
                0, 104, 1, 21101, 48210224024, 0, 1, 21101, 0, 331, 0, 1105, 1, 435, 21101, 0, 937264165644, 1, 21101,
                0, 342, 0, 1105, 1, 435, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 1, 3, 10,
                104, 0, 104, 1, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 1, 21101, 235354025051, 0, 1, 21101, 389, 0,
                0, 1105, 1, 435, 21102, 29166169280, 1, 1, 21102, 400, 1, 0, 1105, 1, 435, 3, 10, 104, 0, 104, 0, 3, 10,
                104, 0, 104, 0, 21102, 709475849060, 1, 1, 21102, 1, 423, 0, 1106, 0, 435, 21102, 868498428684, 1, 1,
                21101, 434, 0, 0, 1105, 1, 435, 99, 109, 2, 21201, -1, 0, 1, 21101, 0, 40, 2, 21102, 1, 466, 3, 21101,
                456, 0, 0, 1105, 1, 499, 109, -2, 2105, 1, 0, 0, 1, 0, 0, 1, 109, 2, 3, 10, 204, -1, 1001, 461, 462,
                477, 4, 0, 1001, 461, 1, 461, 108, 4, 461, 10, 1006, 10, 493, 1101, 0, 0, 461, 109, -2, 2106, 0, 0, 0,
                109, 4, 2102, 1, -1, 498, 1207, -3, 0, 10, 1006, 10, 516, 21102, 1, 0, -3, 21201, -3, 0, 1, 21201, -2,
                0, 2, 21102, 1, 1, 3, 21102, 535, 1, 0, 1106, 0, 540, 109, -4, 2106, 0, 0, 109, 5, 1207, -3, 1, 10,
                1006, 10, 563, 2207, -4, -2, 10, 1006, 10, 563, 21202, -4, 1, -4, 1106, 0, 631, 21201, -4, 0, 1, 21201,
                -3, -1, 2, 21202, -2, 2, 3, 21101, 582, 0, 0, 1105, 1, 540, 22102, 1, 1, -4, 21102, 1, 1, -1, 2207, -4,
                -2, 10, 1006, 10, 601, 21101, 0, 0, -1, 22202, -2, -1, -2, 2107, 0, -3, 10, 1006, 10, 623, 22102, 1, -1,
                1, 21101, 623, 0, 0, 105, 1, 498, 21202, -2, -1, -2, 22201, -4, -2, -4, 109, -5, 2105, 1, 0]

ROBOT = Computer(ACTUAL_INPUT)


# print(ROBOT.run([0]))


def turn(direction, instruction):
    if direction == 'UP':
        if instruction == 0:
            return 'LEFT'
        else:
            return 'RIGHT'
    elif direction == 'LEFT':
        if instruction == 0:
            return 'DOWN'
        else:
            return 'UP'
    elif direction == 'DOWN':
        if instruction == 0:
            return 'RIGHT'
        else:
            return 'LEFT'
    elif direction == 'RIGHT':
        if instruction == 0:
            return 'UP'
        else:
            return 'DOWN'


def move(direction, position):
    if direction == 'UP':
        position[1] += 1
    elif direction == 'LEFT':
        position[0] -= 1
    elif direction == 'DOWN':
        position[1] -= 1
    elif direction == 'RIGHT':
        position[0] += 1
    return position


def paint(robot: Computer) -> Dict:
    panels_painted = {(0, 0): 1}
    position = [0, 0]
    direction = 'UP'
    outputs = []
    try:
        while True:
            # get input color
            if tuple(position) in panels_painted.keys():
                input_color = panels_painted[tuple(position)]
            else:
                input_color = 0

            outputs.append(robot.run([input_color]))
            outputs.append(robot.run([]))

            if len(outputs) == 2:
                panels_painted[tuple(position)] = outputs[0]
                direction = turn(direction, outputs[1])
                position = move(direction, position)
                outputs.clear()
    except EndProgram:
        return panels_painted


panels = paint(ROBOT)


# print(panels)
# print(len(panels.keys()))


def decode_message(panels):
    max_rows = max([abs(pos[1]) for pos in panels.keys()])
    max_cols = max([abs(pos[0]) for pos in panels.keys()])
    print(max_rows)
    print(max_cols)
    grid = [[' ' for _ in range(max_cols + 1)] for _ in range(max_rows + 1)]
    for p in panels:
        x = abs(p[0])
        y = abs(p[1])
        if panels[p] == 1:
            grid[y][x] = 'X'
    for m in grid:
        line = ''
        for n in m:
            if n == 'X':
                line += 'X'
            else:
                line += ' '
        print(line)


decode_message(panels)
