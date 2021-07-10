""" solution to Day 4a of Advent of Code 2020: https://adventofcode.com/2020/day/4 """

def validate_passport(passport):
    """Validates whether input string is valid passport according to rules in problem description"""
    if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
        return True
    else:
        return False

def cleanup(dirty_arr):
    """Munge the data in dirty_arr into a better array"""
    cleaned_up_arr = []
    temp_passport = ""
    for current_line in dirty_arr:
        if len(current_line) == 0:
            cleaned_up_arr.append(temp_passport)
            temp_passport = ""
        else:
            if len(temp_passport) == 0:
                temp_passport += current_line
            else:
                temp_passport += " " + current_line
    cleaned_up_arr.append(temp_passport)
    return cleaned_up_arr

def passport_count(arr):
    """Count the number of valid passports in arr"""
    clean_arr = cleanup(arr)
    clean_count = 0
    for i in clean_arr:
        if validate_passport(i):    
            clean_count += 1
    return clean_count

with open("day-4.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

print(passport_count(new_arr))
