""" solution to Day 3b of Advent of Code 2020: https://adventofcode.com/2020/day/3 """

def trees_hit(arr, horiz, vert):
    """Traverse the map stored in arr, incrementing result whenever you hit a tree (#)"""
    count_vert = 0
    count_horiz = 0
    result = 0
    while count_vert < len(arr):
        count_horiz = count_horiz % len(arr[0])
        if arr[count_vert][count_horiz] == "#":
            result = result + 1
        count_vert += vert
        count_horiz += horiz 
    return result

def solver(arr):
    """Traverse the map multiple times as described in problem and multiply results"""
    return trees_hit(arr,1,1) * trees_hit(arr,3,1) * trees_hit(arr,5,1) * trees_hit(arr,7,1) * trees_hit(arr,1,2)

with open("day-3.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

print(solver(new_arr))
