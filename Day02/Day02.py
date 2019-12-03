"""
An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking at the
first integer (called position 0). Here, you will find an opcode - either 1, 2, or 99. The opcode indicates what to do;
for example, 99 means that the program is finished and should immediately halt. Encountering an unknown opcode means
something went wrong.

Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers
immediately after the opcode tell you these three positions - the first two indicate the positions from which you
should read the input values, and the third indicates the position at which the output should be stored.

For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20, add
those values, and then overwrite the value at position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three
integers after the opcode indicate where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping forward 4 positions.
"""
from typing import List

Opcode = List[int]


def interpret(opcode: Opcode) -> None:
    i = 0
    while opcode[i] != 99:  # halts
        # add numbers indicated by the next two numbers and store in position indicated by the 3rd number
        if opcode[i] == 1:
            p1 = opcode[i + 1]
            p2 = opcode[i + 2]
            p3 = opcode[i + 3]
            output = opcode[p1] + opcode[p2]
            opcode[p3] = output
            i += 4
        # multiply  numbers indicated by the next two numbers and store in position indicated by the 3rd number
        elif opcode[i] == 2:
            p1 = opcode[i + 1]
            p2 = opcode[i + 2]
            p3 = opcode[i + 3]
            output = opcode[p1] * opcode[p2]
            opcode[p3] = output
            i += 4
        else:
            raise RuntimeError(f"invalid opcode: {opcode[i]}")


opcode1 = [1, 0, 0, 0, 99]
interpret(opcode1)
assert (opcode1 == [2, 0, 0, 0, 99])

opcode2 = [2, 3, 0, 3, 99]
interpret(opcode2)
assert (opcode2 == [2, 3, 0, 6, 99])

opcode3 = [2, 4, 4, 5, 99, 0]
interpret(opcode3)
assert (opcode3 == [2, 4, 4, 5, 99, 9801])

opcode4 = [1, 1, 1, 4, 99, 5, 6, 0, 99]
interpret(opcode4)
assert (opcode4 == [30, 1, 1, 4, 2, 5, 6, 0, 99])


def run(opcode: Opcode, noun: int = 12, verb: int = 2) -> int:
    opcode = opcode[:]  # create copy of code
    opcode[1] = noun
    opcode[2] = verb
    interpret(opcode)
    return opcode[0]


ACTUALCODE = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 19, 5, 23, 1, 23, 9, 27, 2, 27, 6, 31, 1,
              31, 6, 35, 2, 35, 9, 39, 1, 6, 39, 43, 2, 10, 43, 47, 1, 47, 9, 51, 1, 51, 6, 55, 1, 55, 6, 59, 2, 59, 10,
              63, 1, 6, 63, 67, 2, 6, 67, 71, 1, 71, 5, 75, 2, 13, 75, 79, 1, 10, 79, 83, 1, 5, 83, 87, 2, 87, 10, 91,
              1, 5, 91, 95, 2, 95, 6, 99, 1, 99, 6, 103, 2, 103, 6, 107, 2, 107, 9, 111, 1, 111, 5, 115, 1, 115, 6, 119,
              2, 6, 119, 123, 1, 5, 123, 127, 1, 127, 13, 131, 1, 2, 131, 135, 1, 135, 10, 0, 99, 2, 14, 0, 0]

print(run(ACTUALCODE))

"""
part 2 determine what pair of inputs produces the output 19690720.

The inputs should still be provided to the program by replacing the values at addresses 1 and 2, just like before. 
In this program, the value placed in address 1 is called the noun, and the value placed in address 2 is called the verb.
 Each of the two input values will be between 0 and 99, inclusive.
 
 Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb? 
 (For example, if noun=12 and verb=2, the answer would be 1202.)
"""

target = 19690720

for noun in range(100):
    for verb in range(100):
        if run(ACTUALCODE, noun, verb) == target:
            print(noun, verb, 100 * noun + verb)
            break
