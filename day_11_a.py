""" solution to Day 11a of Advent of Code 2020: https://adventofcode.com/2020/day/11 """

def reseat(seating_array):
    """ updates the seating in seating_array """
    row_count = len(seating_array)
    col_count = len(seating_array[0])
    temp_array = [["N"]*col_count for _ in range(row_count)]

    i = 0
    while i < row_count:
        j = 0
        while j < col_count:
            if i == 0 and j == 0: # upper left corner
                if seating_array[i][j] == "L":
                    if seating_array[0][1] == "#" or seating_array[1][1] == "#" or seating_array[1][0] == "#":
                        temp_array[i][j] = "L"
                    else:
                        temp_array[i][j] = "#"
                if seating_array[i][j] == ".":
                    temp_array[i][j] = "."
                if seating_array[i][j] == "#":
                    temp_array[i][j] = "#"
            elif i == 0 and j == col_count - 1: # upper right corner
                if seating_array[i][j] == "L":
                    if seating_array[0][col_count-2] == "#" or seating_array[1][col_count-2] == "#" or seating_array[1][col_count-1] == "#":
                        temp_array[i][j] = "L"
                    else:
                        temp_array[i][j] = "#"
                if seating_array[i][j] == ".":
                    temp_array[i][j] = "."
                if seating_array[i][j] == "#":
                    temp_array[i][j] = "#"
            elif i == row_count - 1 and j == 0: # lower left corner
                if seating_array[i][j] == "L":
                    if seating_array[row_count-2][0] == "#" or seating_array[row_count-2][1] == "#" or seating_array[row_count-1][1] == "#":
                        temp_array[i][j] = "L"
                    else:
                        temp_array[i][j] = "#"
                if seating_array[i][j] == ".":
                    temp_array[i][j] = "."
                if seating_array[i][j] == "#":
                    temp_array[i][j] = "#"
            elif i == row_count - 1 and j == col_count - 1: # lower right corner
                if seating_array[i][j] == "L":
                    if seating_array[row_count-1][col_count-2] == "#" or seating_array[row_count-2][col_count-2] == "#" or seating_array[row_count-2][col_count-1] == "#":
                        temp_array[i][j] = "L"
                    else:
                        temp_array[i][j] = "#"
                if seating_array[i][j] == ".":
                    temp_array[i][j] = "."
                if seating_array[i][j] == "#":
                    temp_array[i][j] = "#"
            elif i == 0: # rest of upper row
                neighbor_count = 0
                if seating_array[i][j-1] == "#":
                    neighbor_count += 1
                if seating_array[i+1][j-1] == "#":
                    neighbor_count += 1
                if seating_array[i+1][j] == "#":
                    neighbor_count += 1
                if seating_array[i+1][j+1] == "#":
                    neighbor_count += 1
                if seating_array[i][j+1] == "#":
                    neighbor_count += 1
                if neighbor_count == 0 and seating_array[i][j] == "L":
                    temp_array[i][j] = "#"
                elif neighbor_count > 3 and seating_array[i][j] == "#":
                    temp_array[i][j] = "L"
                elif seating_array[i][j] == ".":
                    temp_array[i][j] = "."
                elif seating_array[i][j] == "#":
                    temp_array[i][j] = "#"
                else:
                    temp_array[i][j] = "L"
            elif i == row_count - 1: # rest of lower row
                neighbor_count = 0
                if seating_array[i][j-1] == "#":
                    neighbor_count += 1
                if seating_array[i-1][j-1] == "#":
                    neighbor_count += 1
                if seating_array[i-1][j] == "#":
                    neighbor_count += 1
                if seating_array[i-1][j+1] == "#":
                    neighbor_count += 1
                if seating_array[i][j+1] == "#":
                    neighbor_count += 1
                if neighbor_count == 0 and seating_array[i][j] == "L":
                    temp_array[i][j] = "#"
                elif neighbor_count > 3 and seating_array[i][j] == "#":
                    temp_array[i][j] = "L"
                elif seating_array[i][j] == ".":
                    temp_array[i][j] = "."
                elif seating_array[i][j] == "#":
                    temp_array[i][j] = "#"
                else:
                    temp_array[i][j] = "L"
            elif j == 0: # rest of left column
                neighbor_count = 0
                if seating_array[i-1][j] == "#":
                    neighbor_count += 1
                if seating_array[i-1][j+1] == "#":
                    neighbor_count += 1
                if seating_array[i][j+1] == "#":
                    neighbor_count += 1
                if seating_array[i+1][j+1] == "#":
                    neighbor_count += 1
                if seating_array[i+1][j] == "#":
                    neighbor_count += 1
                if neighbor_count == 0 and seating_array[i][j] == "L":
                    temp_array[i][j] = "#"
                elif neighbor_count > 3 and seating_array[i][j] == "#":
                    temp_array[i][j] = "L"
                elif seating_array[i][j] == ".":
                    temp_array[i][j] = "."
                elif seating_array[i][j] == "#":
                    temp_array[i][j] = "#"
                else:
                    temp_array[i][j] = "L"
            elif j == col_count - 1: # rest of right column
                neighbor_count = 0
                if seating_array[i-1][j] == "#":
                    neighbor_count += 1
                if seating_array[i-1][j-1] == "#":
                    neighbor_count += 1
                if seating_array[i][j-1] == "#":
                    neighbor_count += 1
                if seating_array[i+1][j-1] == "#":
                    neighbor_count += 1
                if seating_array[i+1][j] == "#":
                    neighbor_count += 1
                if neighbor_count == 0 and seating_array[i][j] == "L":
                    temp_array[i][j] = "#"
                elif neighbor_count > 3 and seating_array[i][j] == "#":
                    temp_array[i][j] = "L"
                elif seating_array[i][j] == ".":
                    temp_array[i][j] = "."
                elif seating_array[i][j] == "#":
                    temp_array[i][j] = "#"
                else:
                    temp_array[i][j] = "L"
            else: # rest of array
                neighbor_count = 0
                if seating_array[i-1][j-1] == "#":
                    neighbor_count += 1
                if seating_array[i-1][j] == "#":
                    neighbor_count += 1
                if seating_array[i-1][j+1] == "#":
                    neighbor_count += 1
                if seating_array[i][j-1] == "#":
                    neighbor_count += 1
                if seating_array[i][j+1] == "#":
                    neighbor_count += 1
                if seating_array[i+1][j-1] == "#":
                    neighbor_count += 1
                if seating_array[i+1][j] == "#":
                    neighbor_count += 1
                if seating_array[i+1][j+1] == "#":
                    neighbor_count += 1
                if neighbor_count == 0 and seating_array[i][j] == "L":
                    temp_array[i][j] = "#"
                elif neighbor_count > 3 and seating_array[i][j] == "#":
                    temp_array[i][j] = "L"            
                elif seating_array[i][j] == ".":
                    temp_array[i][j] = "."
                elif seating_array[i][j] == "#":
                    temp_array[i][j] = "#"
                else:
                    temp_array[i][j] = "L"
            j += 1
        i += 1
    return temp_array

def funct(new_arr):
    """ Driver """
    while new_arr != reseat(new_arr):
        new_arr = reseat(new_arr)
    return new_arr

def count_occupied_seats(arr_c):
    """ count how many seats are occupied """
    count = 0
    for i in arr_c:
        for j in i:
            if j == "#":
                count += 1
    return count

with open("day-11.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

new_arr = [list(row) for row in new_arr]

junk = funct(new_arr)

print(count_occupied_seats(junk))
