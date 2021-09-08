""" solution to Day 21a of Advent of Code 2020: https://adventofcode.com/2020/day/21 """

def funct(arr):
    return 0 

with open("day-21.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

allergen_dict = {}

for item in new_arr:
    items = item.split(" (contains")
    items[1] = items[1].strip()
    items[1] = items[1][0:-1]
    allergens = items[1].split(", ")
    ingredients = items[0].split(" ")

    for key in allergen_dict.keys():
        if key in allergens:
            for ingred in allergen_dict[key]:
                if ingred not in ingredients:
                    allergen_dict[key].remove(ingred)

    for all_item in allergens:
        if allergen_dict.has_key(all_item):
            possible_ingredients = allergen_dict[all_item]
            new_possible_ingredients = []
            split_possible_ingredients = items[0].split()
            for poss in split_possible_ingredients:
                if poss in possible_ingredients:
                    new_possible_ingredients.append(poss)
            allergen_dict[all_item] = new_possible_ingredients
        else:
            allergen_dict[all_item] = items[0].split(" ")

print(allergen_dict)

count = 0

potential_allergens = []

for key in allergen_dict:
    potential_allergens = potential_allergens + allergen_dict[key]

unique_potential_allergens = list(set(potential_allergens))

for item in new_arr:
    items = item.split(" (contains")
    items[1] = items[1].strip()
    items[1] = items[1][0:-1]
    allergens = items[1].split(", ")
    ingredients = items[0].split(" ")

    for ingred in unique_potential_allergens:
       if ingred in ingredients:
           ingredients.remove(ingred)
    print(ingredients)
    count += len(ingredients)

print(count)
