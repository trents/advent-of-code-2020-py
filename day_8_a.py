""" solution to Day 8a of Advent of Code 2020: https://adventofcode.com/2020/day/8 """

def processor(instruction_array):
    """Traverse instructions in array, incrementing accumulator, until an instruction repeats"""
    processed_array = [True] * len(instruction_array)
    current_iter = 0
    accumulation = 0
    while processed_array[current_iter]:
        processed_array[current_iter] = False
        if instruction_array[current_iter][0] == "n":
            current_iter += 1
        elif instruction_array[current_iter][0] == "a":
            test_iter = instruction_array[current_iter].split()
            accumulation += int(test_iter[1])
            current_iter += 1
        elif instruction_array[current_iter][0] == "j":
            test_iter = instruction_array[current_iter].split()
            current_iter += int(test_iter[1])

    return accumulation

with open("day-8.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

print(processor(new_arr))
