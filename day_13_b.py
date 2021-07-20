""" solution to Day 13b of Advent of Code 2020: https://adventofcode.com/2020/day/13 """

def funct(buses):
    """ Find the earliest timestamp at which all named buses depart sequentially """
    # I rewrote this algorithm several times to get speed down from many minutes to fraction of a second.
    # The super slow solution checks each possible timestamp but I wanted speed!

    bus_list = {} # create a dict with keys being the items in buses
    for id, bus in enumerate(buses):
        if bus != 'x':
            bus_list[int(bus)] = -id % int(bus) # values are the number of seconds between this bus's departure and previous bus

    iterator = 0
    increment = 1
    for bus in bus_list.keys(): # for each bus
        while iterator % bus != bus_list[bus]: # if a bus isn't departing right now
            iterator += increment # iterate until a bus departs
        increment *= bus # then multiply incrementor by the bus number

    return iterator

with open("day-13.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

timestamp = int(new_arr[0])
buses = new_arr[1].split(",")

print(funct(buses))
