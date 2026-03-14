# assume that the function is split and each line of code is
# stored in a string inside a list, we loop
# so list[index] refers to each line in the string
# precondition : there is a white space around operators -saba

# i think += and -= should be in assignment instead of operators, im not going to move them this instant but
# this should be considered for making everything mesh in the future when we're refactoring this -ollie

def return_operations(split_string: str, operator: str):
    parts = split_string.split()
    operator_position = parts.index(operator)
    first_operand = parts[operator_position - 1]
    parts.pop(operator_position - 1)
    parts.pop(parts.index(operator))
    second_operand = " ".join(parts)
    return [first_operand, second_operand]

def identify_operations(split_string):
    if "+=" in split_string:
        result = return_operations(split_string, "+=")
        print("Increases {} by {}.".format(result[0], result[1]))
        return "Increases {} by {}.".format(result[0], result[1])
    elif "+" in split_string:
        result = return_operations(split_string, "+")
        print("Adds {} with {}".format(result[0], result[1]))
        return "Adds {} with {}".format(result[0], result[1])
    elif "-=" in split_string:
        result = return_operations(split_string, "-=")
        print("Decrease {} by {}.".format(result[0], result[1]))
        return "Decrease {} by {}.".format(result[0], result[1])
    elif "-" in split_string:
        result = return_operations(split_string, "-")
        print("Subtract {} from {}.".format(result[0], result[1]))
        return "Subtract {} from {}.".format(result[0], result[1])
    elif "**=" in split_string:
        # we should do this first otherwise we're not getting into this block
        result = return_operations(split_string, "**=")
        print("Set {} to itself raised to the power of {}.".format(result[0], result[1]))
        return "Set {} to itself raised to the power of {}.".format(result[0], result[1])
    elif "**" in split_string:
        result = return_operations(split_string, "**")
        print("Raise {} to the power of {}.".format(result[0], result[1]))
        return "Raise {} to the power of {}.".format(result[0], result[1])
    elif "*=" in split_string:
        # *= and * are translated the same
        result = return_operations(split_string, "*=")
        print("Multiply {} by {}.".format(result[0], result[1]))
        return "Multiply {} by {}.".format(result[0], result[1])
    elif "*" in split_string:
        # *= and * are translated the same
        result = return_operations(split_string, "*")
        print("Multiply {} with {}.".format(result[0], result[1]))
        return "Multiply {} with {}.".format(result[0], result[1])
    elif "//" in split_string:
        #ordering matters cause if we put / before this, we never get to // block
        result = return_operations(split_string, "//")
        print("Divide {} by {}, rounding down to the nearest whole number.".format(result[0], result[1]))
        return "Divide {} by {}, rounding down to the nearest whole number.".format(result[0], result[1])
    elif "/=" in split_string:
        result = return_operations(split_string, "/=")
        print("Divide {} by {}.".format(result[0], result[1]))
        return "Divide {} by {}.".format(result[0], result[1])
    elif "/" in split_string:
        result = return_operations(split_string, "/")
        print("Divide {} with {}.".format(result[0], result[1]))
        return "Divide {} with {}.".format(result[0], result[1])
    elif "%=" in split_string:
        result = return_operations(split_string, "%=")
        print("Set {} to the remainder when divided by {}.".format(result[0], result[1]))
        return "Set {} to the remainder when divided by {}.".format(result[0], result[1])
    elif "%" in split_string:
        result = return_operations(split_string, "%")
        print("Find the remainder when {} is divided by {}.".format(result[0], result[1]))
        return "Find the remainder when {} is divided by {}.".format(result[0], result[1])
    else:
        print(split_string)
        return split_string


def main():
    my_string = "x += y"
    identify_operations(my_string)
    my_second_string = "x + y"
    identify_operations(my_second_string)
    # i minorly refactored this function for this exact case. i feel like this reads a heck of a lot better than
    # "increases x by x added to y" which is what the recursive case would give us. i will look more into what
    # sort of edge cases this approach could produce though and we'll come up with a final decision tmrw
    my_third_string = "x += x + y"
    identify_operations(my_third_string)


if __name__ == "__main__":
    main()