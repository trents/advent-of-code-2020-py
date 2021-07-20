""" solution to Day 12a of Advent of Code 2020: https://adventofcode.com/2020/day/12 """

def manhattan(arr):
    """ calculate Manhattan distance after following directions in arr """
    total_north = 0
    total_east = 0
    cur_dir = "E"
    for i in arr:
        command = i[0]
        number = int(i[1:])
        if command == "N":
           total_north += number
        elif command == "S":
           total_north -= number
        elif command == "E":
           total_east += number
        elif command == "W":
           total_east -= number
        elif command == "L":
           number = number % 360
           if number == 90:
               if cur_dir == "E":
                   cur_dir = "N"
               elif cur_dir == "N":
                   cur_dir = "W"
               elif cur_dir == "W":
                   cur_dir = "S"
               else:
                   cur_dir = "E"
           elif number == 180:
               if cur_dir == "E":
                   cur_dir = "W"
               elif cur_dir == "N":
                   cur_dir = "S"
               elif cur_dir == "W":
                   cur_dir = "E"
               else:
                   cur_dir = "N"
           elif number == 270:
               if cur_dir == "E":
                   cur_dir = "S"
               elif cur_dir == "N":
                   cur_dir = "E"
               elif cur_dir == "W":
                   cur_dir = "N"
               else:
                   cur_dir = "W"
        elif command == "R":
           number = number % 360
           if number == 270:
               if cur_dir == "E":
                   cur_dir = "N"
               elif cur_dir == "N":
                   cur_dir = "W"
               elif cur_dir == "W":
                   cur_dir = "S"
               else:
                   cur_dir = "E"
           elif number == 180:
               if cur_dir == "E":
                   cur_dir = "W"
               elif cur_dir == "N":
                   cur_dir = "S"
               elif cur_dir == "W":
                   cur_dir = "E"
               else:
                   cur_dir = "N"
           elif number == 90:
               if cur_dir == "E":
                   cur_dir = "S"
               elif cur_dir == "N":
                   cur_dir = "E"
               elif cur_dir == "W":
                   cur_dir = "N"
               else:
                   cur_dir = "W"
        elif command == "F":
            if cur_dir == "N":
               total_north += number
            elif cur_dir == "S":
               total_north -= number
            elif cur_dir == "E":
               total_east += number
            elif cur_dir == "W":
               total_east -= number
    return abs(total_north) + abs(total_east)

with open("day-12.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

print(manhattan(new_arr))
