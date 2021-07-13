""" solution to Day 9b of Advent of Code 2020: https://adventofcode.com/2020/day/9 """

PREAMBLE = 25

def encryption_weakness_key(target_number, number_array):
    """Gets key of start of encryption weakness"""
    original_list = list(number_array)
    i = 0
    for i, _ in enumerate(number_array):
        if i < len(number_array) - 1:
            temp = number_array[i]
            temp2 = number_array[i+1]
            number_array[i] = temp + temp2
            i += 1
    jumper = 1
    while target_number not in number_array:
        j = 0
        jumper += 1
        while j < len(number_array) - jumper:
            temp = number_array[j]
            temp2 = original_list[j+jumper]
            number_array[j] = temp + temp2
            j = j + 1
    k = 0
    while k < len(number_array) - 1:
        if number_array[k] == target_number:
            return_value = k
        k += 1
    return return_value

def encryption_weakness(target_number,number_array):
    """Finds smallest and largest number in weakness range and returns their sum"""
    backup_array = list(number_array)
    start_key = encryption_weakness_key(target_number,number_array)
    i = start_key
    sum_digits = 0
    smallest_number = backup_array[i]
    largest_number = backup_array[i]
    while sum_digits < target_number:
        sum_digits += backup_array[i]
        if backup_array[i] < smallest_number:
            smallest_number = backup_array[i]
        if backup_array[i] > largest_number:
            largest_number = backup_array[i]
        i += 1
    return smallest_number + largest_number

def shift_array(number_array, new_number):
    """shift contents of number array"""
    for i, _ in enumerate(number_array):
        if i == len(number_array) - 1:
            number_array[i] = new_number
        else:
            number_array[i] = number_array[i+1]
    return number_array

def load_small_array(big_array):
    """Load the first PREAMBLE digits into the array"""
    i = 0
    new_array = []
    while i < PREAMBLE:
        new_array.append(big_array[i])
        i += 1
    return new_array

def valid_number(array, digit_sum):
    """Check if any two numbers in the array add up to digit_sum"""
    is_valid = False
    for i, _ in enumerate(array):
        j = i + 1
        while j < len(array):
            if array[i] + array[j] == digit_sum:
                is_valid = True
            j += 1
    return is_valid

def invalid_number(number_array):
    """Traverse the array and find first number that isn't a sum of two of prev 25"""
    preamble_array = load_small_array(number_array)
    i = 25
    while valid_number(preamble_array, number_array[i]):
        preamble_array = shift_array(preamble_array, number_array[i])
        i += 1
    return number_array[i]

with open("day-9.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(int(line.strip()))

print(encryption_weakness(invalid_number(new_arr),new_arr))
