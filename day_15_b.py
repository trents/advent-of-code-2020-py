""" solution to Day 15b of Advent of Code 2020: https://adventofcode.com/2020/day/15 """
# required complete rewrite from 15a because it was prohibitively slow with the much larger target

def funct(arr):
    """  """
    turn = 1
    ult = {}
    penult = {}
    numbers = arr[0].split(",")

    # initial seeding of dicts
    for i in range(len(numbers)):
        ult[int(numbers[i])] = turn
        penult[int(numbers[i])] = 0
        turn += 1
    
    target = int(numbers[-1])
    while turn <= 30000000:
        if penult[target] == 0:
            target = 0
            if target in ult:
                penult[target] = ult[target]
            else:
                penult[target] = 0
            ult[target] = turn
        else:
            num = ult[target] - penult[target]
            target = num
            if target not in ult.keys():
                penult[target] = 0
                ult[target] = turn
            else:
                penult[target] = ult[target]
                ult[target] = turn
        turn += 1
    return target

with open("day-15.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

print(funct(new_arr))
