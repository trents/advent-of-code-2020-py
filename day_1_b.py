""" solution to Day 1b of Advent of Code 2020: https://adventofcode.com/2020/day/1 """

def funct(arr):
    """Find three items that sum to 2020, then return their product"""
    count_i = 0
    while count_i < len(arr):
        count_j = count_i + 1
        while count_j < len(arr):
            count_k = count_j + 1
            while count_k < len(arr):
                if int(arr[count_i]) + int(arr[count_j]) + int(arr[count_k]) == 2020:
                    return int(arr[count_i]) * int(arr[count_j]) * int(arr[count_k])
                count_k = count_k + 1
            count_j = count_j + 1
        count_i = count_i + 1

with open("day-1.txt") as file:
    d = file.readlines()

print(funct(d))
