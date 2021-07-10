""" solution to Day 4b of Advent of Code 2020: https://adventofcode.com/2020/day/4 """

import re

def validate_passport(passport):
    """Validates whether input string is valid passport according to rules in problem description"""

    # Start by converting passport into a dict

    passport_dict = dict((x.strip(), y.strip())
        for x, y in (element.split(':')
        for element in passport.split(' ')))

    # Now, validate each element of the dict
    # This can definitely be made more efficient with fewer ifs, but I like to make sure the
    #   logic is clear and the code works before improving efficiency.

    result = True

    birth_year = passport_dict.get("byr")
    if birth_year:
        if int(birth_year) < 1920 or int(birth_year) > 2002:
            result = False
    else:
        result = False

    issue_year = passport_dict.get("iyr")
    if issue_year:
        if int(issue_year) < 2010 or int(issue_year) > 2020:
            result = False
    else:
        result = False

    expiration_year = passport_dict.get("eyr")
    if expiration_year:
        if int(expiration_year) < 2020 or int(expiration_year) > 2030:
            result = False
    else:
        result = False

    height = passport_dict.get("hgt")
    if height:
        if height[-2:] == "cm":
            if int(height[0:len(height)-2]) > 193 or int(height[0:len(height)-2]) < 150:
                result = False
        elif height[-2:] == "in":
            if int(height[0:len(height)-2]) > 76 or int(height[0:len(height)-2]) < 59:
                result = False
        else:
            result = False
    else:
        result = False

    hair_color = passport_dict.get("hcl")
    if hair_color:
        len_hair_color = len(hair_color[1:])
        valid_chars_in_hair_color = len(re.findall("[0-9a-f]",hair_color[1:]))
        if hair_color[0] != "#" or len_hair_color != 6 or valid_chars_in_hair_color != 6:
            result = False
    else:
        result = False

    eye_color = passport_dict.get("ecl")
    if eye_color:
        if eye_color not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            result = False
    else:
        result = False

    pass_id = passport_dict.get("pid")
    if pass_id:
        if len(pass_id) != 9 or len(re.findall("[0-9]",pass_id)) != 9:
            result = False
    else:
        result = False

    return result

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
