"""
https://adventofcode.com/2019/day/5
instructions online are garbage

part 1:
1. Add new variable parameter
2. Instruction = last two digits of parameter
3. instructions follow day 2 code
4. add if instruction == 3 then store input value(taken as input parameter) to position in indicated in value i+1
5. add if instruciton == 4 then store save value at position i+1 to results list to be returned later
6. add 3 mode variables that get value from parameter reading right from left
    mode1 = parameter[2]
    mode2 = parameter[1]
    mode3 = parameter[0]
7. if mode == 0 follow steps above
8. if mode == 1 then take value of position instead of value AT position. i.e. take opcode[i] instead of opcode[i+1]
9. return results list

part 2:
1. add if instruction == 5. check opcode i + 1. If non-zero then i = opcode[i+2]
2. add if instuction == 6. check opcode i + 1. If zero then i = opcode[i+2]
3. add if instruction == 7. check opcode i + 1 < opcode i + 2 then opcode[i+3] = 1 else opcode[i+3] = 0
4. add if instruction == 8. check opcode i + 1 = opcode i + 2 then opcode[i+3] = 1 else opcode[i+3] = 0
5. carry on same modes from part 1
"""

from typing import List

Opcode = List[int]


def digits(n: int, num_digits: int = 6) -> List[int]:
    d = []
    for _ in range(num_digits):
        d.append(n % 10)
        n = n // 10
    return list(reversed(d))


def interpret(opcode: Opcode, input: int) -> List[int]:
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
            opcode[p1] = input
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


def run(opcode: Opcode) -> int:
    opcode = opcode[:]  # create copy of code
    return interpret(opcode, 5)


ACTUALCODE = [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1101, 65, 39, 225, 2, 14, 169, 224, 101, -2340, 224,
              224, 4, 224, 1002, 223, 8, 223, 101, 7, 224, 224, 1, 224, 223, 223, 1001, 144, 70, 224, 101, -96, 224,
              224, 4, 224, 1002, 223, 8, 223, 1001, 224, 2, 224, 1, 223, 224, 223, 1101, 92, 65, 225, 1102, 42, 8, 225,
              1002, 61, 84, 224, 101, -7728, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 5, 224, 1, 223, 224, 223,
              1102, 67, 73, 224, 1001, 224, -4891, 224, 4, 224, 102, 8, 223, 223, 101, 4, 224, 224, 1, 224, 223, 223,
              1102, 54, 12, 225, 102, 67, 114, 224, 101, -804, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 3, 224,
              1, 224, 223, 223, 1101, 19, 79, 225, 1101, 62, 26, 225, 101, 57, 139, 224, 1001, 224, -76, 224, 4, 224,
              1002, 223, 8, 223, 1001, 224, 2, 224, 1, 224, 223, 223, 1102, 60, 47, 225, 1101, 20, 62, 225, 1101, 47,
              44, 224, 1001, 224, -91, 224, 4, 224, 1002, 223, 8, 223, 101, 2, 224, 224, 1, 224, 223, 223, 1, 66, 174,
              224, 101, -70, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 6, 224, 1, 223, 224, 223, 4, 223, 99, 0, 0,
              0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227,
              99999, 1005, 0, 256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999,
              1006, 227, 274, 1105, 1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1,
              0, 1105, 1, 99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1,
              99999, 108, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 329, 101, 1, 223, 223, 1107, 226, 677, 224, 1002,
              223, 2, 223, 1005, 224, 344, 101, 1, 223, 223, 8, 226, 677, 224, 102, 2, 223, 223, 1006, 224, 359, 101,
              1, 223, 223, 108, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 374, 1001, 223, 1, 223, 1108, 226, 677,
              224, 1002, 223, 2, 223, 1005, 224, 389, 101, 1, 223, 223, 1007, 677, 677, 224, 1002, 223, 2, 223, 1006,
              224, 404, 1001, 223, 1, 223, 1108, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 419, 1001, 223, 1, 223,
              1008, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 434, 101, 1, 223, 223, 107, 677, 677, 224, 102, 2, 223,
              223, 1006, 224, 449, 1001, 223, 1, 223, 1007, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 464, 101, 1,
              223, 223, 7, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 479, 101, 1, 223, 223, 1007, 226, 226, 224, 102,
              2, 223, 223, 1005, 224, 494, 101, 1, 223, 223, 7, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 509, 101,
              1, 223, 223, 1008, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 524, 1001, 223, 1, 223, 108, 226, 677,
              224, 1002, 223, 2, 223, 1006, 224, 539, 101, 1, 223, 223, 8, 226, 226, 224, 102, 2, 223, 223, 1006, 224,
              554, 101, 1, 223, 223, 8, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 569, 1001, 223, 1, 223, 1108, 677,
              226, 224, 1002, 223, 2, 223, 1006, 224, 584, 101, 1, 223, 223, 1107, 677, 226, 224, 1002, 223, 2, 223,
              1005, 224, 599, 101, 1, 223, 223, 107, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 614, 1001, 223, 1,
              223, 7, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 629, 1001, 223, 1, 223, 107, 677, 226, 224, 1002,
              223, 2, 223, 1005, 224, 644, 1001, 223, 1, 223, 1107, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 659,
              101, 1, 223, 223, 1008, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 674, 1001, 223, 1, 223, 4, 223, 99,
              226]

print(run(ACTUALCODE))
