""" solution to Day 8b of Advent of Code 2020: https://adventofcode.com/2020/day/8 """
# I had to massively rewrite Day 8a because it didn't work at all for Day 8b

def operator(program):
    """This operates the program"""
    commands_seen = set()
    accumulator = 0
    index = 0
    while True:
        if index >= len(program):
            return accumulator
        command, argument = program[index]

        # If the program repeats a command, return False
        if index in commands_seen:
            return False
        commands_seen.add(index)
        if command == 'nop':
            index += 1
        elif command == 'acc':
            accumulator += argument
            index += 1
        elif command == 'jmp':
            index += argument
        else:
            return False
    return False

def swapper(program):
    """This goes through program, swapping "jmp" and "nop," until valid result"""
    for index, command in enumerate(program):
        if command[0] == 'nop' or command[0] == 'jmp':
            orig_command = command[0]
            if orig_command == 'nop':
                program[index][0] = 'jmp'
            elif orig_command == 'jmp':
                program[index][0] = 'nop'

            # Note: operator will either return False or return an int
            if accumulator := operator(program):
                return accumulator
            program[index][0] = orig_command

new_arr = []

with open("day-8.txt") as file:
    for line in file:
        line = line.rstrip().split(' ')
        new_arr.append([line[0], int(line[1])])

print(swapper(new_arr))
