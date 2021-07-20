""" solution to Day 14a of Advent of Code 2020: https://adventofcode.com/2020/day/14 """

def apply_mask(mask,value):
    """ Apply the mask to the value """
    # very kludge-y application of the mask by converting input to binary string
    #  then applying mask then converting result back to int, but it works fast
    # definitely a better way of doing this if more speed desired later

    value_string = ""
    temp_value = value
    while temp_value > 0:
        if temp_value % 2 == 1:
            value_string = "1" + value_string
            temp_value = (temp_value - 1) / 2
        else:
            value_string = "0" + value_string
            temp_value = temp_value / 2
    while len(value_string) < 36:
        value_string = "0" + value_string

    i = 0
    while i < len(value_string):
        if mask[i] == "0":
            temp_string = list(value_string)
            temp_string[i] = "0"
            value_string = "".join(temp_string)
        elif mask[i] == "1":
            temp_string = list(value_string)
            temp_string[i] = "1"
            value_string = "".join(temp_string)
        i += 1

    value_string = value_string[::-1] 
    multiplier = 1
    result = 0
    for i in value_string:
        result += multiplier * int(i)
        multiplier *= 2
    return result

def funct(arr):
    """Traverse the map stored in arr, incrementing result whenever you hit a tree (#)"""
    current_mask = ""
    string_dict = {}
    for item in arr:
        if item[0:4] == "mask":
            temp_array = item.split(" ")
            current_mask = temp_array[2]
        else:
            temp_array = item.split(" ")
            value = int(temp_array[2])
            temp_value = temp_array[0].split("[")
            temp_value = temp_value[1].split("]")
            temp_value = int(temp_value[0])
            string_dict[temp_value] = apply_mask(current_mask,value)
    return sum(string_dict.values())

with open("day-14.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

print(funct(new_arr))
