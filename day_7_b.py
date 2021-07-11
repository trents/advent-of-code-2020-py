""" solution to Day 7b of Advent of Code 2020: https://adventofcode.com/2020/day/7 """

def bag_content_count(bag_number, bag_adj, bag_type, bag_arr):
    """Given an array of bags, recursively find how many bags are inside the given bags"""
    result = 0
    for k in bag_arr:
        test_bag_arr = k.split()
        if test_bag_arr[0] == bag_adj and test_bag_arr[1] == bag_type:
            size_bag_string = len(test_bag_arr)
            m_count = 4
            while m_count < size_bag_string:
                if test_bag_arr[m_count] != "no":
                    num_bags = int(test_bag_arr[m_count])
                    new_bag_p = test_bag_arr[m_count+1]
                    new_bag_t = test_bag_arr[m_count+2]
                    result += bag_content_count(num_bags, new_bag_p, new_bag_t, bag_arr)
                m_count += 4
    return bag_number + result * bag_number

def gold_bag_content_count(arr):
    """Count bags inside a shiny gold bag, then recursively see how many bags are in those"""
    gold_bag_content_cnt = 0

    for i in arr:
        test_arr = i.split()
        if test_arr[0] == "shiny" and test_arr[1] == "gold":
            size_gold_bag_string = len(test_arr)
            j = 4
            while j < size_gold_bag_string:
                num_bags = int(test_arr[j])
                bag_p = test_arr[j+1]
                bag_t = test_arr[j+2]
                gold_bag_content_cnt += bag_content_count(num_bags, bag_p, bag_t, arr)
                j += 4
    return gold_bag_content_cnt

with open("day-7.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

print(gold_bag_content_count(new_arr))
