""" solution to Day 13a of Advent of Code 2020: https://adventofcode.com/2020/day/13 """

def funct(buses,timestamp):
    """ Find the product of the time to wait for the best bus and the bus number """
    min_time = 999
    min_timestamp = 999
    for bus in buses:
        if bus != "x":
            bus_number = int(bus)
            next_departure = timestamp - (timestamp % bus_number) + bus_number
            if next_departure - timestamp < min_time:
                min_time = next_departure - timestamp
                min_timestamp = bus_number
    return min_time * min_timestamp

with open("day-13.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

timestamp = int(new_arr[0])
buses = new_arr[1].split(",")

print(funct(buses,timestamp))
