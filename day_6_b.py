""" solution to Day 6b of Advent of Code 2020: https://adventofcode.com/2020/day/6 """

def test_pos_results(test_result):
    """Return the number of individual tests with common answers"""
    common_characters = [True] * 26
    test_result_array = test_result.split()
    for i, datum in enumerate(test_result_array):
        sec_common_characters = [False] * 26
        for j in range(len(datum)):
            sec_common_characters[ord(test_result_array[i][j]) - ord('a')] = True
        for k in range(26):
            if common_characters[k] and sec_common_characters[k]:
                common_characters[k] = True
            else:
                common_characters[k] = False
    return sum(common_characters)

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
                temp_test += " " + current_line
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
