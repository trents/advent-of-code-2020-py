""" solution to Day 2a of Advent of Code 2020: https://adventofcode.com/2020/day/2 """

import re

def funct(arr):
    """Validates character count in substring and increments result if valid"""
    res = 0
    test_case = 0
    for i in arr:
        test = re.split("[-: ]",i)
        test_case = test[4].count(test[2])
        if int(test[1]) >= test_case >= int(test[0]):
            res = res + 1
    return res

with open("day-2.txt") as file:
    d = file.readlines()

print(funct(d))
