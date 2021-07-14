""" solution to Day 10a of Advent of Code 2020: https://adventofcode.com/2020/day/10 """

def gap_count(arr):
    """Count the 1 and 3 gaps in arr, then return the product of them"""
    one_count = 0
    three_count = 1 # the gap between the last charger and the device
    i = 0
    if arr[0] == 1:
       one_count += 1
    elif arr[0] == 3:
       three_count += 1
    while i < len(arr) - 1:
        if arr[i] + 1 == arr[i+1]:
           one_count += 1
        elif arr[i] + 3 == arr[i+1]:
           three_count += 1
        i += 1
    return one_count * three_count

with open("day-10.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(int(line.strip()))

new_arr.sort()
print(gap_count(new_arr))
