""" solution to Day 5a of Advent of Code 2020: https://adventofcode.com/2020/day/5 """

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

def max_seat_id(arr):
    """go through arr and find the highest seat ID and return it"""
    max_seat_num = 0
    for seat_string in arr:
        temp_seat_num = seat_id_calc(seat_string)
        if temp_seat_num > max_seat_num:
            max_seat_num = temp_seat_num
    return max_seat_num

with open("day-5.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

print(max_seat_id(new_arr))
