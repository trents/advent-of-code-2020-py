""" solution to Day 19b of Advent of Code 2020: https://adventofcode.com/2020/day/19 """

import re

def build_regex(ruleset,rule):
    regex_to_build = ""
    if rule == "\"a\"":
        return "a"
    if rule == "\"b\"":
        return "b"
    rule_process = ruleset[rule]
    if rule == "8":
# 8: 42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 42
        regex_to_build = "((" + build_regex(ruleset,"42") + ")|(" + build_regex(ruleset,"42") + build_regex(ruleset,"42") + ")|(" + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + ")|(" + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + ")|(" + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + ")|(" + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + "))"
    elif rule == "11":
# 11: 42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31
        regex_11 = "((" + build_regex(ruleset,"42") + build_regex(ruleset,"31") + ")|(" + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"31") + build_regex(ruleset,"31") + ")|(" + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"31") + build_regex(ruleset,"31") + build_regex(ruleset,"31") + ")|(" + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"31") + build_regex(ruleset,"31") + build_regex(ruleset,"31") + build_regex(ruleset,"31") + ")|(" + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"31") + build_regex(ruleset,"31") + build_regex(ruleset,"31") + build_regex(ruleset,"31") + build_regex(ruleset,"31") + ")|(" + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"42") + build_regex(ruleset,"31") + build_regex(ruleset,"31") + build_regex(ruleset,"31") + build_regex(ruleset,"31") + build_regex(ruleset,"31") + build_regex(ruleset,"31") + "))"
        regex_to_build = regex_11
    elif "|" in rule_process:
        rule_list = rule_process.split(" | ")
        rule_list1 = rule_list[0].split(" ")
        rule_list2 = rule_list[1].split(" ")
        regex_to_build = "(("
        for item in rule_list1:
            regex_to_build = regex_to_build + build_regex(ruleset,item.strip())
        regex_to_build = regex_to_build + ")|("
        for item in rule_list2:
            regex_to_build = regex_to_build + build_regex(ruleset,item.strip())
        regex_to_build = regex_to_build + "))"
    else:
        if rule_process == "a":
            return "a"
        elif rule_process == "b":
            return "b"
        else:
            regex_to_build = "("
            rule_list = rule_process.split()
            for item in rule_list:
                regex_to_build = regex_to_build + build_regex(ruleset,item)
            regex_to_build = regex_to_build + ")"
    return regex_to_build

def funct(rules,tests):
    rule_dict = {}
    for line in rules:
        temp_splitter = line.split(": ")
        rule_dict[temp_splitter[0]] = temp_splitter[1]
    regex = build_regex(rule_dict,str(0))
    regex = "\\A" + regex + "\\Z"
    reg_to_use = re.compile(regex)
    count = 0
    for line in tests:
        if reg_to_use.match(line):
            count += 1

    return count

with open("day-19.txt") as file:
    d = file.readlines()
rule_arr = []
test_arr = []
is_rules = True
for line in d:
    line = line.strip()
    if len(line) > 0:
        if is_rules:
           test_arr.append(line)
        else:
           rule_arr.append(line)
    else:
        is_rules = False

print(funct(test_arr,rule_arr))
