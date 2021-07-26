""" solution to Day 16a of Advent of Code 2020: https://adventofcode.com/2020/day/16 """

def funct(valid_values,ticket_array):
    """ Check if values aren't in valid values, then sum the invalid ones """
    result = 0
    for j in ticket_array:
       ticket_split = j.split(",")
       k = 0
       while k < len(ticket_split):
           if int(ticket_split[k]) not in valid_values:
              result = result + int(ticket_split[k])
           k += 1
    return result

with open("day-16.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

i = 0
range_array = []

while len(new_arr[i]) > 0:
    line_arr = new_arr[i].split(":")
    values = line_arr[1].strip()
    ranges = values.split(" ")
    range_array.append(ranges[0])
    range_array.append(ranges[2])
    i += 1

valid_values = []

for range in range_array:
    borders = range.split("-")
    start = int(borders[0])
    stop = int(borders[1])
    j = start
    while j <= stop:
        valid_values.append(j)
        j += 1

valid_values_u = set(valid_values)
valid_values_f = list(valid_values_u)

i += 5 # skipping my ticket 

tickets_array = []

while i < len(new_arr):
    tickets_array.append(new_arr[i])
    i += 1

print(funct(valid_values_f,tickets_array))
