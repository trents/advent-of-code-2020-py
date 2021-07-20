""" solution to Day 12b of Advent of Code 2020: https://adventofcode.com/2020/day/12 """

def manhattan(arr):
    """ calculate Manhattan distance after following directions in arr """
    total_north = 0
    total_east = 0
    cur_waypoint_north = 1
    cur_waypoint_east = 10
    for i in arr:
        command = i[0]
        number = int(i[1:])
        if command == "N":
           cur_waypoint_north += number
        elif command == "S":
           cur_waypoint_north -= number
        elif command == "E":
           cur_waypoint_east += number
        elif command == "W":
           cur_waypoint_east -= number
        elif command == "L":
           number = number % 360
           if number == 90:
               temp_east = 0 - cur_waypoint_north
               cur_waypoint_north = cur_waypoint_east
               cur_waypoint_east = temp_east         
           elif number == 180:
               cur_waypoint_north = 0 - cur_waypoint_north
               cur_waypoint_east = 0 - cur_waypoint_east
           elif number == 270:
               temp_north = 0 - cur_waypoint_east
               cur_waypoint_east = cur_waypoint_north
               cur_waypoint_north = temp_north
        elif command == "R":
           number = number % 360
           if number == 270:
               temp_east = 0 - cur_waypoint_north
               cur_waypoint_north = cur_waypoint_east  
               cur_waypoint_east = temp_east
           elif number == 180:
               cur_waypoint_north = 0 - cur_waypoint_north
               cur_waypoint_east = 0 - cur_waypoint_east
           elif number == 90:
               temp_north = 0 - cur_waypoint_east
               cur_waypoint_east = cur_waypoint_north
               cur_waypoint_north = temp_north
        elif command == "F":
           total_north += cur_waypoint_north * number 
           total_east += cur_waypoint_east * number
    return abs(total_north) + abs(total_east)

with open("day-12.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

print(manhattan(new_arr))
