"""
https://adventofcode.com/2019/day/7
"""

from typing import List
from itertools import permutations

Opcode = List[int]


def digits(n: int, num_digits: int = 6) -> List[int]:
    d = []
    for _ in range(num_digits):
        d.append(n % 10)
        n = n // 10
    return list(reversed(d))


def interpret(opcode: Opcode, input_instruction: List[int]) -> List[int]:
    i = 0
    result = []
    while opcode[i] != 99:  # halts
        parameter = digits(opcode[i], 5)
        instruction = parameter[-1]
        mode1 = parameter[2]
        mode2 = parameter[1]
        mode3 = parameter[0]
        # print(f"current location {i}, current instruction {instruction}")
        # add numbers indicated by the next two numbers and store in position indicated by the 3rd number
        if instruction == 1:
            if mode1 == 0:
                p1 = opcode[opcode[i + 1]]
            elif mode1 == 1:
                p1 = opcode[i + 1]
            else:
                raise RuntimeError(f"invalid Mode: {mode1}")
            if mode2 == 0:
                p2 = opcode[opcode[i + 2]]
            elif mode2 == 1:
                p2 = opcode[i + 2]
            else:
                raise RuntimeError(f"invalid Mode: {mode2}")
            if mode3 == 0:
                p3 = opcode[i + 3]
            else:
                raise RuntimeError(f"invalid Mode: {mode3}")
            output = p1 + p2
            # print(f"Writing {output} to position {p3}")
            opcode[p3] = output
            i += 4
        # multiply  numbers indicated by the next two numbers and store in position indicated by the 3rd number
        elif instruction == 2:
            if mode1 == 0:
                p1 = opcode[opcode[i + 1]]
            elif mode1 == 1:
                p1 = opcode[i + 1]
            else:
                raise RuntimeError(f"invalid Mode: {mode1}")
            if mode2 == 0:
                p2 = opcode[opcode[i + 2]]
            elif mode2 == 1:
                p2 = opcode[i + 2]
            else:
                raise RuntimeError(f"invalid Mode: {mode2}")
            if mode3 == 0:
                p3 = opcode[i + 3]
            else:
                raise RuntimeError(f"invalid Mode: {mode3}")
            output = p1 * p2
            # print(f"Writing {output} to position {p3}")
            opcode[p3] = output
            i += 4
        elif instruction == 3:
            p1 = opcode[i + 1]
            opcode[p1] = input_instruction[0]
            input_instruction = input_instruction[1:]
            i += 2
            # print(f"Writing {input} to position {p1}")
        elif instruction == 4:
            if mode1 == 0:
                p1 = opcode[i + 1]
                output = opcode[p1]
            else:
                output = opcode[i + 1]
            i += 2
            # print(f"Adding {output} to results")
            result.append(output)
        elif instruction == 5:
            if mode1 == 0:
                p1 = opcode[opcode[i + 1]]
            elif mode1 == 1:
                p1 = opcode[i + 1]
            else:
                raise RuntimeError(f"invalid Mode: {mode1}")
            if mode2 == 0:
                p2 = opcode[opcode[i + 2]]
            elif mode2 == 1:
                p2 = opcode[i + 2]
            else:
                raise RuntimeError(f"invalid Mode: {mode2}")
            if p1 != 0:
                # print(f"jumping to position {p2} with value of {opcode[p2]}")
                i = p2
            else:
                # print(f"jumping to position {i+3} with value of {opcode[i+3]}")
                i += 3
        elif instruction == 6:
            if mode1 == 0:
                p1 = opcode[opcode[i + 1]]
            elif mode1 == 1:
                p1 = opcode[i + 1]
            else:
                raise RuntimeError(f"invalid Mode: {mode1}")
            if mode2 == 0:
                p2 = opcode[opcode[i + 2]]
            elif mode2 == 1:
                p2 = opcode[i + 2]
            else:
                raise RuntimeError(f"invalid Mode: {mode2}")
            if p1 == 0:
                # print(f"jumping to position {p2} with value of {opcode[p2]}")
                i = p2
            else:
                # print(f"jumping to position {i+3} with value of {opcode[i+3]}")
                i += 3
        elif instruction == 7:
            if mode1 == 0:
                p1 = opcode[opcode[i + 1]]
            elif mode1 == 1:
                p1 = opcode[i + 1]
            else:
                raise RuntimeError(f"invalid Mode: {mode1}")
            if mode2 == 0:
                p2 = opcode[opcode[i + 2]]
            elif mode2 == 1:
                p2 = opcode[i + 2]
            else:
                raise RuntimeError(f"invalid Mode: {mode2}")
            if mode3 == 0:
                p3 = opcode[i + 3]
            elif mode3 == 1:
                p3 = i + 3
            else:
                raise RuntimeError(f"invalid Mode: {mode3}")
            if p1 < p2:
                # print(f"Writing 1 to position {opcode[p3]}")
                opcode[p3] = 1
            else:
                # print(f"Writing 0 to position {opcode[p3]}")
                opcode[p3] = 0
            i += 4
        elif instruction == 8:
            if mode1 == 0:
                p1 = opcode[opcode[i + 1]]
            elif mode1 == 1:
                p1 = opcode[i + 1]
            else:
                raise RuntimeError(f"invalid Mode: {mode1}")
            if mode2 == 0:
                p2 = opcode[opcode[i + 2]]
            elif mode2 == 1:
                p2 = opcode[i + 2]
            else:
                raise RuntimeError(f"invalid Mode: {mode2}")
            if mode3 == 0:
                p3 = opcode[i + 3]
            elif mode3 == 1:
                p3 = i + 3
            else:
                raise RuntimeError(f"invalid Mode: {mode3}")
            if p1 == p2:
                # print(f"Writing 1 to position {opcode[p3]}")
                opcode[p3] = 1
            else:
                # print(f"Writing 0 to position {opcode[p3]}")
                opcode[p3] = 0
            i += 4
        else:
            raise RuntimeError(f"invalid opcode: {opcode[i]}")
    return result


def run(opcode: Opcode, instruction: List[int]) -> List[int]:
    opcode = opcode[:]  # create copy of code
    return interpret(opcode, instruction)


ACTUAL_PROGRAM = [3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 42, 67, 84, 97, 118, 199, 280, 361, 442, 99999, 3, 9, 101, 4, 9,
                9, 102, 5, 9, 9, 101, 2, 9, 9, 1002, 9, 2, 9, 4, 9, 99, 3, 9, 101, 5, 9, 9, 102, 5, 9, 9, 1001, 9, 5, 9,
                102, 3, 9, 9, 1001, 9, 2, 9, 4, 9, 99, 3, 9, 1001, 9, 5, 9, 1002, 9, 2, 9, 1001, 9, 5, 9, 4, 9, 99, 3,
                9, 1001, 9, 5, 9, 1002, 9, 3, 9, 4, 9, 99, 3, 9, 102, 4, 9, 9, 101, 4, 9, 9, 102, 2, 9, 9, 101, 3, 9, 9,
                4, 9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2,
                9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102,
                2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9,
                101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3,
                9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9,
                3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9,
                4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9,
                9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 99, 3, 9, 102,
                2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9,
                1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9,
                1001, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 99, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9,
                3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4,
                9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 2, 9,
                4, 9, 99]

# print(run(input_signal))

test_input = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
test_phase = (4, 3, 2, 1, 0)


def run_amp(program: List[int], input_signal: int, phase: int) -> int:
    inputs = [phase, input_signal]
    output = run(program, inputs)[0]
    return output


def run_all(program: List[int], phases: tuple) -> int:
    last_output = 0
    for phase in phases:
        last_output = run_amp(program, last_output, phase)
    return last_output


assert run_all(test_input, test_phase) == 43210
assert run_all([3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0],
               (0, 1, 2, 3, 4)) == 54321
assert run_all(
    [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31,
     4, 31, 99, 0, 0, 0],
    (1, 0, 4, 3, 2)) == 65210


def max_output() -> int:
    perms = permutations(range(5))
    output = []
    for perm in perms:
        output.append(run_all(ACTUAL_PROGRAM, perm))
    return max(output)


print(max_output())
