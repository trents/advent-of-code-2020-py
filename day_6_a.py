""" solution to Day 6a of Advent of Code 2020: https://adventofcode.com/2020/day/6 """

def test_pos_results(test_result):
    """Simply return the number of unique characters in the string"""
    return len(set(test_result))

def cleanup(dirty_arr):
    """Munge the data in dirty_arr into a better array"""
    cleaned_up_arr = []
    temp_test = ""
    for current_line in dirty_arr:
        if len(current_line) == 0:
            cleaned_up_arr.append(temp_test)
            temp_test = ""
        else:
            if len(temp_test) == 0:
                temp_test += current_line
            else:
                temp_test += current_line
    cleaned_up_arr.append(temp_test)
    return cleaned_up_arr

def test_count(arr):
    """Count the number of valid passports in arr"""
    clean_arr = cleanup(arr)
    count = 0
    for test_data in clean_arr:
        count = count + test_pos_results(test_data)
    return count

with open("day-6.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

print(test_count(new_arr))
