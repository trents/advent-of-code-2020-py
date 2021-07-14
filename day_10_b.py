""" solution to Day 10b of Advent of Code 2020: https://adventofcode.com/2020/day/10 """

def gap_count(arr):
    """Count the total number of charger arrangements"""
    # I'm doing this by counting possible paths in the array
    paths_array = [0] * len(arr)
    if arr[0] == 1 or arr[0] == 2 or arr[0] == 3: # the first element is reachable from the start
        paths_array[0] = 1
    if arr[1] == 2 or arr[1] == 3: # the second element is reachable from the start
        paths_array[1] = 1
    if arr[2] == 3: # the third element is reachable from the start
        paths_array[2] = 1
    i = 0
    value = arr[0]
    while i < len(arr):
        if i + 3 < len(arr): # the element 3 away in the array is reachable
            if value + 3 == arr[i+3]:
                paths_array[i+3] += paths_array[i]
        if i + 2 < len(arr): # the element 2 away in the array is reachable
            if value + 2 == arr[i+2] or value + 3 == arr[i+2]:
                paths_array[i+2] += paths_array[i]
        if i + 1 < len(arr): # the next telement in the array is reachable
            if value + 1 == arr[i+1] or value + 2 == arr[i+1] or value + 3 == arr[i+1]:
                paths_array[i+1] += paths_array[i]
            value = arr[i+1]
        i += 1
    return paths_array[len(arr)-1]

with open("day-10.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(int(line.strip()))

new_arr.sort()
print(gap_count(new_arr))
