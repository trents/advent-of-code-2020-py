""" solution to Day 11b of Advent of Code 2020: https://adventofcode.com/2020/day/11 """

def see_direction(seating_array, direction, row, col):
    """ First non-. in that direction"""
    if direction == 0: # vert up
        temp_i = row - 1
        while temp_i > -1:
            if seating_array[temp_i][col] == "#":
                return "#"
            elif seating_array[temp_i][col] == "L":
                return "L"
            temp_i -= 1
        return "."   
    elif direction == 1: # up and right
        temp_i = row - 1
        temp_j = col + 1
        while temp_i > -1 and temp_j < len(seating_array[0]):
            if seating_array[temp_i][temp_j] == "#":
                return "#"
            elif seating_array[temp_i][temp_j] == "L":
                return "L"
            temp_i -= 1
            temp_j += 1
        return "."
    elif direction == 2: # right
        temp_j = col + 1
        while temp_j < len(seating_array[0]):
            if seating_array[row][temp_j] == "#":
                return "#"
            elif seating_array[row][temp_j] == "L":
                return "L"
            temp_j += 1
        return "."
    elif direction == 3: # down and right
        temp_i = row + 1
        temp_j = col + 1
        while temp_i < len(seating_array) and temp_j < len(seating_array[0]):
            if seating_array[temp_i][temp_j] == "#":
                return "#"
            elif seating_array[temp_i][temp_j] == "L":
                return "L"
            temp_i += 1
            temp_j += 1
        return "."
    elif direction == 4: # down
        temp_i = row + 1
        while temp_i < len(seating_array):
            if seating_array[temp_i][col] == "#":
                return "#"
            elif seating_array[temp_i][col] == "L":
                return "L"
            temp_i += 1
        return "."
    elif direction == 5: # down and left
        temp_i = row + 1
        temp_j = col - 1
        while temp_i < len(seating_array) and temp_j > -1:
            if seating_array[temp_i][temp_j] == "#":
                return "#"
            elif seating_array[temp_i][temp_j] == "L":
                return "L"
            temp_i += 1
            temp_j -= 1
        return "."
    elif direction == 6: # left
        temp_j = col - 1
        while temp_j > -1:
            if seating_array[row][temp_j] == "#":
                return "#"
            elif seating_array[row][temp_j] == "L":
                return "L"
            temp_j -= 1
        return "."
    else: # up and left
        temp_i = row - 1
        temp_j = col - 1
        while temp_i > -1 and temp_j > -1:
            if seating_array[temp_i][temp_j] == "#":
                return "#"
            elif seating_array[temp_i][temp_j] == "L":
                return "L"
            temp_i -= 1
            temp_j -= 1
        return "."

def reseat(seating_array):
    row_count = len(seating_array)
    col_count = len(seating_array[0])
    temp_array = [["N"]*col_count for _ in range(row_count)] 

    i = 0
    while i < row_count:
        j = 0
        while j < col_count:
            if i == 0 and j == 0: # upper left corner
                if seating_array[i][j] == "L":
                    if see_direction(seating_array,2,0,0) == "#" or see_direction(seating_array,3,0,0) == "#" or see_direction(seating_array,4,0,0) == "#":
                        temp_array[i][j] = "L"
                    else:
                        temp_array[i][j] = "#"
                if seating_array[i][j] == ".":
                    temp_array[i][j] = "."
                if seating_array[i][j] == "#":
                    temp_array[i][j] = "#"
            elif i == 0 and j == col_count - 1: # upper right corner
                if seating_array[i][j] == "L":
                    if see_direction(seating_array,4,i,j) == "#" or see_direction(seating_array,5,i,j) == "#" or see_direction(seating_array,6,i,j) == "#":
                        temp_array[i][j] = "L"
                    else:
                        temp_array[i][j] = "#"
                if seating_array[i][j] == ".":
                    temp_array[i][j] = "."
                if seating_array[i][j] == "#":
                    temp_array[i][j] = "#"
            elif i == row_count - 1 and j == 0: # lower left corner
                if seating_array[i][j] == "L":
                    if see_direction(seating_array,2,i,j) == "#" or see_direction(seating_array,1,i,j) == "#" or see_direction(seating_array,0,i,j) == "#":
                        temp_array[i][j] = "L"
                    else:
                        temp_array[i][j] = "#"
                if seating_array[i][j] == ".":
                    temp_array[i][j] = "."
                if seating_array[i][j] == "#":
                    temp_array[i][j] = "#"
            elif i == row_count - 1 and j == col_count - 1: # lower right corner
                if seating_array[i][j] == "L":
                    if see_direction(seating_array,0,i,j) == "#" or see_direction(seating_array,7,i,j) == "#" or see_direction(seating_array,6,i,j) == "#":
                        temp_array[i][j] = "L"
                    else:
                        temp_array[i][j] = "#"
                if seating_array[i][j] == ".":
                    temp_array[i][j] = "."
                if seating_array[i][j] == "#":
                    temp_array[i][j] = "#"
            elif i == 0: # rest of upper row
                neighbor_count = 0
                if see_direction(seating_array,2,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,3,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,4,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,5,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,6,i,j) == "#":
                    neighbor_count += 1
                if neighbor_count == 0 and seating_array[i][j] == "L":
                    temp_array[i][j] = "#"
                elif neighbor_count > 4 and seating_array[i][j] == "#":
                    temp_array[i][j] = "L"
                elif seating_array[i][j] == ".":
                    temp_array[i][j] = "."
                elif seating_array[i][j] == "#":
                    temp_array[i][j] = "#"
                else:
                    temp_array[i][j] = "L"
            elif i == row_count - 1: # rest of lower row
                neighbor_count = 0
                if see_direction(seating_array,6,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,7,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,0,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,1,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,2,i,j) == "#":
                    neighbor_count += 1
                if neighbor_count == 0 and seating_array[i][j] == "L":
                    temp_array[i][j] = "#"
                elif neighbor_count > 4 and seating_array[i][j] == "#":
                    temp_array[i][j] = "L"
                elif seating_array[i][j] == ".":
                    temp_array[i][j] = "."
                elif seating_array[i][j] == "#":
                    temp_array[i][j] = "#"
                else:
                    temp_array[i][j] = "L"
            elif j == 0: # rest of left column
                neighbor_count = 0
                if see_direction(seating_array,0,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,1,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,2,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,3,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,4,i,j) == "#":
                    neighbor_count += 1
                if neighbor_count == 0 and seating_array[i][j] == "L":
                    temp_array[i][j] = "#"
                elif neighbor_count > 4 and seating_array[i][j] == "#":
                    temp_array[i][j] = "L"
                elif seating_array[i][j] == ".":
                    temp_array[i][j] = "."
                elif seating_array[i][j] == "#":
                    temp_array[i][j] = "#"
                else:
                    temp_array[i][j] = "L"
            elif j == col_count - 1: # rest of right column
                neighbor_count = 0
                if see_direction(seating_array,4,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,5,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,6,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,7,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,0,i,j) == "#":
                    neighbor_count += 1
                if neighbor_count == 0 and seating_array[i][j] == "L":
                    temp_array[i][j] = "#"
                elif neighbor_count > 4 and seating_array[i][j] == "#":
                    temp_array[i][j] = "L"
                elif seating_array[i][j] == ".":
                    temp_array[i][j] = "."
                elif seating_array[i][j] == "#":
                    temp_array[i][j] = "#"
                else:
                    temp_array[i][j] = "L"
            else: # rest of array
                neighbor_count = 0
                if see_direction(seating_array,0,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,1,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,2,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,3,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,4,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,5,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,6,i,j) == "#":
                    neighbor_count += 1
                if see_direction(seating_array,7,i,j) == "#":
                    neighbor_count += 1
                if neighbor_count == 0 and seating_array[i][j] == "L":
                    temp_array[i][j] = "#"
                elif neighbor_count > 4 and seating_array[i][j] == "#":
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
    while new_arr != reseat(new_arr):
        new_arr = reseat(new_arr)
    return new_arr

def count_occupied_seats(arr_c):
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
row_count = len(junk)
col_count = len(junk[0])
i = 0
while i < row_count:
    j = 0
    blank_string = ""
    while j < col_count:
        blank_string = blank_string + junk[i][j]
        j += 1
    print(blank_string)
    i += 1

print(count_occupied_seats(junk))
