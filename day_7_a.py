""" solution to Day 7a of Advent of Code 2020: https://adventofcode.com/2020/day/7 """

def contains_bags(data_arr,bag_arr):
    """Given an array of bags, find which bags can contain them and add to array"""
    new_bags = []
    for i in data_arr:
        test1_array = i.split()
        j = 5
        while j < len(test1_array):
            for k in bag_arr:
                test2_array = k.split()
                if test1_array[j] == test2_array[0] and test1_array[j+1] == test2_array[1]:
                    new_bags.append(test1_array[0] + " " + test1_array[1])
            j += 4
    for bag in new_bags:
        bag_arr.append(bag)

    # shiny gold bags can't hold shiny gold bags!
    if "shiny gold" in bag_arr:
        bag_arr.remove("shiny gold")
    return list(set(bag_arr))

def can_contain_gold_bag(arr):
    """Build list of bags that can eventually contain a gold bag"""
    gold_bag = ["shiny gold"]
    gold_bag_container = []

    # finding which ones can directly hold a gold bag
    gold_bag_container = contains_bags(arr, gold_bag)

    # finding which bags can hold those bags, iteratively
    temp_len = 0
    while temp_len < len(gold_bag_container):
        temp_len = len(gold_bag_container)
        gold_bag_container = contains_bags(arr, gold_bag_container)

    return len(gold_bag_container)

with open("day-7.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

print(can_contain_gold_bag(new_arr))
