"""
https://adventofcode.com/2019/day/4
It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
"""

from typing import List
from collections import Counter

ACTUALLOW = 197487
ACTUALHIGH = 673251


def is_valid(password: int) -> bool:
    p = [int(x) for x in str(password)]
    correct_length = (len(p) == 6)
    double = has_duplicate(p)
    increasing = is_increasing(p)
    return correct_length and double and increasing


def has_duplicate(password: List[str]) -> bool:
    for i in range(1, len(password)):
        if password[i] == password[i-1]:
            return True
    return False


def is_increasing(password: List[str]) -> bool:
    for i in range(1, len(password)):
        if password[i] < password[i-1]:
            return False
    return True


assert is_valid(111111)
assert not is_valid(223450)
assert not is_valid(123789)


def count_valid(low: int = ACTUALLOW, high: int = ACTUALHIGH) -> int:
    count = 0
    for num in range(low, high+1):
        if is_valid(num):
            count += 1
    return count

"""
Part 2:
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of 
matching digits.
"""


def has_correct_duplicate(password: List[int]) -> bool:
    pairs = zip(password, password[1:])
    dupes = [(x, y) for (x, y) in pairs if x == y]
    cnt = Counter(dupes)
    if all(v > 1 for v in cnt.values()):
        return False
    return True


def is_valid2(password: int) -> bool:
    p = [int(x) for x in str(password)]
    correct_length = (len(p) == 6)
    has_dupe = has_duplicate(p)
    has_correct_dupe = has_correct_duplicate(p)
    increasing = is_increasing(p)
    return correct_length and has_dupe and increasing and has_correct_dupe


def count_valid2(low: int = ACTUALLOW, high: int = ACTUALHIGH) -> int:
    count = 0
    for num in range(low, high+1):
        if is_valid2(num):
            count += 1
    return count


assert is_valid2(112233)
assert not is_valid2(123444)
assert is_valid2(111122)

print(count_valid())
print(count_valid2())

