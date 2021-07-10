""" solution to Day 2b of Advent of Code 2020: https://adventofcode.com/2020/day/2 """

import re

def funct(arr):
    """Validates characters in substring, XORs them, and increments result if valid"""
    res = 0
    for i in arr:
        test = re.split("[-: ]",i)
        test_case1 = test[4][int(test[0])-1]
        test_case2 = test[4][int(test[1])-1]
        test_case1_valid = False
        test_case2_valid = False
        if test_case1 == test[2]:
            test_case1_valid = True
        if test_case2 == test[2]:
            test_case2_valid = True
        if bool(test_case1_valid) ^ bool(test_case2_valid):
            res = res + 1
    return res

with open("day-2.txt") as file:
    d = file.readlines()

print(funct(d))
