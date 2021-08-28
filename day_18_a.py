""" solution to Day 18a of Advent of Code 2020: https://adventofcode.com/2020/day/18 """

def math_solver(equation):
    result = 0
    if "(" in equation:
        i = 0
        subeq_one = ""
        while equation[i] != "(":
            subeq_one = subeq_one + equation[i]
            i += 1
        j = i+1

        # now check for next matching parenthesis

        subeq_two = ""
        paren_count = 0
        matching_paren = False
        while matching_paren == False:
            if equation[j] == "(":
                paren_count += 1
                subeq_two = subeq_two + "("
            elif equation[j] == ")":
                if paren_count == 0:
                    matching_paren = True
                else:
                    subeq_two = subeq_two + equation[j]
                    paren_count -= 1
            else:
                subeq_two = subeq_two + equation[j]
            j += 1

        subeq_three = ""
        
        while j < len(equation):
            subeq_three = subeq_three + equation[j]
            j += 1

        if len(subeq_one) > 0:
            if subeq_one[-1] == "*" or subeq_one[-1] == "+":
                subeq_one = str(math_solver(subeq[0:-2])) + " " + subeq_one[-1]
 
        new_equation = subeq_one + str(math_solver(subeq_two)) + subeq_three

        result = math_solver(new_equation)

    else:
        split_eq = equation.split()
        next_operand = ""
        result = 0
        for value in split_eq:
            if value == "*" or value == "+":
                next_operand = value
            else:
                temp_num = int(value)
                if len(next_operand) < 1:
                    result = temp_num
                elif next_operand == "*":
                    result *= temp_num
                else:
                    result += temp_num
    return result

with open("day-18.txt") as file:
    d = file.readlines()
new_arr = []
for line in d:
    new_arr.append(line.strip())

sum_of_answers = 0

for entry in new_arr:
    sum_of_answers = sum_of_answers + int(math_solver(entry))

print(sum_of_answers)
