""" solution to Day 5b of Advent of Code 2020: https://adventofcode.com/2020/day/1 """

def seat_id_calc(seat_id_string):
    """calculate the seat ID of a given seat identifier"""
    seat_id = 0
    row_id = 0
    if seat_id_string[0] == "B":
        seat_id = seat_id + 64
    if seat_id_string[1] == "B":
        seat_id = seat_id + 32
    if seat_id_string[2] == "B":
        seat_id = seat_id + 16
    if seat_id_string[3] == "B":
        seat_id = seat_id + 8
    if seat_id_string[4] == "B":
        seat_id = seat_id + 4
    if seat_id_string[5] == "B":
        seat_id = seat_id + 2
    if seat_id_string[6] == "B":
        seat_id = seat_id + 1
    if seat_id_string[7] == "R":
        row_id = row_id + 4
    if seat_id_string[8] == "R":
        row_id = row_id + 2
    if seat_id_string[9] == "R":
        row_id = row_id + 1

    return seat_id * 8 + row_id

def my_seat_id(arr):
    """go through arr and find empty seat between two full seats"""
    full_seat_id = []
    my_seat_num = 0
    for seat_string in arr:
        full_seat_id.append(seat_id_calc(seat_string))
    full_seat_id.sort()
    i = 0
    while i < len(full_seat_id) - 1:
        if full_seat_id[i] == full_seat_id[i+1] - 2:
            my_seat_num = full_seat_id[i] + 1
        i += 1
    return my_seat_num

with open("day-5.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

print(my_seat_id(new_arr))
