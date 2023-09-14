def arithmetic_arranger(problems, solve=False):
    # Error spotting
    if len(problems) > 5:
        return "Error: Too many problems."

    # 2D array for lines
    arranged_problems = [[], [], []]
    if solve:
        # To make a new line for the equation results
        arranged_problems.append([])

    equation_number = 0

    for prob in problems:
        equation_number += 1

        problem = prob.split(" ")

        first = problem[0]
        operator = problem[1]
        second = problem[2]

        # Error spotting
        if not (first.isnumeric() and second.isnumeric()):
            return "Error: Numbers must only contain digits."

        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        if not (operator == "+" or operator == "-"):
            return "Error: Operator must be '+' or '-'."

        # Formatting the equations
        equation_length = max(len(first), len(second)) + 2

        if len(first) >= len(second):
            arranged_problems[0].append(" " * 2 + first)
            arranged_problems[1].append(operator + " " * (equation_length - 1 - len(second)) + second)
        else:
            arranged_problems[0].append(" " * (equation_length - len(first)) + first)
            arranged_problems[1].append(operator + " " + second)

        arranged_problems[2].append("-" * equation_length)

        if solve:
            result = 0
            if operator == "+":
                result = int(first) + int(second)
            else:
                result = int(first) - int(second)

            arranged_problems[3].append(" " * (equation_length - len(str(result))) + str(result))

        # If the problem is not the last problem,
        # put 4 spaces after each equation,
        # otherwise, place "\n" character after
        # each line apart from the last one
        if equation_number != len(problems):
            for line in arranged_problems:
                line.append(" " * 4)
        else:
            for i in range(0, len(arranged_problems) - 1):
                arranged_problems[i].append("\n")

    arranged_string = []

    for line in arranged_problems:
        arranged_string.append("".join(line))

    return "".join(arranged_string)