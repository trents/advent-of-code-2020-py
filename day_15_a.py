""" solution to Day 15a of Advent of Code 2020: https://adventofcode.com/2020/day/15 """

def funct(arr):
    """  """
    data_array = [-1] * 2020
    mini_arr = arr[0].split(",")
    iter = 0
    for i in mini_arr:
        data_array[iter] = int(i)
        iter += 1
    while iter < 2020:
        if data_array.count(data_array[iter-1]) == 1:
            data_array[iter] = 0
        else:
            last_time = iter - 1
            last_time_before_that = last_time - 1
            while data_array[last_time] != data_array[last_time_before_that]:
                last_time_before_that -= 1
            data_array[iter] = last_time - last_time_before_that
        iter += 1
    return data_array[2019]

with open("day-15.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

print(funct(new_arr))
