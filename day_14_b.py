""" solution to Day 14b of Advent of Code 2020: https://adventofcode.com/2020/day/14 """

def flatten(t):
    flat_list = []
    for sublist in t:
        if isinstance(sublist, str):
            flat_list.append(sublist)
        else:
            flat_list = flat_list + flatten(sublist)
    return flat_list

def value_of_address(value,address):
    """ Returns value of given address using rules from 14b """
    incrementer = 0
    big_set = []
    for char in address:
        if char == "X":
            string1 = address[0:incrementer] + "0" + address[incrementer+1:]
            string2 = address[0:incrementer] + "1" + address[incrementer+1:]
            return [value_of_address(value,string1), value_of_address(value,string2)]
        incrementer += 1
    return address

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
        if mask[i] == "1":
            temp_string = list(value_string)
            temp_string[i] = "1"
            value_string = "".join(temp_string)
        elif mask[i] == "X":
            temp_string = list(value_string)
            temp_string[i] = "X"
            value_string = "".join(temp_string)
        i += 1
    return value_string

def funct(arr):
    """Traverse the map stored in arr, incrementing result whenever you hit a tree (#)"""
    current_mask = ""
    result = 0
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
            temp_value = temp_value[0]
            string_dict[value] = apply_mask(current_mask,int(temp_value))
    values = string_dict.items()
    new_dict = {}
    for address in values:
        total = []
        total = total + value_of_address(int(address[0]),address[1])
        total = flatten(total)
        for entry in total:
            new_dict[entry] = int(address[0])
    return sum(new_dict.values())

with open("day-14.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

print(funct(new_arr))
