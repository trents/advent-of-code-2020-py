""" solution to Day 3a of Advent of Code 2020: https://adventofcode.com/2020/day/3 """

def funct(arr):
    """Traverse the map stored in arr, incrementing result whenever you hit a tree (#)"""
    count_i = 0
    result = 0
    while count_i < len(arr):
        count_j = count_i * 3 % len(arr[0])
        if arr[count_i][count_j] == "#":
            result = result + 1
        count_i = count_i + 1
    return result

with open("day-3.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

print(funct(new_arr))
