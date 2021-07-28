""" solution to Day 16b of Advent of Code 2020: https://adventofcode.com/2020/day/16 """

import re

def departure_product(fields,ticket):
    """ Return the product of all ticket fields starting with departure """
    product = 1
    i = 0

    ticket_array = ticket.split(",")

    for field in fields:
        if "departure" in field:
            product = product * int(ticket_array[i])
        i += 1
    return product

def fields_condenser(fields):
    """ condenses the fields so that we can identify which field is which """

    # check if all fields are solo
    all_solo = True
    for field in fields:
        if "," in field:
            all_solo = False
    if all_solo:
        # if they're all solo, we need to strip trailing Xs
        i = 0
        for field in fields:
            fields[i] = field[0:-1]
            i += 1
        return fields
    
    # if not, find the first solo field without an X on the end
    i = 0
    solo_field = ""
    is_solo = True
    for field in fields:
        if "," in field:
            i += 1
        elif is_solo and field[-1] != "X":
            is_solo = False
            solo_field = field
            fields[i] = field + "X" # append an X to it once we pull it out
        else:
            i += 1

    if len(solo_field) == 0:
        return fields

    # update all fields to remove the solo field
    i = 0
    for field in fields:
        if solo_field in field and "," in field:
            field = re.sub(solo_field,"",field)
            field = re.sub(",,",",",field)
            if field[0] == ",":
               field = field[1::]
            if field[-1] == ",":
               field = field[0:-1]
            fields[i] = field
        i += 1
    return fields_condenser(fields)

def is_valid_field(range1,range2,fields):
    """ Validation of a field to throw out garbage tickets """
    range1_nums = range1.split("-")
    range2_nums = range2.split("-")
    range1_start = int(range1_nums[0])
    range1_end = int(range1_nums[1])
    range2_start = int(range2_nums[0])
    range2_end = int(range2_nums[1])

    fields_individual = fields.split(",")

    is_valid = True

    for field in fields_individual:
        intfield = int(field)
        if intfield < range1_start or intfield > range2_end or (intfield > range1_end and intfield < range2_start):
            is_valid = False

    return is_valid

def get_valid_tickets(valid_values,ticket_array):
    """ Return a list of valid tickets """
    valid_tickets = []
    for j in ticket_array:
        ticket_split = j.split(",")
        k = 0
        valid_ticket = True
        while k < len(ticket_split):
            if int(ticket_split[k]) not in valid_values:
                valid_ticket = False 
            k += 1
        if valid_ticket:
            valid_tickets.append(j)
    return valid_tickets

def get_ordered_fields(valid_tickets,range_values):
    """ Returns the ticket fields """
    fields = []
    j = 0
    while j < 20:
        fields.append("")
        for fieldlist in valid_tickets:
            valid_ticket_fields = fieldlist.split(",")
            if len(fields[j]) > 0:
                fields[j] = fields[j] + "," + valid_ticket_fields[j]
            else:
                fields[j] = valid_ticket_fields[j]
        j += 1

    ordered_field_names = [""] * len(range_values)
    n = 0
    for range_value in range_values:
        range_value_array = range_value.split(": ")
        range_name = range_value_array[0]
        ranges = range_value_array[1].split(" or ")
        range_no_1 = ranges[0]
        range_no_2 = ranges[1]
        n = 0
        for field in fields:
            if is_valid_field(range_no_1,range_no_2,field):
                if len(ordered_field_names[n]) > 0:
                    ordered_field_names[n] = ordered_field_names[n] + "," + range_name
                else:
                    ordered_field_names[n] = range_name
            n += 1
    fields = fields_condenser(ordered_field_names)
    return fields

# Data munging, then driver

with open("day-16.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

i = 0
range_array = []
range_values = []

while len(new_arr[i]) > 0:
    range_values.append(new_arr[i])
    line_arr = new_arr[i].split(":")
    values = line_arr[1].strip()
    ranges = values.split(" ")
    range_array.append(ranges[0])
    range_array.append(ranges[2])
    i += 1

valid_values = []

for range in range_array:
    borders = range.split("-")
    start = int(borders[0])
    stop = int(borders[1])
    j = start
    while j <= stop:
        valid_values.append(j)
        j += 1

valid_values_u = set(valid_values)
valid_values_f = list(valid_values_u)

i += 2 # skipping header rows

my_ticket = new_arr[i]

i += 3 # skipping header rows

tickets_array = []

while i < len(new_arr):
    tickets_array.append(new_arr[i])
    i += 1

valid_tickets = get_valid_tickets(valid_values_f,tickets_array)
fields_ordered = get_ordered_fields(valid_tickets,range_values)
print(departure_product(fields_ordered,my_ticket))
