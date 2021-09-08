""" solution to Day 22a of Advent of Code 2020: https://adventofcode.com/2020/day/22 """

def play_game(deck1, deck2):
    while len(deck1) > 0 and len(deck2) > 0:
        if deck1[0] > deck2[0]:
            deck1.append(deck1[0])
            deck1.append(deck2[0])
            del deck1[0]
            del deck2[0]
        else:
            deck2.append(deck2[0])
            deck2.append(deck1[0])
            del deck1[0]
            del deck2[0]

    if len(deck1) > 0:
        winning_deck = deck1
    else:
        winning_deck = deck2

    score = 0
    max_index = len(winning_deck) - 1
    for i in range(len(winning_deck)):
        score += (i+1) * winning_deck[max_index-i]
    return score

with open("day-22.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

deck1 = []
deck2 = []

curdeck = 1

i = 1

while i < len(new_arr):
    if curdeck == 1:
        if len(new_arr[i]) > 0:
            deck1.append(int(new_arr[i]))
        else:
            curdeck = 2
    if curdeck == 2:
        if len(new_arr[i]) > 0 and ":" not in new_arr[i]:
            deck2.append(int(new_arr[i]))

    i += 1

print(play_game(deck1, deck2))
